# 高质量宣传图片快速生成指南

## 🎯 目标
快速生成高质量的投资价值宣传图片，吸引买家注意

## 📋 三种方案

### 方案一：AI API生成（推荐）

#### 步骤1：获取OpenAI API密钥
1. 访问：https://platform.openai.com/api-keys
2. 注册并登录OpenAI账号
3. 创建API密钥
4. 复制API密钥

#### 步骤2：配置API密钥
打开 `generate_promo_images_ai.py` 文件，找到以下代码：
```python
openai.api_key = "your-openai-api-key-here"
```
替换为您的API密钥：
```python
openai.api_key = "sk-your-actual-api-key-here"
```

#### 步骤3：运行脚本
```bash
cd d:\game\full_porject\reddezhou
python generate_promo_images_ai.py
```

#### 步骤4：查看生成的图片
图片将保存在：`D:\game\full_porject\reddezhou\assets\screenshots\promo\`

---

### 方案二：下载图片 + PS脚本处理（最推荐）

#### 步骤1：下载高质量图片

**推荐网站**：
1. **Unsplash**：https://unsplash.com
   - 搜索关键词：investment, business, money, success, poker
   
2. **Pexels**：https://www.pexels.com
   - 搜索关键词：wealth, finance, startup, entrepreneur
   
3. **Pixabay**：https://pixabay.com
   - 搜索关键词：gold, coins, chart, growth

**推荐搜索关键词**：
- investment（投资）
- business success（商业成功）
- money growth（财富增长）
- poker chips（扑克筹码）
- startup（创业）
- wealth（财富）
- finance（金融）

#### 步骤2：创建输入目录
```bash
mkdir "D:\game\full_porject\reddezhou\assets\screenshots\promo\input"
```

#### 步骤3：将下载的图片放入输入目录
将下载的图片放入：
`D:\game\full_porject\reddezhou\assets\screenshots\promo\input\`

#### 步骤4：运行PS脚本
1. 打开Photoshop
2. 文件 > 脚本 > 浏览
3. 选择 `photoshop_script_comprehensive.jsx`
4. 点击确定运行

#### 步骤5：查看生成的图片
图片将保存在：`D:\game\full_porject\reddezhou\assets\screenshots\promo\`

---

### 方案三：手动制作（最灵活）

#### 步骤1：下载高质量图片
从Unsplash、Pexels、Pixabay下载图片

#### 步骤2：使用Photoshop手动制作
1. 打开图片
2. 添加渐变背景
3. 添加标题文字
4. 添加副标题文字
5. 保存为PNG

---

## 🎨 推荐图片类型

### 1. 投资价值类
- **市场规模**：地球、图表、增长曲线
- **盈利模式**：金币、钞票、收入图表
- **投资回报**：ROI图表、增长曲线

### 2. 创业优势类
- **启动门槛**：启动按钮、门槛图标
- **快速上线**：火箭、速度图标
- **技术支持**：技术图标、支持图标

### 3. 盈利前景类
- **月收入**：收入图表、金币堆
- **回本周期**：时间轴、回本曲线
- **现金流**：现金流图表、钱流图标

### 4. 成功案例类
- **案例展示**：成功案例、数据对比
- **用户评价**：好评图标、用户头像
- **运营数据**：数据图表、增长曲线

---

## 📝 宣传语设计

### 主标题
- "投资德州扑克，开启财富之门！"
- "月入百万，不是梦想！"
- "创业首选，德州扑克平台！"
- "3-6个月回本，ROI 200%-500%！"

### 副标题
- "全球市场500亿美元，中国用户3亿+"
- "启动资金10-30万，5-10天快速上线"
- "技术成熟稳定，盈利模式清晰"
- "专业团队支持，全程技术指导"

---

## 💡 执行建议

### 推荐执行顺序
1. **方案二**：下载图片 + PS脚本处理（最快）
2. **方案一**：AI API生成（最智能）
3. **方案三**：手动制作（最灵活）

### 时间预估
- **方案一**：10-20分钟（需要API密钥）
- **方案二**：20-30分钟（需要下载图片）
- **方案三**：60-90分钟（需要手动制作）

---

## 🚀 立即开始

### 快速开始（推荐）
```bash
# 1. 创建输入目录
mkdir "D:\game\full_porject\reddezhou\assets\screenshots\promo\input"

# 2. 下载图片到输入目录
# 访问 Unsplash.com 搜索 "investment" 并下载图片

# 3. 运行PS脚本
# 打开Photoshop > 文件 > 脚本 > 浏览 > photoshop_script_comprehensive.jsx
```

---

## 📞 需要帮助？

如果遇到问题，请检查：
1. ✅ 输入目录是否存在
2. ✅ 输入目录中是否有图片
3. ✅ Photoshop是否正确安装
4. ✅ API密钥是否正确配置

---

**开始制作高质量宣传图片吧！** 🎨

**吸引买家，展示投资价值！** 💰
