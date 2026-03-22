# 前端部署文档

本文档详细说明红德州项目前端的部署流程、环境配置和构建运行。

## 目录

- [环境要求](#环境要求)
- [项目结构](#项目结构)
- [开发环境搭建](#开发环境搭建)
- [配置说明](#配置说明)
- [开发运行](#开发运行)
- [生产构建](#生产构建)
- [部署上线](#部署上线)
- [常见问题](#常见问题)

## 环境要求

### 必需软件

| 软件 | 版本要求 | 用途 |
|------|----------|------|
| Node.js | 12.x+ | JavaScript运行环境 |
| npm | 6.x+ | 包管理器 |
| Git | 2.x+ | 版本控制（可选） |

### 推荐软件

| 软件 | 版本要求 | 用途 |
|------|----------|------|
| VS Code | 最新版 | 代码编辑器 |
| Chrome | 最新版 | 浏览器调试 |

## 项目结构

### 前端项目列表

```
Server/dz/web/
├── mis/                # 后台管理系统
├── paipu/              # 牌谱系统
├── webdownload/        # 下载站
├── staticweb/          # 静态网站
└── osm/                # 地图服务
```

### MIS后台管理系统结构

```
mis/
├── public/             # 公共资源
│   ├── favicon.ico
│   └── index.html
├── src/                # 源代码
│   ├── api/            # API接口
│   ├── assets/         # 静态资源
│   ├── components/     # 组件
│   ├── directive/      # 指令
│   ├── plugins/        # 插件
│   ├── router/         # 路由配置
│   ├── store/          # 状态管理
│   ├── utils/          # 工具函数
│   ├── views/          # 页面视图
│   ├── App.vue         # 根组件
│   ├── main.js         # 入口文件
│   └── menu.js         # 菜单配置
├── package.json       # 依赖配置
├── vue.config.js      # Vue配置
└── babel.config.js    # Babel配置
```

## 开发环境搭建

### 1. 安装Node.js

#### Windows

1. 访问 [Node.js官网](https://nodejs.org/)
2. 下载LTS版本安装包
3. 运行安装程序，按提示完成安装
4. 验证安装：

```bash
node -v
npm -v
```

#### Linux

```bash
# 使用nvm安装Node.js（推荐）
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash

# 重新加载配置
source ~/.bashrc

# 安装Node.js 14.x
nvm install 14

# 使用Node.js 14.x
nvm use 14

# 验证安装
node -v
npm -v
```

#### macOS

```bash
# 使用Homebrew安装
brew install node

# 验证安装
node -v
npm -v
```

### 2. 配置npm镜像（可选）

```bash
# 使用淘宝镜像
npm config set registry https://registry.npm.taobao.org

# 验证配置
npm config get registry
```

### 3. 安装Vue CLI

```bash
# 全局安装Vue CLI
npm install -g @vue/cli

# 验证安装
vue --version
```

## 配置说明

### 1. 环境变量配置

项目支持三种环境配置：

- **dev** - 开发环境
- **uat** - 测试环境
- **production** - 生产环境

#### 创建环境配置文件

在项目根目录创建以下文件：

**`.env.dev`** (开发环境)

```bash
NODE_ENV=development
BASE_URL=http://localhost:8663/api
```

**`.env.uat`** (测试环境)

```bash
NODE_ENV=production
BASE_URL=http://8.210.96.200:8663/api
```

**`.env.production`** (生产环境)

```bash
NODE_ENV=production
BASE_URL=http://your-domain.com/api
```

### 2. API配置

编辑 `src/api/request.js`：

```javascript
// 根据环境配置API地址
let baseURL = '/api';
let env = process.env;

switch (env.NODE_ENV) {
    case 'dev':
        baseURL = 'http://localhost:8663/api';
        break;
    case 'uat':
        baseURL = 'http://8.210.96.200:8663/api';
        break;
    case 'production':
        baseURL = 'http://your-domain.com/api';
        break;
    default:
        break;
}

axios.defaults.baseURL = baseURL;
```

### 3. Vue配置

编辑 `vue.config.js`：

```javascript
module.exports = {
    // 基本路径
    publicPath: './',

    // 输出文件目录
    outputDir: 'dist',

    // 静态资源目录
    assetsDir: 'static',

    // 开发服务器配置
    devServer: {
        port: 8080,
        open: true,
        proxy: {
            '/api': {
                target: 'http://localhost:8663',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '/api'
                }
            }
        }
    },

    // 生产环境配置
    productionSourceMap: false,

    // CSS配置
    css: {
        loaderOptions: {
            sass: {
                data: `@import "@/assets/scss/global.scss";`
            }
        }
    }
}
```

## 开发运行

### 1. 安装依赖

```bash
# 进入项目目录
cd Server/dz/web/mis

# 安装依赖
npm install

# 或者使用cnpm（如果配置了淘宝镜像）
cnpm install
```

### 2. 启动开发服务器

```bash
# 启动开发环境
npm run serve

# 访问 http://localhost:8080
```

开发服务器会自动打开浏览器，并支持热重载。

### 3. 其他开发命令

```bash
# 代码检查
npm run lint

# 代码格式化
npm run format
```

## 生产构建

### 1. 构建不同环境

```bash
# 构建开发环境
npm run build-dev

# 构建测试环境
npm run build-uat

# 构建生产环境
npm run build
```

### 2. 构建产物

构建完成后，会在项目根目录生成 `dist` 目录：

```
dist/
├── index.html          # 入口HTML文件
└── static/             # 静态资源
    ├── css/             # CSS文件
    ├── js/              # JS文件
    ├── img/             # 图片
    └── fonts/           # 字体
```

### 3. 构建优化

#### 代码分割

在 `vue.config.js` 中配置：

```javascript
module.exports = {
    configureWebpack: {
        optimization: {
            splitChunks: {
                chunks: 'all',
                cacheGroups: {
                    libs: {
                        name: 'chunk-libs',
                        test: /[\\/]node_modules[\\/]/,
                        priority: 10,
                        chunks: 'initial'
                    },
                    elementUI: {
                        name: 'chunk-elementUI',
                        priority: 20,
                        test: /[\\/]node_modules[\\/]_?element-ui(.*)/
                    }
                }
            }
        }
    }
}
```

#### Gzip压缩

安装插件：

```bash
npm install compression-webpack-plugin --save-dev
```

配置：

```javascript
const CompressionWebpackPlugin = require('compression-webpack-plugin')

module.exports = {
    configureWebpack: {
        plugins: [
            new CompressionWebpackPlugin({
                algorithm: 'gzip',
                test: /\.(js|css|html|svg)$/,
                threshold: 10240,
                minRatio: 0.8
            })
        ]
    }
}
```

## 部署上线

### 1. Nginx部署

#### 安装Nginx

```bash
# CentOS/RHEL
yum install -y nginx

# Ubuntu/Debian
apt-get install -y nginx
```

#### 配置Nginx

创建配置文件 `/etc/nginx/conf.d/reddezhou.conf`：

```nginx
server {
    listen 80;
    server_name your-domain.com;

    # 前端静态文件
    location / {
        root /var/www/reddezhou/mis/dist;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # API代理
    location /api/ {
        proxy_pass http://localhost:8663/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # 静态资源缓存
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

#### 部署文件

```bash
# 创建部署目录
mkdir -p /var/www/reddezhou/mis

# 复制构建产物
cp -r dist/* /var/www/reddezhou/mis/

# 设置权限
chown -R nginx:nginx /var/www/reddezhou/mis
chmod -R 755 /var/www/reddezhou/mis
```

#### 启动Nginx

```bash
# 测试配置
nginx -t

# 启动Nginx
systemctl start nginx
systemctl enable nginx
```

### 2. Docker部署

#### 创建Dockerfile

```dockerfile
# 构建阶段
FROM node:14-alpine as build-stage

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# 生产阶段
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

#### 构建镜像

```bash
docker build -t reddezhou-mis:latest .
```

#### 运行容器

```bash
docker run -d \
  --name reddezhou-mis \
  -p 80:80 \
  reddezhou-mis:latest
```

### 3. CI/CD部署

#### GitHub Actions配置

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'

    - name: Install dependencies
      run: npm install

    - name: Build
      run: npm run build

    - name: Deploy to server
      uses: easingthemes/ssh-deploy@v2.1.5
      env:
        SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
        REMOTE_HOST: ${{ secrets.REMOTE_HOST }}
        REMOTE_USER: ${{ secrets.REMOTE_USER }}
        TARGET: /var/www/reddezhou/mis
```

## 常见问题

### 1. npm install失败

```bash
# 清除缓存
npm cache clean --force

# 删除node_modules和package-lock.json
rm -rf node_modules package-lock.json

# 重新安装
npm install
```

### 2. 端口被占用

```bash
# 查看端口占用
netstat -ano | findstr :8080

# 或者修改vue.config.js中的端口
devServer: {
    port: 8081
}
```

### 3. API请求失败

检查：
- 后端服务是否启动
- API地址配置是否正确
- 代理配置是否正确
- 跨域问题是否解决

### 4. 构建失败

```bash
# 清除构建缓存
rm -rf dist

# 重新构建
npm run build
```

### 5. 样式不生效

检查：
- SCSS编译是否正确
- 样式作用域是否正确
- 浏览器缓存是否清除

### 6. 路由跳转404

在Nginx配置中添加：

```nginx
location / {
    try_files $uri $uri/ /index.html;
}
```

## 性能优化

### 1. 代码分割

使用动态导入：

```javascript
const component = () => import('@/views/Home.vue')
```

### 2. 懒加载

路由懒加载：

```javascript
{
    path: '/home',
    component: () => import('@/views/home/index.vue')
}
```

### 3. 图片优化

- 使用WebP格式
- 压缩图片大小
- 使用CDN加速

### 4. 缓存策略

```nginx
# 静态资源长期缓存
location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}

# HTML文件不缓存
location ~* \.html$ {
    expires -1;
    add_header Cache-Control "no-cache, no-store, must-revalidate";
}
```

## 安全建议

1. **HTTPS部署**
   - 使用SSL证书
   - 强制HTTPS重定向

2. **XSS防护**
   - 输入验证
   - 输出编码
   - CSP策略

3. **CSRF防护**
   - 使用Token验证
   - SameSite Cookie

4. **敏感信息保护**
   - 不在前端存储敏感信息
   - 使用HttpOnly Cookie

## 监控和日志

### 1. 错误监控

集成Sentry：

```bash
npm install @sentry/vue
```

```javascript
import * as Sentry from "@sentry/vue";
import { Integrations } from "@sentry/tracing";

Sentry.init({
  Vue,
  dsn: "your-dsn",
  integrations: [new Integrations.BrowserTracing()],
  tracesSampleRate: 1.0,
});
```

### 2. 性能监控

使用Google Analytics：

```javascript
// main.js
import VueAnalytics from 'vue-analytics'

Vue.use(VueAnalytics, {
  id: 'UA-XXXXX-Y'
})
```

## 技术支持

如遇到部署问题，请联系技术支持团队。
