# 官方网站搭建指南

## 📋 概述

本指南将帮助您搭建红德州项目的官方网站，用于展示项目、吸引客户、提供联系方式。

**网站目标**：
- 展示项目的完整性和专业性
- 提供详细的项目介绍
- 引导客户联系购买
- 提供技术文档下载

**网站规格**：
- 响应式设计：支持PC、平板、手机
- 页面数量：5-8页
- 加载速度：< 3秒
- SEO优化：支持搜索引擎优化

---

## 🌐 网站结构

### 页面结构

```
reddezhou.com/
├── index.html              # 首页
├── about.html              # 关于我们
├── features.html           # 功能介绍
├── technology.html         # 技术架构
├── services.html           # 技术服务
├── contact.html            # 联系我们
├── docs/                   # 文档页面
│   ├── technical-architecture.html
│   ├── client-setup.html
│   └── deployment.html
├── assets/                 # 静态资源
│   ├── css/
│   │   ├── style.css
│   │   └── responsive.css
│   ├── js/
│   │   ├── main.js
│   │   └── analytics.js
│   ├── images/
│   │   ├── logo.png
│   │   ├── hero-bg.jpg
│   │   ├── screenshot-1.png
│   │   ├── screenshot-2.png
│   │   └── ...
│   └── fonts/
│       └── ...
└── sitemap.xml             # 网站地图
```

---

## 🏠 首页（index.html）

### 页面结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="红德州 - 完整的在线德州扑克游戏平台，采用微服务架构，包含完整的服务端、运营后台和Unity游戏客户端">
    <meta name="keywords" content="德州扑克,在线游戏,游戏平台,Java,Netty,Unity,Vue.js">
    <title>红德州 - 完整的在线德州扑克游戏平台</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/responsive.css">
</head>
<body>
    <!-- 导航栏 -->
    <nav class="navbar">
        <div class="container">
            <div class="logo">
                <a href="index.html">
                    <img src="assets/images/logo.png" alt="红德州Logo">
                </a>
            </div>
            <ul class="nav-menu">
                <li><a href="index.html">首页</a></li>
                <li><a href="about.html">关于我们</a></li>
                <li><a href="features.html">功能介绍</a></li>
                <li><a href="technology.html">技术架构</a></li>
                <li><a href="services.html">技术服务</a></li>
                <li><a href="contact.html" class="btn-contact">联系我们</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero区域 -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1>红德州</h1>
                <h2>完整的在线德州扑克游戏平台</h2>
                <p>采用现代化微服务架构，包含完整的服务端、运营后台和Unity游戏客户端</p>
                <div class="hero-buttons">
                    <a href="contact.html" class="btn btn-primary">联系我们</a>
                    <a href="features.html" class="btn btn-secondary">了解更多</a>
                </div>
            </div>
        </div>
    </section>

    <!-- 核心功能 -->
    <section class="features">
        <div class="container">
            <h2 class="section-title">核心功能</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🎮</div>
                    <h3>多种扑克游戏</h3>
                    <p>德州扑克、奥马哈、短牌等多种扑克游戏</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🏆</div>
                    <h3>锦标赛系统</h3>
                    <p>支持MTT、SNG等锦标赛模式</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">👥</div>
                    <h3>俱乐部系统</h3>
                    <p>创建和管理扑克俱乐部</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💳</div>
                    <h3>支付系统</h3>
                    <p>完整的充值、提现、资金管理</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h3>运营后台</h3>
                    <p>用户管理、数据统计、活动配置</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💬</div>
                    <h3>社交功能</h3>
                    <p>好友、聊天、礼物等社交功能</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 技术架构 -->
    <section class="technology">
        <div class="container">
            <h2 class="section-title">技术架构</h2>
            <div class="technology-content">
                <div class="tech-item">
                    <h3>服务端</h3>
                    <p>Java 8 + Netty + Spring Boot</p>
                </div>
                <div class="tech-item">
                    <h3>运营后台</h3>
                    <p>Vue.js + ElementUI + ECharts</p>
                </div>
                <div class="tech-item">
                    <h3>客户端</h3>
                    <p>Unity 2019 + C# + ET Framework</p>
                </div>
                <div class="tech-item">
                    <h3>数据库</h3>
                    <p>MySQL + MongoDB + Redis</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 项目优势 -->
    <section class="advantages">
        <div class="container">
            <h2 class="section-title">项目优势</h2>
            <div class="advantages-grid">
                <div class="advantage-card">
                    <h3>✅ 完整的前后端匹配</h3>
                    <p>服务端、运营后台、Unity客户端完全匹配，无需额外开发</p>
                </div>
                <div class="advantage-card">
                    <h3>✅ 现代化技术栈</h3>
                    <p>Java 8 + Netty + Vue.js + Unity，采用最新的技术栈</p>
                </div>
                <div class="advantage-card">
                    <h3>✅ 快速部署上线</h3>
                    <p>5-10个工作日即可部署完成，快速抢占市场</p>
                </div>
                <div class="advantage-card">
                    <h3>✅ 专业的技术支持</h3>
                    <p>7x24小时技术支持，2小时内响应</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 服务套餐 -->
    <section class="services">
        <div class="container">
            <h2 class="section-title">服务套餐</h2>
            <div class="services-grid">
                <div class="service-card">
                    <h3>套餐A</h3>
                    <div class="price">5-20万</div>
                    <p>基础部署服务</p>
                    <ul>
                        <li>环境搭建</li>
                        <li>项目部署</li>
                        <li>数据库初始化</li>
                        <li>基础配置</li>
                        <li>测试验证</li>
                    </ul>
                    <a href="contact.html" class="btn btn-primary">联系我们</a>
                </div>
                <div class="service-card featured">
                    <div class="badge">推荐</div>
                    <h3>套餐B</h3>
                    <div class="price">50-200万</div>
                    <p>高级定制服务</p>
                    <ul>
                        <li>功能定制</li>
                        <li>界面定制</li>
                        <li>协议调整</li>
                        <li>性能优化</li>
                        <li>安全增强</li>
                    </ul>
                    <a href="contact.html" class="btn btn-primary">联系我们</a>
                </div>
                <div class="service-card">
                    <h3>套餐C</h3>
                    <div class="price">200-500万</div>
                    <p>企业级服务</p>
                    <ul>
                        <li>完整定制</li>
                        <li>技术培训</li>
                        <li>长期支持</li>
                        <li>咨询服务</li>
                        <li>专属团队</li>
                    </ul>
                    <a href="contact.html" class="btn btn-primary">联系我们</a>
                </div>
            </div>
        </div>
    </section>

    <!-- 演示视频 -->
    <section class="demo-video">
        <div class="container">
            <h2 class="section-title">演示视频</h2>
            <div class="video-container">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        </div>
    </section>

    <!-- CTA区域 -->
    <section class="cta">
        <div class="container">
            <h2>准备好开始了吗？</h2>
            <p>立即联系我们，获取完整的技术方案和报价</p>
            <a href="contact.html" class="btn btn-primary btn-large">立即联系我们</a>
        </div>
    </section>

    <!-- 页脚 -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>红德州</h3>
                    <p>完整的在线德州扑克游戏平台</p>
                </div>
                <div class="footer-section">
                    <h3>快速链接</h3>
                    <ul>
                        <li><a href="about.html">关于我们</a></li>
                        <li><a href="features.html">功能介绍</a></li>
                        <li><a href="technology.html">技术架构</a></li>
                        <li><a href="services.html">技术服务</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>联系我们</h3>
                    <ul>
                        <li>邮箱：business@reddezhou.com</li>
                        <li>电话：+86-XXX-XXXX-XXXX</li>
                        <li>微信：reddezhou</li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>关注我们</h3>
                    <div class="social-links">
                        <a href="https://www.linkedin.com/company/reddezhou" target="_blank">LinkedIn</a>
                        <a href="https://www.facebook.com/reddezhou" target="_blank">Facebook</a>
                        <a href="https://weibo.com/reddezhou" target="_blank">微博</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 红德州技术团队. 保留所有权利.</p>
            </div>
        </div>
    </footer>

    <script src="assets/js/main.js"></script>
</body>
</html>
```

---

## 🎨 CSS样式（assets/css/style.css）

```css
/* 全局样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Microsoft YaHei', Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* 导航栏 */
.navbar {
    background: #fff;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
}

.logo img {
    height: 40px;
}

.nav-menu {
    display: flex;
    list-style: none;
}

.nav-menu li {
    margin-left: 30px;
}

.nav-menu a {
    text-decoration: none;
    color: #333;
    font-weight: 500;
    transition: color 0.3s;
}

.nav-menu a:hover {
    color: #1E88E5;
}

.btn-contact {
    background: #1E88E5;
    color: #fff !important;
    padding: 8px 20px;
    border-radius: 5px;
}

.btn-contact:hover {
    background: #1565C0;
}

/* Hero区域 */
.hero {
    background: linear-gradient(135deg, #1E88E5 0%, #42A5F5 100%);
    color: #fff;
    padding: 200px 0 100px;
    text-align: center;
}

.hero h1 {
    font-size: 60px;
    margin-bottom: 20px;
}

.hero h2 {
    font-size: 30px;
    margin-bottom: 20px;
    font-weight: 400;
}

.hero p {
    font-size: 18px;
    margin-bottom: 40px;
    opacity: 0.9;
}

.hero-buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
}

.btn {
    display: inline-block;
    padding: 12px 30px;
    text-decoration: none;
    border-radius: 5px;
    font-weight: 500;
    transition: all 0.3s;
}

.btn-primary {
    background: #fff;
    color: #1E88E5;
}

.btn-primary:hover {
    background: #f5f5f5;
    transform: translateY(-2px);
}

.btn-secondary {
    background: transparent;
    color: #fff;
    border: 2px solid #fff;
}

.btn-secondary:hover {
    background: #fff;
    color: #1E88E5;
}

.btn-large {
    padding: 15px 40px;
    font-size: 18px;
}

/* 通用样式 */
section {
    padding: 80px 0;
}

.section-title {
    text-align: center;
    font-size: 36px;
    margin-bottom: 60px;
    color: #1E88E5;
}

/* 核心功能 */
.features {
    background: #f9f9f9;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

.feature-card {
    background: #fff;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s;
}

.feature-card:hover {
    transform: translateY(-10px);
}

.feature-icon {
    font-size: 48px;
    margin-bottom: 20px;
}

.feature-card h3 {
    font-size: 24px;
    margin-bottom: 15px;
    color: #1E88E5;
}

.feature-card p {
    color: #666;
}

/* 技术架构 */
.technology {
    background: #fff;
}

.technology-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
}

.tech-item {
    text-align: center;
    padding: 30px;
    background: #f9f9f9;
    border-radius: 10px;
}

.tech-item h3 {
    font-size: 20px;
    margin-bottom: 10px;
    color: #1E88E5;
}

.tech-item p {
    color: #666;
}

/* 项目优势 */
.advantages {
    background: #f9f9f9;
}

.advantages-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 30px;
}

.advantage-card {
    background: #fff;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.advantage-card h3 {
    font-size: 20px;
    margin-bottom: 15px;
    color: #1E88E5;
}

.advantage-card p {
    color: #666;
}

/* 服务套餐 */
.services {
    background: #fff;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

.service-card {
    background: #f9f9f9;
    padding: 40px;
    border-radius: 10px;
    text-align: center;
    transition: transform 0.3s;
    position: relative;
}

.service-card:hover {
    transform: translateY(-10px);
}

.service-card.featured {
    background: #1E88E5;
    color: #fff;
}

.service-card.featured h3,
.service-card.featured .price,
.service-card.featured p,
.service-card.featured li {
    color: #fff;
}

.service-card.featured .btn-primary {
    background: #fff;
    color: #1E88E5;
}

.badge {
    position: absolute;
    top: -15px;
    right: 20px;
    background: #FFD700;
    color: #333;
    padding: 5px 15px;
    border-radius: 20px;
    font-weight: 500;
}

.service-card h3 {
    font-size: 24px;
    margin-bottom: 15px;
    color: #1E88E5;
}

.price {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 15px;
    color: #1E88E5;
}

.service-card p {
    margin-bottom: 20px;
    color: #666;
}

.service-card ul {
    list-style: none;
    margin-bottom: 30px;
    text-align: left;
}

.service-card li {
    padding: 10px 0;
    border-bottom: 1px solid #ddd;
    color: #666;
}

.service-card li:last-child {
    border-bottom: none;
}

/* 演示视频 */
.demo-video {
    background: #f9f9f9;
    text-align: center;
}

.video-container {
    max-width: 800px;
    margin: 0 auto;
    position: relative;
    padding-bottom: 56.25%;
    height: 0;
    overflow: hidden;
}

.video-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 10px;
}

/* CTA区域 */
.cta {
    background: linear-gradient(135deg, #1E88E5 0%, #42A5F5 100%);
    color: #fff;
    text-align: center;
    padding: 100px 0;
}

.cta h2 {
    font-size: 36px;
    margin-bottom: 20px;
}

.cta p {
    font-size: 18px;
    margin-bottom: 40px;
    opacity: 0.9;
}

.cta .btn-primary {
    background: #fff;
    color: #1E88E5;
}

/* 页脚 */
.footer {
    background: #333;
    color: #fff;
    padding: 60px 0 20px;
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 40px;
    margin-bottom: 40px;
}

.footer-section h3 {
    font-size: 20px;
    margin-bottom: 20px;
    color: #1E88E5;
}

.footer-section ul {
    list-style: none;
}

.footer-section li {
    margin-bottom: 10px;
}

.footer-section a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s;
}

.footer-section a:hover {
    color: #1E88E5;
}

.social-links {
    display: flex;
    gap: 15px;
}

.social-links a {
    color: #fff;
    text-decoration: none;
}

.footer-bottom {
    text-align: center;
    padding-top: 20px;
    border-top: 1px solid #444;
    color: #999;
}
```

---

## 📱 响应式CSS（assets/css/responsive.css）

```css
/* 平板设备 */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 40px;
    }

    .hero h2 {
        font-size: 24px;
    }

    .hero-buttons {
        flex-direction: column;
        align-items: center;
    }

    .nav-menu {
        display: none;
    }

    .features-grid,
    .advantages-grid,
    .services-grid {
        grid-template-columns: 1fr;
    }

    .footer-content {
        grid-template-columns: 1fr;
    }
}

/* 手机设备 */
@media (max-width: 480px) {
    .hero h1 {
        font-size: 32px;
    }

    .hero h2 {
        font-size: 20px;
    }

    .hero p {
        font-size: 16px;
    }

    .section-title {
        font-size: 28px;
    }

    .feature-card,
    .advantage-card,
    .service-card {
        padding: 30px 20px;
    }
}
```

---

## 📝 JavaScript（assets/js/main.js）

```javascript
// 导航栏滚动效果
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = '#fff';
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    }
});

// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// 移动端菜单
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', function() {
        navMenu.classList.toggle('active');
    });
}
```

---

## 🔍 SEO优化

### meta标签

```html
<meta name="description" content="红德州 - 完整的在线德州扑克游戏平台，采用微服务架构，包含完整的服务端、运营后台和Unity游戏客户端">
<meta name="keywords" content="德州扑克,在线游戏,游戏平台,Java,Netty,Unity,Vue.js,微服务,游戏开发">
<meta name="author" content="红德州技术团队">
<meta name="robots" content="index, follow">
```

### Open Graph标签

```html
<meta property="og:title" content="红德州 - 完整的在线德州扑克游戏平台">
<meta property="og:description" content="红德州是一个功能完整的在线德州扑克游戏平台，采用微服务架构，包含完整的服务端、运营后台和Unity游戏客户端">
<meta property="og:image" content="https://www.reddezhou.com/assets/images/og-image.jpg">
<meta property="og:url" content="https://www.reddezhou.com">
<meta property="og:type" content="website">
```

### 网站地图（sitemap.xml）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://www.reddezhou.com/</loc>
        <lastmod>2026-03-22</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://www.reddezhou.com/about.html</loc>
        <lastmod>2026-03-22</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.reddezhou.com/features.html</loc>
        <lastmod>2026-03-22</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.reddezhou.com/technology.html</loc>
        <lastmod>2026-03-22</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.reddezhou.com/services.html</loc>
        <lastmod>2026-03-22</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.reddezhou.com/contact.html</loc>
        <lastmod>2026-03-22</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
```

---

## 🚀 部署步骤

### 1. 购买域名
- 访问域名注册商（如阿里云、腾讯云、GoDaddy）
- 注册域名：reddezhou.com 或类似域名
- 配置DNS解析

### 2. 购买服务器
- 访问云服务商（如阿里云、腾讯云、AWS）
- 购买云服务器（推荐配置：2核4G）
- 安装Nginx

### 3. 上传网站文件
- 使用FTP或SCP上传网站文件到服务器
- 文件路径：/var/www/html/

### 4. 配置Nginx
```nginx
server {
    listen 80;
    server_name reddezhou.com www.reddezhou.com;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### 5. 配置SSL证书
- 使用Let's Encrypt免费SSL证书
- 或购买商业SSL证书

### 6. 测试网站
- 访问网站，确认网站正常运行
- 检查所有页面和链接
- 检查移动端显示

---

## ✅ 检查清单

### 内容检查
- [ ] 首页内容完整
- [ ] 关于我们页面完整
- [ ] 功能介绍页面完整
- [ ] 技术架构页面完整
- [ ] 技术服务页面完整
- [ ] 联系我们页面完整

### 设计检查
- [ ] 页面设计美观
- [ ] 响应式设计正常
- [ ] 颜色方案统一
- [ ] 字体方案统一
- [ ] 图标风格统一

### 技术检查
- [ ] HTML代码规范
- [ ] CSS代码规范
- [ ] JavaScript代码规范
- [ ] SEO优化完成
- [ ] 网站速度优化

### 部署检查
- [ ] 域名已购买
- [ ] 服务器已购买
- [ ] 网站文件已上传
- [ ] Nginx已配置
- [ ] SSL证书已配置
- [ ] 网站正常运行

---

**更新日期**：2026-03-22
**版本**：v1.0.0
