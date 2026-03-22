"""
高质量宣传图片生成器 - 纯Python版本
使用PIL库生成投资价值宣传图片（无需外部图片和AI API）
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math

# 配置
OUTPUT_DIR = "D:\\game\\full_porject\\reddezhou\\assets\\screenshots\\promo\\"

# 宣传图片配置
PROMO_CONFIGS = [
    {
        "title": "投资德州扑克",
        "subtitle": "开启财富之门",
        "bg_color": (102, 126, 234),  # #667eea
        "gradient_colors": [(102, 126, 234), (118, 75, 162)],  # 渐变色
        "icon": "💰",
        "output": "promo-01-investment.png"
    },
    {
        "title": "德州扑克平台",
        "subtitle": "创业首选项目",
        "bg_color": (118, 75, 162),  # #764ba2
        "gradient_colors": [(118, 75, 162), (240, 147, 251)],
        "icon": "🎰",
        "output": "promo-02-poker.png"
    },
    {
        "title": "月入百万",
        "subtitle": "不是梦想",
        "bg_color": (240, 147, 251),  # #f093fb
        "gradient_colors": [(240, 147, 251), (245, 87, 108)],
        "icon": "📈",
        "output": "promo-03-growth.png"
    },
    {
        "title": "快速上线",
        "subtitle": "5-10天部署完成",
        "bg_color": (245, 87, 108),  # #f5576c
        "gradient_colors": [(245, 87, 108), (79, 172, 254)],
        "icon": "🚀",
        "output": "promo-04-startup.png"
    },
    {
        "title": "ROI 200%-500%",
        "subtitle": "3-6个月回本",
        "bg_color": (79, 172, 254),  # #4facfe
        "gradient_colors": [(79, 172, 254), (0, 242, 254)],
        "icon": "💎",
        "output": "promo-05-roi.png"
    },
    {
        "title": "全球市场",
        "subtitle": "500亿美元规模",
        "bg_color": (0, 242, 254),  # #00f2fe
        "gradient_colors": [(0, 242, 254), (250, 112, 154)],
        "icon": "🌍",
        "output": "promo-06-global.png"
    },
    {
        "title": "财富自由",
        "subtitle": "从德州扑克开始",
        "bg_color": (250, 112, 154),  # #fa709a
        "gradient_colors": [(250, 112, 154), (102, 126, 234)],
        "icon": "🏆",
        "output": "promo-07-wealth.png"
    }
]

def create_gradient_background(width, height, color1, color2):
    """创建渐变背景"""
    img = Image.new('RGB', (width, height))
    
    for y in range(height):
        # 计算渐变比例
        ratio = y / height
        
        # 计算当前行的颜色
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        
        # 绘制一行
        for x in range(width):
            img.putpixel((x, y), (r, g, b))
    
    return img

def add_decorative_elements(draw, width, height, bg_color):
    """添加装饰元素"""
    # 添加圆形装饰
    for i in range(5):
        x = (i * 200) + 100
        y = 100
        radius = 50 + (i * 10)
        
        # 绘制半透明圆形
        for r in range(radius, 0, -1):
            alpha = int(255 * (r / radius) * 0.1)
            color = (255, 255, 255, alpha)
            # PIL的ImageDraw不支持透明度，所以跳过
    
    # 添加线条装饰
    for i in range(3):
        y = 200 + (i * 100)
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 30), width=1)

def create_promo_image(config):
    """创建宣传图片"""
    try:
        print(f"🎨 正在生成: {config['output']}")
        
        # 图片尺寸
        width = 1024
        height = 1024
        
        # 创建渐变背景
        img = create_gradient_background(
            width, height,
            config['gradient_colors'][0],
            config['gradient_colors'][1]
        )
        
        # 创建绘图对象
        draw = ImageDraw.Draw(img)
        
        # 添加装饰元素
        add_decorative_elements(draw, width, height, config['bg_color'])
        
        # 尝试使用中文字体
        try:
            # 尝试多种中文字体
            font_paths = [
                "C:\\Windows\\Fonts\\msyh.ttc",  # 微软雅黑
                "C:\\Windows\\Fonts\\simhei.ttf",  # 黑体
                "C:\\Windows\\Fonts\\simsun.ttc",  # 宋体
                "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",  # Linux
            ]
            
            font_large = None
            font_small = None
            
            for font_path in font_paths:
                try:
                    font_large = ImageFont.truetype(font_path, 80)
                    font_small = ImageFont.truetype(font_path, 40)
                    break
                except:
                    continue
            
            if font_large is None:
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()
                
        except Exception as e:
            print(f"⚠️ 字体加载失败，使用默认字体: {e}")
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
        
        # 绘制图标（使用emoji）
        try:
            icon_font = ImageFont.truetype("seguiemj.ttf", 150) if os.path.exists("C:\\Windows\\Fonts\\seguiemj.ttf") else font_large
            icon_bbox = draw.textbbox((0, 0), config['icon'], font=icon_font)
            icon_width = icon_bbox[2] - icon_bbox[0]
            icon_x = (width - icon_width) // 2
            draw.text((icon_x, 250), config['icon'], fill="white", font=icon_font)
        except:
            print("⚠️ 图标绘制失败，跳过")
        
        # 绘制标题
        title = config['title']
        title_bbox = draw.textbbox((0, 0), title, font=font_large)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (width - title_width) // 2
        title_y = 500
        
        # 添加文字阴影
        shadow_offset = 3
        draw.text((title_x + shadow_offset, title_y + shadow_offset), title, fill=(0, 0, 0, 100), font=font_large)
        draw.text((title_x, title_y), title, fill="white", font=font_large)
        
        # 绘制副标题
        subtitle = config['subtitle']
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
        subtitle_x = (width - subtitle_width) // 2
        subtitle_y = 620
        
        draw.text((subtitle_x + shadow_offset, subtitle_y + shadow_offset), subtitle, fill=(0, 0, 0, 100), font=font_small)
        draw.text((subtitle_x, subtitle_y), subtitle, fill="white", font=font_small)
        
        # 添加底部装饰线
        draw.line([(100, height - 100), (width - 100, height - 100)], fill=(255, 255, 255, 100), width=2)
        
        # 添加底部文字
        footer_text = "红德州 - 完整的德州扑克平台解决方案"
        footer_bbox = draw.textbbox((0, 0), footer_text, font=font_small)
        footer_width = footer_bbox[2] - footer_bbox[0]
        footer_x = (width - footer_width) // 2
        footer_y = height - 80
        
        draw.text((footer_x, footer_y), footer_text, fill=(255, 255, 255, 200), font=font_small)
        
        # 保存图片
        output_path = os.path.join(OUTPUT_DIR, config['output'])
        img.save(output_path, 'PNG', quality=95)
        
        print(f"✅ 已生成: {config['output']}")
        return True
        
    except Exception as e:
        print(f"❌ 生成失败: {config['output']}")
        print(f"   错误信息: {str(e)}")
        return False

def main():
    """主函数"""
    print("🚀 开始生成高质量宣传图片...")
    print(f"📁 输出目录: {OUTPUT_DIR}")
    
    # 创建输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 生成图片
    success_count = 0
    for i, config in enumerate(PROMO_CONFIGS):
        print(f"\n[{i+1}/{len(PROMO_CONFIGS)}] 处理: {config['output']}")
        
        if create_promo_image(config):
            success_count += 1
    
    print(f"\n🎉 完成！成功生成 {success_count}/{len(PROMO_CONFIGS)} 张图片")
    print(f"📁 图片保存在: {OUTPUT_DIR}")
    
    # 显示生成的图片列表
    print("\n📋 生成的图片列表:")
    for config in PROMO_CONFIGS:
        print(f"  - {config['output']}: {config['title']} - {config['subtitle']}")

if __name__ == "__main__":
    main()
