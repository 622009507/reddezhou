"""
高质量宣传图片生成器 - AI API版本
使用DALL-E API生成投资价值宣传图片
"""

import openai
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

# 配置
OUTPUT_DIR = "D:\\game\\full_porject\\reddezhou\\assets\\screenshots\\promo\\"

# OpenAI API配置
# 请替换为您的API密钥
openai.api_key = "your-openai-api-key-here"

# 宣传图片配置
PROMO_CONFIGS = [
    {
        "prompt": "professional investment poster, gold coins and money stacks, business success, modern elegant design, high quality, 4k",
        "title": "投资德州扑克",
        "subtitle": "开启财富之门",
        "output": "promo-01-investment.png"
    },
    {
        "prompt": "poker chips and cards on casino table, texas hold'em, professional lighting, elegant atmosphere, high quality photo",
        "title": "德州扑克平台",
        "subtitle": "创业首选项目",
        "output": "promo-02-poker.png"
    },
    {
        "prompt": "business growth chart going up, money and success, modern infographic design, professional, high quality",
        "title": "月入百万",
        "subtitle": "不是梦想",
        "output": "promo-03-growth.png"
    },
    {
        "prompt": "startup business team working together, modern office, success and collaboration, professional photo, high quality",
        "title": "快速上线",
        "subtitle": "5-10天部署完成",
        "output": "promo-04-startup.png"
    },
    {
        "prompt": "ROI return on investment concept, money growing, financial success, modern design, professional quality",
        "title": "ROI 200%-500%",
        "subtitle": "3-6个月回本",
        "output": "promo-05-roi.png"
    },
    {
        "prompt": "global market world map with connections, international business, modern technology, professional design",
        "title": "全球市场",
        "subtitle": "500亿美元规模",
        "output": "promo-06-global.png"
    },
    {
        "prompt": "wealth and prosperity, gold and diamonds, luxury lifestyle, elegant design, high quality photo",
        "title": "财富自由",
        "subtitle": "从德州扑克开始",
        "output": "promo-07-wealth.png"
    }
]

def generate_image_with_dalle(prompt, output_path):
    """使用DALL-E生成图片"""
    try:
        print(f"🎨 正在生成图片: {prompt[:50]}...")
        
        # 调用DALL-E API
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            quality="standard"
        )
        
        # 获取图片URL
        image_url = response['data'][0]['url']
        
        # 下载图片
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        
        # 保存图片
        image.save(output_path, 'PNG', quality=95)
        print(f"✅ 图片已保存: {output_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ 生成图片失败: {str(e)}")
        return False

def add_text_to_image(image_path, title, subtitle, output_path):
    """在图片上添加文字"""
    try:
        # 打开图片
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        
        # 尝试使用中文字体
        try:
            font_large = ImageFont.truetype("msyh.ttc", 60)
            font_small = ImageFont.truetype("msyh.ttc", 30)
        except:
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
        
        # 计算文字位置（居中）
        width, height = img.size
        
        # 绘制半透明背景
        overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.rectangle([(0, height - 200), (width, height)], fill=(0, 0, 0, 180))
        img = img.convert('RGBA')
        img = Image.alpha_composite(img, overlay)
        
        # 重新创建绘图对象
        draw = ImageDraw.Draw(img)
        
        # 绘制标题
        title_bbox = draw.textbbox((0, 0), title, font=font_large)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (width - title_width) // 2
        title_y = height - 180
        
        draw.text((title_x, title_y), title, fill="white", font=font_large)
        
        # 绘制副标题
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
        subtitle_x = (width - subtitle_width) // 2
        subtitle_y = height - 100
        
        draw.text((subtitle_x, subtitle_y), subtitle, fill="white", font=font_small)
        
        # 保存图片
        img = img.convert('RGB')
        img.save(output_path, 'PNG', quality=95)
        print(f"✅ 文字已添加: {output_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ 添加文字失败: {str(e)}")
        return False

def main():
    """主函数"""
    print("🚀 开始生成高质量宣传图片...")
    print(f"📁 输出目录: {OUTPUT_DIR}")
    
    # 创建输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 检查API密钥
    if openai.api_key == "your-openai-api-key-here":
        print("❌ 请先配置OpenAI API密钥！")
        print("📝 请将代码中的 'your-openai-api-key-here' 替换为您的API密钥")
        print("🔑 获取API密钥: https://platform.openai.com/api-keys")
        return
    
    # 生成图片
    success_count = 0
    for i, config in enumerate(PROMO_CONFIGS):
        print(f"\n[{i+1}/{len(PROMO_CONFIGS)}] 处理: {config['output']}")
        
        # 生成图片
        temp_path = OUTPUT_DIR + "temp_" + config['output']
        if generate_image_with_dalle(config['prompt'], temp_path):
            # 添加文字
            final_path = OUTPUT_DIR + config['output']
            if add_text_to_image(temp_path, config['title'], config['subtitle'], final_path):
                success_count += 1
            
            # 删除临时文件
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    print(f"\n🎉 完成！成功生成 {success_count}/{len(PROMO_CONFIGS)} 张图片")
    print(f"📁 图片保存在: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
