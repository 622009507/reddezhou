// Photoshop脚本 - 高质量宣传图片生成器（综合版）
// 使用方法：在Photoshop中 文件 > 脚本 > 浏览，选择此脚本运行

// 配置信息
var INPUT_DIR = "D:\\game\\full_porject\\reddezhou\\assets\\screenshots\\promo\\input\\";  // 输入图片目录
var OUTPUT_DIR = "D:\\game\\full_porject\\reddezhou\\assets\\screenshots\\promo\\";  // 输出目录

// 宣传图片配置
var PROMO_CONFIGS = [
    {
        title: "投资德州扑克",
        subtitle: "开启财富之门",
        bgColor: [102, 126, 234],  // #667eea
        textColor: [255, 255, 255],  // 白色
        fontSize: 60,
        subtitleSize: 30
    },
    {
        title: "德州扑克平台",
        subtitle: "创业首选项目",
        bgColor: [118, 75, 162],  // #764ba2
        textColor: [255, 255, 255],
        fontSize: 60,
        subtitleSize: 30
    },
    {
        title: "月入百万",
        subtitle: "不是梦想",
        bgColor: [240, 147, 251],  // #f093fb
        textColor: [255, 255, 255],
        fontSize: 60,
        subtitleSize: 30
    },
    {
        title: "快速上线",
        subtitle: "5-10天部署完成",
        bgColor: [245, 87, 108],  // #f5576c
        textColor: [255, 255, 255],
        fontSize: 60,
        subtitleSize: 30
    },
    {
        title: "ROI 200%-500%",
        subtitle: "3-6个月回本",
        bgColor: [79, 172, 254],  // #4facfe
        textColor: [255, 255, 255],
        fontSize: 60,
        subtitleSize: 30
    },
    {
        title: "全球市场",
        subtitle: "500亿美元规模",
        bgColor: [0, 242, 254],  // #00f2fe
        textColor: [255, 255, 255],
        fontSize: 60,
        subtitleSize: 30
    },
    {
        title: "财富自由",
        subtitle: "从德州扑克开始",
        bgColor: [250, 112, 154],  // #fa709a
        textColor: [255, 255, 255],
        fontSize: 60,
        subtitleSize: 30
    }
];

// 主函数
function main() {
    // 检查输入目录是否存在
    var inputFolder = new Folder(INPUT_DIR);
    if (!inputFolder.exists) {
        alert("❌ 输入目录不存在！\n\n请创建以下目录并放入图片：\n" + INPUT_DIR);
        return;
    }
    
    // 获取输入目录中的所有图片文件
    var files = inputFolder.getFiles(/\.(jpg|jpeg|png|bmp|gif)$/i);
    
    if (files.length === 0) {
        alert("❌ 输入目录中没有图片文件！\n\n请将图片放入以下目录：\n" + INPUT_DIR);
        return;
    }
    
    // 创建输出目录
    var outputFolder = new Folder(OUTPUT_DIR);
    if (!outputFolder.exists) {
        outputFolder.create();
    }
    
    // 显示开始提示
    var startMsg = "🚀 开始生成宣传图片...\n\n";
    startMsg += "📁 输入目录: " + INPUT_DIR + "\n";
    startMsg += "📁 输出目录: " + OUTPUT_DIR + "\n";
    startMsg += "🖼️ 找到 " + files.length + " 张图片\n\n";
    startMsg += "点击确定开始生成...";
    alert(startMsg);
    
    // 处理每张图片
    var successCount = 0;
    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        var config = PROMO_CONFIGS[i % PROMO_CONFIGS.length];
        
        $.writeln("\n[" + (i+1) + "/" + files.length + "] 处理: " + file.name);
        
        if (processImage(file, config, i)) {
            successCount++;
        }
    }
    
    // 显示完成提示
    var endMsg = "🎉 完成！\n\n";
    endMsg += "✅ 成功生成: " + successCount + "/" + files.length + " 张图片\n";
    endMsg += "📁 输出目录: " + OUTPUT_DIR;
    alert(endMsg);
}

// 处理单张图片
function processImage(inputFile, config, index) {
    try {
        // 打开图片
        var doc = app.open(inputFile);
        
        // 调整图片大小（统一为1024x1024）
        var width = doc.width.value;
        var height = doc.height.value;
        var size = Math.min(width, height);
        
        // 如果图片不是正方形，裁剪为正方形
        if (width !== height) {
            var left = (width - size) / 2;
            var top = (height - size) / 2;
            doc.crop([left, top, left + size, top + size]);
        }
        
        // 调整大小为1024x1024
        doc.resizeImage(1024, 1024, 72, ResampleMethod.BICUBIC);
        
        // 添加半透明渐变背景（底部）
        addGradientBackground(doc, config.bgColor);
        
        // 添加标题文字
        addTextLayer(doc, config.title, config.fontSize, config.textColor, 1024/2, 1024 - 150);
        
        // 添加副标题文字
        addTextLayer(doc, config.subtitle, config.subtitleSize, config.textColor, 1024/2, 1024 - 80);
        
        // 保存为PNG
        var outputFile = new File(OUTPUT_DIR + "promo-" + String(index + 1).padStart(2, '0') + ".png");
        var pngOptions = new PNGSaveOptions();
        pngOptions.compression = 9;
        pngOptions.interlaced = false;
        
        doc.saveAs(outputFile, pngOptions, true, Extension.LOWERCASE);
        doc.close(SaveOptions.DONOTSAVECHANGES);
        
        $.writeln("✅ 已生成: promo-" + String(index + 1).padStart(2, '0') + ".png");
        return true;
        
    } catch (e) {
        $.writeln("❌ 处理失败: " + inputFile.name + " - " + e.message);
        return false;
    }
}

// 添加渐变背景
function addGradientBackground(doc, bgColor) {
    // 创建新图层
    var bgLayer = doc.artLayers.add();
    bgLayer.name = "Gradient Background";
    bgLayer.move(doc.activeLayer, ElementPlacement.PLACEATBEGINNING);
    
    // 选择底部区域
    var bottom = doc.height.value - 200;
    doc.selection.select([
        [0, bottom],
        [doc.width.value, bottom],
        [doc.width.value, doc.height.value],
        [0, doc.height.value]
    ]);
    
    // 创建渐变
    var gradient = new Gradient();
    gradient.type = GradientType.LINEAR;
    
    // 设置渐变颜色（从透明到半透明）
    var startColor = new RGBColor();
    startColor.red = bgColor[0];
    startColor.green = bgColor[1];
    startColor.blue = bgColor[2];
    
    // 填充渐变
    var fillColor = new SolidColor();
    fillColor.rgb = startColor;
    
    // 设置透明度
    bgLayer.opacity = 80;
    
    // 填充颜色
    doc.selection.fill(fillColor);
    doc.selection.deselect();
}

// 添加文字图层
function addTextLayer(doc, text, fontSize, textColor, x, y) {
    var textLayer = doc.artLayers.add();
    textLayer.name = "Text: " + text;
    textLayer.kind = LayerKind.TEXT;
    
    var textItem = textLayer.textItem;
    textItem.contents = text;
    textItem.size = fontSize;
    textItem.font = "SimHei";  // 使用黑体
    
    // 设置颜色
    textItem.color.rgb.red = textColor[0];
    textItem.color.rgb.green = textColor[1];
    textItem.color.rgb.blue = textColor[2];
    
    // 设置位置（居中）
    textItem.justification = Justification.CENTER;
    textItem.position = [x, y];
    
    // 添加阴影效果
    textLayer.layerEffects = new LayerEffects();
    textLayer.layerEffects.dropShadow = new DropShadowEffect();
    textLayer.layerEffects.dropShadow.enabled = true;
    textLayer.layerEffects.dropShadow.opacity = 50;
    textLayer.layerEffects.dropShadow.distance = 5;
    textLayer.layerEffects.dropShadow.size = 10;
}

// 运行主函数
main();
