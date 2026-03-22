# 演示准备清单

本文档提供了红德州项目演示前的完整准备清单，确保演示顺利进行。

## 目录

- [演示类型选择](#演示类型选择)
- [环境准备清单](#环境准备清单)
- [配置检查清单](#配置检查清单)
- [服务启动清单](#服务启动清单)
- [功能演示清单](#功能演示清单)
- [常见问题排查](#常见问题排查)

## 演示类型选择

根据您的需求，选择合适的演示类型：

### 1. 运营后台界面演示（推荐入门）

**适用场景**：快速了解项目功能，查看管理界面

**准备工作**：
- ✅ Node.js环境
- ✅ 运营后台代码
- ⚠️ 后端API服务（可选，部分功能需要）

**演示内容**：
- 登录界面
- 用户管理
- 数据统计
- 活动配置
- 系统设置

**预计时间**：10-15分钟

### 2. 完整系统演示（推荐）

**适用场景**：全面了解系统功能，展示完整流程

**准备工作**：
- ✅ 完整的Java环境
- ✅ 所有依赖服务（MySQL、MongoDB、Redis等）
- ✅ 后端服务代码
- ✅ 运营后台代码

**演示内容**：
- 所有运营后台功能
- 后端服务运行状态
- 数据库数据展示
- 实时日志查看

**预计时间**：30-60分钟

### 3. 代码架构演示（技术展示）

**适用场景**：向技术人员展示代码架构和设计

**准备工作**：
- ✅ IDE（IntelliJ IDEA推荐）
- ✅ 代码阅读工具

**演示内容**：
- 项目结构讲解
- 核心代码展示
- 技术架构说明
- 设计模式分析

**预计时间**：20-30分钟

## 环境准备清单

### 基础软件

- [ ] **JDK 1.8+**
  - 下载地址：https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html
  - 验证命令：`java -version`
  - 配置JAVA_HOME环境变量

- [ ] **Maven 3.3+**
  - 下载地址：https://maven.apache.org/download.cgi
  - 验证命令：`mvn -version`
  - 配置MAVEN_HOME环境变量

- [ ] **Node.js 12.x+**
  - 下载地址：https://nodejs.org/
  - 验证命令：`node -v` 和 `npm -v`

- [ ] **Git**（可选）
  - 下载地址：https://git-scm.com/downloads
  - 验证命令：`git --version`

### 数据库服务

- [ ] **MySQL 5.x**
  - 下载地址：https://dev.mysql.com/downloads/mysql/
  - 端口：3306
  - 创建数据库：crazy_poker、allin_vest、yunying
  - 导入SQL脚本：`Server/dz/sql/` 目录下的文件

- [ ] **MongoDB 3.x**
  - 下载地址：https://www.mongodb.com/try/download/community
  - 端口：27017
  - 创建用户：dzpk
  - 创建数据库：crazy_poker

- [ ] **Redis 3.x**
  - 下载地址：https://redis.io/download
  - 端口：6379
  - 设置密码：redis_password

### 中间件服务

- [ ] **Zookeeper 3.x**
  - 下载地址：https://zookeeper.apache.org/releases.html
  - 端口：2181
  - 集群模式需要配置多个节点

- [ ] **RabbitMQ 3.x**
  - 下载地址：https://www.rabbitmq.com/download.html
  - 端口：5672（AMQP）、15672（管理界面）
  - 管理界面：http://localhost:15672
  - 默认用户：guest/guest（建议修改）

- [ ] **ActiveMQ 5.x**
  - 下载地址：https://activemq.apache.org/components/classic/download/
  - 端口：61616
  - 管理界面：http://localhost:8161

### 开发工具

- [ ] **IntelliJ IDEA**（推荐）
  - 下载地址：https://www.jetbrains.com/idea/download/
  - 安装Maven插件
  - 安装Lombok插件

- [ ] **VS Code**（前端开发）
  - 下载地址：https://code.visualstudio.com/
  - 安装Vue.js插件
  - 安装ESLint插件

- [ ] **Navicat** 或 **DBeaver**（数据库管理）
  - 下载地址：https://www.navicat.com/ 或 https://dbeaver.io/
  - 配置MySQL连接
  - 配置MongoDB连接

## 配置检查清单

### 后端配置

- [ ] **数据库配置**
  - [ ] MySQL连接信息正确（IP、端口、用户名、密码）
  - [ ] MongoDB连接信息正确
  - [ ] Redis连接信息正确
  - [ ] 数据库已创建并导入数据

- [ ] **服务配置**
  - [ ] Zookeeper连接地址正确
  - [ ] RabbitMQ连接信息正确
  - [ ] ActiveMQ连接信息正确
  - [ ] 服务端口未被占用

- [ ] **环境配置**
  - [ ] 选择正确的环境（develop/aws_test/aws_online）
  - [ ] 配置文件路径正确
  - [ ] 日志配置正确

### 前端配置

- [ ] **依赖安装**
  - [ ] 运行 `npm install` 成功
  - [ ] 无依赖冲突
  - [ ] 无安全漏洞警告

- [ ] **API配置**
  - [ ] 后端API地址配置正确
  - [ ] 代理配置正确（开发环境）
  - [ ] 环境变量配置正确

- [ ] **构建配置**
  - [ ] vue.config.js配置正确
  - [ ] babel.config.js配置正确
  - [ ] package.json脚本正确

## 服务启动清单

### 基础服务启动顺序

1. [ ] **MySQL**
   ```bash
   systemctl start mysqld
   # 或
   service mysql start
   ```

2. [ ] **MongoDB**
   ```bash
   systemctl start mongod
   # 或
   service mongod start
   ```

3. [ ] **Redis**
   ```bash
   redis-server redis.conf
   # 或
   systemctl start redis
   ```

4. [ ] **Zookeeper**
   ```bash
   /usr/local/zookeeper-3.4.14/bin/zkServer.sh start
   ```

5. [ ] **RabbitMQ**
   ```bash
   systemctl start rabbitmq-server
   # 或
   service rabbitmq-server start
   ```

6. [ ] **ActiveMQ**
   ```bash
   /usr/local/apache-activemq-5.15.9/bin/activemq start
   ```

### 后端服务启动顺序

1. [ ] **Login服务**
   ```bash
   cd Server/dz/game/login
   java -jar target/login-develop-v1.3.5-*.jar
   ```

2. [ ] **Room服务**
   ```bash
   cd Server/dz/game/room
   java -jar target/room-develop-v1.5.2-*.jar
   ```

3. [ ] **其他游戏服务**（可选）
   - [ ] MTT服务
   - [ ] Omaha服务
   - [ ] 其他服务...

4. [ ] **支持服务**（可选）
   - [ ] Pay服务
   - [ ] WebAPI服务
   - [ ] Yunying服务
   - [ ] 其他服务...

### 前端服务启动

1. [ ] **运营后台**
   ```bash
   cd Server/dz/web/mis
   npm run serve
   ```

2. [ ] **访问地址**
   - 运营后台：http://localhost:8080
   - RabbitMQ管理：http://localhost:15672
   - ActiveMQ管理：http://localhost:8161

## 功能演示清单

### 运营后台功能

#### 登录模块
- [ ] 登录界面展示
- [ ] 用户名密码登录
- [ ] 验证码功能（如果有）
- [ ] 记住密码功能
- [ ] 忘记密码功能

#### 用户管理
- [ ] 用户列表展示
- [ ] 用户搜索功能
- [ ] 用户详情查看
- [ ] 用户信息编辑
- [ ] 用户状态管理（启用/禁用）
- [ ] 用户等级管理

#### 数据统计
- [ ] 在线用户统计
- [ ] 注册用户统计
- [ ] 充值金额统计
- [ ] 游戏场次统计
- [ ] 收益统计
- [ ] 图表展示

#### 活动配置
- [ ] 活动列表
- [ ] 活动创建
- [ ] 活动编辑
- [ ] 活动删除
- [ ] 活动规则配置

#### 系统设置
- [ ] 系统参数配置
- [ ] 游戏规则配置
- [ ] 支付配置
- [ ] 消息配置
- [ ] 日志查看

### 后端服务功能

#### 服务监控
- [ ] 服务运行状态
- [ ] 端口监听状态
- [ ] 内存使用情况
- [ ] CPU使用情况
- [ ] 线程数量

#### 日志查看
- [ ] 登录日志
- [ ] 游戏日志
- [ ] 错误日志
- [ ] 性能日志
- [ ] 实时日志查看

#### 数据库检查
- [ ] 数据库连接状态
- [ ] 表数据查看
- [ ] 索引状态
- [ ] 慢查询日志

## 常见问题排查

### 环境问题

#### JDK版本不匹配
**症状**：编译失败，提示不支持的类或方法

**解决方案**：
```bash
# 检查JDK版本
java -version

# 如果不是1.8，需要安装JDK 1.8
# 下载并安装JDK 1.8
# 配置JAVA_HOME环境变量
```

#### Maven依赖下载失败
**症状**：编译时提示依赖找不到

**解决方案**：
```bash
# 清理Maven缓存
mvn clean

# 配置国内镜像源
# 编辑 ~/.m2/settings.xml
# 添加阿里云镜像
```

#### Node.js版本过低
**症状**：npm install失败

**解决方案**：
```bash
# 检查Node.js版本
node -v

# 如果低于12.x，需要升级
# 使用nvm升级
nvm install 14
nvm use 14
```

### 服务问题

#### 端口被占用
**症状**：服务启动失败，提示端口已被使用

**解决方案**：
```bash
# 查看端口占用
netstat -tuln | grep 8500

# 杀死占用进程
kill -9 <PID>

# 或修改服务端口配置
```

#### 数据库连接失败
**症状**：服务启动后无法连接数据库

**解决方案**：
1. 检查数据库服务是否启动
2. 检查连接信息是否正确
3. 检查防火墙设置
4. 检查数据库用户权限

#### 内存不足
**症状**：服务启动后频繁崩溃

**解决方案**：
```bash
# 增加JVM内存
java -Xms1g -Xmx2g -jar target/login-develop-v1.3.5-*.jar

# 或优化代码，减少内存使用
```

### 前端问题

#### npm install失败
**症状**：依赖安装失败

**解决方案**：
```bash
# 清除npm缓存
npm cache clean --force

# 删除node_modules
rm -rf node_modules package-lock.json

# 重新安装
npm install

# 或使用cnpm
npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm install
```

#### API请求失败
**症状**：前端无法调用后端API

**解决方案**：
1. 检查后端服务是否启动
2. 检查API地址配置
3. 检查跨域配置
4. 检查网络连接

#### 样式不生效
**症状**：页面样式显示异常

**解决方案**：
1. 检查SCSS编译是否正确
2. 清除浏览器缓存
3. 检查样式作用域
4. 检查CSS加载顺序

## 演示前检查

### 最终检查清单

- [ ] 所有必需软件已安装
- [ ] 所有依赖服务已启动
- [ ] 后端服务已启动并正常运行
- [ ] 前端服务已启动并可访问
- [ ] 数据库连接正常
- [ ] 配置文件已正确设置
- [ ] 日志文件可正常查看
- [ ] 演示脚本已准备（如有）
- [ ] 演示数据已准备（如有）
- [ ] 备份方案已准备（如有）

### 演示准备时间估算

| 演示类型 | 准备时间 | 演示时间 | 总时间 |
|---------|---------|---------|--------|
| 运营后台界面演示 | 5分钟 | 15分钟 | 20分钟 |
| 完整系统演示 | 30分钟 | 30分钟 | 60分钟 |
| 代码架构演示 | 10分钟 | 30分钟 | 40分钟 |

## 演示注意事项

### 演示前

1. **提前测试**：提前一天进行完整测试
2. **数据准备**：准备演示用的测试数据
3. **环境备份**：备份重要配置和数据
4. **网络检查**：确保网络连接稳定
5. **设备检查**：检查演示设备是否正常

### 演示中

1. **时间控制**：严格控制演示时间
2. **重点突出**：突出核心功能和亮点
3. **节奏把控**：合理控制演示节奏
4. **互动交流**：及时回答观众问题
5. **应急预案**：准备应急处理方案

### 演示后

1. **收集反馈**：收集观众反馈意见
2. **问题记录**：记录演示中发现的问题
3. **总结改进**：总结演示经验，改进下次演示
4. **环境清理**：清理演示环境（如需要）
5. **资料整理**：整理演示相关资料

## 演示支持

如遇到演示相关问题，请联系技术支持团队。

## 附录

### 快速启动脚本

创建 `quick-start.sh`：

```bash
#!/bin/bash

echo "开始启动红德州演示环境..."

# 启动基础服务
echo "启动基础服务..."
systemctl start mysqld
systemctl start mongod
systemctl start redis
/usr/local/zookeeper-3.4.14/bin/zkServer.sh start
systemctl start rabbitmq-server
/usr/local/apache-activemq-5.15.9/bin/activemq start

# 等待服务启动
sleep 10

# 启动后端服务
echo "启动后端服务..."
cd Server/dz/game/login
nohup java -jar target/login-develop-v1.3.5-*.jar > /dev/null 2>&1 &
cd ../../../..

cd Server/dz/game/room
nohup java -jar target/room-develop-v1.5.2-*.jar > /dev/null 2>&1 &
cd ../../../..

# 启动前端服务
echo "启动前端服务..."
cd Server/dz/web/mis
nohup npm run serve > /dev/null 2>&1 &
cd ../../../..

echo "演示环境启动完成！"
echo "运营后台：http://localhost:8080"
echo "RabbitMQ管理：http://localhost:15672"
echo "ActiveMQ管理：http://localhost:8161"
```

### 快速停止脚本

创建 `quick-stop.sh`：

```bash
#!/bin/bash

echo "停止红德州演示环境..."

# 停止前端服务
pkill -f "npm.*serve"

# 停止后端服务
pkill -f "java.*login"
pkill -f "java.*room"

# 停止基础服务
systemctl stop rabbitmq-server
/usr/local/apache-activemq-5.15.9/bin/activemq stop
/usr/local/zookeeper-3.4.14/bin/zkServer.sh stop
systemctl stop redis
systemctl stop mongod
systemctl stop mysqld

echo "演示环境已停止！"
```
