# GitHub Pages部署指南

## 🎯 目标

将红德州Demo部署到GitHub Pages，让买家可以通过URL访问Demo。

## 🚀 部署步骤

### 方法1：使用GitHub网页界面（推荐）

#### 步骤1：上传文件到GitHub

1. **访问GitHub仓库**
   - 打开浏览器
   - 访问：https://github.com/622009507/reddezhou

2. **上传demo.html文件**
   - 点击"Add file" → "Upload files"
   - 拖拽或选择 `demo.html` 文件
   - 在"Commit changes"中填写提交信息：
     - "Add demo.html for GitHub Pages"
   - 点击"Commit changes"按钮

3. **上传assets目录**
   - 点击"Add file" → "Upload files"
   - 拖拽或选择整个 `assets` 目录
   - 在"Commit changes"中填写提交信息：
     - "Add assets directory with screenshots"
   - 点击"Commit changes"按钮

#### 步骤2：启用GitHub Pages

1. **进入Settings页面**
   - 在GitHub仓库页面
   - 点击"Settings"标签

2. **找到Pages设置**
   - 在左侧菜单中找到"Pages"
   - 点击进入Pages设置页面

3. **配置Pages**
   - **Source**：选择"Deploy from a branch"
   - **Branch**：选择"main"分支
   - **Folder**：选择"/ (root)"目录
   - 点击"Save"按钮

4. **等待部署完成**
   - GitHub会自动部署
   - 通常需要1-5分钟
   - 部署完成后会显示访问地址

#### 步骤3：访问Demo

1. **获取访问地址**
   - 部署完成后，GitHub会显示访问地址
   - 格式通常是：`https://622009507.github.io/reddezhou/`

2. **访问Demo**
   - 在浏览器中访问：`https://622009507.github.io/reddezhou/demo.html`
   - 或者访问根目录：`https://622009507.github.io/reddezhou/`

---

### 方法2：使用Git命令行

#### 步骤1：添加文件到Git

```bash
cd d:\game\full_porject\reddezhou

# 添加demo.html
git add demo.html

# 添加assets目录
git add assets/

# 提交更改
git commit -m "Add demo.html and assets for GitHub Pages"
```

#### 步骤2：推送到GitHub

```bash
# 推送到GitHub
git push origin main
```

#### 步骤3：启用GitHub Pages

1. **访问GitHub仓库**
   - 打开浏览器
   - 访问：https://github.com/622009507/reddezhou

2. **进入Settings页面**
   - 点击"Settings"标签

3. **找到Pages设置**
   - 在左侧菜单中找到"Pages"
   - 点击进入Pages设置页面

4. **配置Pages**
   - **Source**：选择"Deploy from a branch"
   - **Branch**：选择"main"分支
   - **Folder**：选择"/ (root)"目录
   - 点击"Save"按钮

5. **等待部署完成**
   - GitHub会自动部署
   - 通常需要1-5分钟

---

### 方法3：使用gh CLI工具

#### 步骤1：安装GitHub CLI

```bash
# Windows
winget install --id GitHub.cli

# 或者使用chocolatey
choco install gh
```

#### 步骤2：登录GitHub

```bash
gh auth login
```

#### 步骤3：启用GitHub Pages

```bash
cd d:\game\full_porject\reddezhou

# 启用GitHub Pages
gh api -X POST repos/622009507/reddezhou/pages \
  -f source[branch]=main \
  -f source[path]=/
```

#### 步骤4：等待部署完成

- GitHub会自动部署
- 通常需要1-5分钟
- 可以通过以下命令查看部署状态：

```bash
gh api repos/622009507/reddezhou/pages
```

---

## 📋 验证部署

### 检查部署状态

1. **访问GitHub Pages设置**
   - 访问：https://github.com/622009507/reddezhou/settings/pages

2. **查看部署状态**
   - 查看部署状态
   - 查看访问地址
   - 查看部署日志

### 访问Demo

1. **访问根目录**
   - https://622009507.github.io/reddezhou/

2. **访问Demo页面**
   - https://622009507.github.io/reddezhou/demo.html

3. **访问截图**
   - https://622009507.github.io/reddezhou/assets/screenshots/backend/backend-01-login.png
   - https://622009507.github.io/reddezhou/assets/screenshots/backend/backend-02-dashboard.png

---

## 🔧 故障排除

### 问题1：部署失败

**原因**：
- 文件路径错误
- 文件大小超限
- 网络问题

**解决方案**：
1. 检查文件路径是否正确
2. 压缩大文件
3. 检查网络连接
4. 查看GitHub Pages日志

### 问题2：访问404

**原因**：
- 部署未完成
- 文件路径错误
- URL错误

**解决方案**：
1. 等待部署完成（1-5分钟）
2. 检查文件路径
3. 检查URL是否正确
4. 查看GitHub Pages设置

### 问题3：图片无法加载

**原因**：
- 图片路径错误
- 图片未上传
- 大小写问题

**解决方案**：
1. 检查图片路径
2. 确认图片已上传
3. 检查文件名大小写
4. 使用相对路径

---

## 🎯 自定义域名（可选）

### 步骤1：添加自定义域名

1. **进入GitHub Pages设置**
   - 访问：https://github.com/622009507/reddezhou/settings/pages

2. **添加自定义域名**
   - 在"Custom domain"中输入您的域名
   - 例如：`demo.yourdomain.com`

### 步骤2：配置DNS

1. **添加CNAME记录**
   - 访问您的域名DNS管理
   - 添加CNAME记录：
     - **主机记录**：demo
     - **记录值**：622009507.github.io

2. **等待DNS生效**
   - 通常需要24-48小时
   - 可以使用`nslookup`检查

### 步骤3：验证域名

1. **访问自定义域名**
   - 访问：http://demo.yourdomain.com
   - 检查是否正常访问

---

## 📊 监控和优化

### 查看访问统计

1. **GitHub Insights**
   - 访问：https://github.com/622009507/reddezhou/graphs/traffic
   - 查看访问统计
   - 查看访问来源

2. **Google Analytics**
   - 在demo.html中添加Google Analytics代码
   - 跟踪用户行为
   - 分析访问数据

### 优化加载速度

1. **压缩图片**
   - 使用TinyPNG等工具压缩图片
   - 减少图片大小
   - 提高加载速度

2. **启用CDN**
   - 使用GitHub Pages自带的CDN
   - 加速静态资源加载

3. **优化代码**
   - 压缩HTML、CSS、JavaScript
   - 减少HTTP请求
   - 提高加载速度

---

## 🎉 完成

部署完成后，买家就可以通过以下URL访问Demo：

- **Demo页面**：https://622009507.github.io/reddezhou/demo.html
- **根目录**：https://622009507.github.io/reddezhou/

---

**立即开始部署吧！** 🚀

**推荐使用方法1（GitHub网页界面），最简单直接！**