# 后端部署文档

本文档详细说明红德州项目后端的部署流程、环境配置和服务启动。

## 目录

- [环境要求](#环境要求)
- [基础环境搭建](#基础环境搭建)
- [数据库配置](#数据库配置)
- [后端服务配置](#后端服务配置)
- [编译打包](#编译打包)
- [服务启动](#服务启动)
- [常见问题](#常见问题)

## 环境要求

### 必需软件

| 软件 | 版本要求 | 用途 |
|------|----------|------|
| JDK | 1.8+ | Java运行环境 |
| Maven | 3.3+ | 项目构建工具 |
| MySQL | 5.6+ | 主数据库 |
| MongoDB | 3.2+ | 日志和缓存数据库 |
| Redis | 3.0+ | 缓存服务 |
| Zookeeper | 3.4+ | 服务注册与发现 |
| RabbitMQ | 3.6+ | 消息队列 |
| ActiveMQ | 5.11+ | 消息队列 |

### 硬件要求

- CPU: 4核以上
- 内存: 8GB以上
- 硬盘: 100GB以上

## 基础环境搭建

### 1. 安装JDK

```bash
# 下载JDK 1.8
wget https://download.oracle.com/otn-pub/java/jdk/8u281-b09/jdk-8u281-linux-x64.tar.gz

# 解压
tar -zxvf jdk-8u281-linux-x64.tar.gz -C /usr/local/

# 配置环境变量
vi /etc/profile

# 添加以下内容
export JAVA_HOME=/usr/local/jdk1.8.0_281
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH

# 使配置生效
source /etc/profile

# 验证安装
java -version
```

### 2. 安装Maven

```bash
# 下载Maven
wget https://archive.apache.org/dist/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz

# 解压
tar -zxvf apache-maven-3.6.3-bin.tar.gz -C /usr/local/

# 配置环境变量
vi /etc/profile

# 添加以下内容
export MAVEN_HOME=/usr/local/apache-maven-3.6.3
export PATH=$MAVEN_HOME/bin:$PATH

# 使配置生效
source /etc/profile

# 验证安装
mvn -version
```

### 3. 安装MySQL

```bash
# CentOS/RHEL
yum install -y mysql-server

# Ubuntu/Debian
apt-get install -y mysql-server

# 启动MySQL
systemctl start mysqld
systemctl enable mysqld

# 设置root密码
mysql_secure_installation
```

### 4. 安装MongoDB

```bash
# 创建MongoDB仓库
vi /etc/yum.repos.d/mongodb-org-3.2.repo

# 添加以下内容
[mongodb-org-3.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.2.asc

# 安装MongoDB
yum install -y mongodb-org

# 启动MongoDB
systemctl start mongod
systemctl enable mongod
```

### 5. 安装Redis

```bash
# 下载Redis
wget http://download.redis.io/releases/redis-5.0.7.tar.gz

# 解压
tar -zxvf redis-5.0.7.tar.gz
cd redis-5.0.7

# 编译安装
make
make install

# 配置Redis
vi redis.conf

# 修改以下配置
daemonize yes
bind 0.0.0.0
requirepass your_password

# 启动Redis
redis-server redis.conf
```

### 6. 安装Zookeeper

```bash
# 下载Zookeeper
wget https://archive.apache.org/dist/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz

# 解压
tar -zxvf zookeeper-3.4.14.tar.gz -C /usr/local/

# 配置Zookeeper
cd /usr/local/zookeeper-3.4.14/conf
cp zoo_sample.cfg zoo.cfg

# 修改配置
vi zoo.cfg

# 修改数据目录
dataDir=/var/lib/zookeeper

# 创建数据目录
mkdir -p /var/lib/zookeeper

# 启动Zookeeper
/usr/local/zookeeper-3.4.14/bin/zkServer.sh start
```

### 7. 安装RabbitMQ

```bash
# 安装Erlang
yum install -y epel-release
yum install -y erlang

# 下载RabbitMQ
wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.7.15/rabbitmq-server-3.7.15-1.el7.noarch.rpm

# 安装RabbitMQ
rpm -ivh rabbitmq-server-3.7.15-1.el7.noarch.rpm

# 启动RabbitMQ
systemctl start rabbitmq-server
systemctl enable rabbitmq-server

# 启用管理插件
rabbitmq-plugins enable rabbitmq_management

# 创建用户
rabbitmqctl add_user admin admin123
rabbitmqctl set_user_tags admin administrator
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
```

### 8. 安装ActiveMQ

```bash
# 下载ActiveMQ
wget https://archive.apache.org/dist/activemq/5.15.9/apache-activemq-5.15.9-bin.tar.gz

# 解压
tar -zxvf apache-activemq-5.15.9-bin.tar.gz -C /usr/local/

# 启动ActiveMQ
/usr/local/apache-activemq-5.15.9/bin/activemq start
```

## 数据库配置

### 1. MySQL配置

#### 创建数据库

```sql
-- 创建主游戏数据库
CREATE DATABASE IF NOT EXISTS crazy_poker DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 创建All-in数据库
CREATE DATABASE IF NOT EXISTS allin_vest DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 创建运营后台数据库
CREATE DATABASE IF NOT EXISTS yunying DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### 导入数据

```bash
# 进入SQL脚本目录
cd Server/dz/sql

# 导入主游戏数据库
mysql -u root -p crazy_poker < crazy_poker.sql

# 导入All-in数据库
mysql -u root -p allin_vest < allin_vest.sql

# 导入运营后台数据库
mysql -u root -p yunying < yunying20200731.sql
```

#### 创建数据库用户

```sql
-- 创建应用用户
CREATE USER 'dzpk'@'%' IDENTIFIED BY 'dzpk_password';

-- 授予权限
GRANT ALL PRIVILEGES ON crazy_poker.* TO 'dzpk'@'%';
GRANT ALL PRIVILEGES ON allin_vest.* TO 'dzpk'@'%';
GRANT ALL PRIVILEGES ON yunying.* TO 'dzpk'@'%';

-- 刷新权限
FLUSH PRIVILEGES;
```

### 2. MongoDB配置

#### 创建数据库用户

```bash
# 连接MongoDB
mongo

# 切换到admin数据库
use admin

# 创建管理员用户
db.createUser({
  user: "admin",
  pwd: "admin_password",
  roles: [{ role: "userAdminAnyDatabase", db: "admin" }]
})

# 创建应用用户
use crazy_poker
db.createUser({
  user: "dzpk",
  pwd: "dzpk_password",
  roles: [{ role: "readWrite", db: "crazy_poker" }]
})
```

## 后端服务配置

### 配置文件说明

每个服务模块都有以下配置文件：

- `filters/config-develop.properties` - 开发环境配置
- `filters/config-aws_test.properties` - 测试环境配置
- `filters/config-aws_online.properties` - 生产环境配置

### 通用配置项

#### 1. 数据库配置

```properties
# MySQL配置
jdbc.url=jdbc:mysql://localhost:3306/crazy_poker?useUnicode=true&characterEncoding=UTF-8&serverTimezone=UTC
jdbc.username=dzpk
jdbc.password=dzpk_password

# MongoDB配置
mongodb.url=mongodb://dzpk:dzpk_password@localhost:27017/crazy_poker
mongodb.database=crazy_poker

# Redis配置
redis.ip=localhost
redis.port=6379
redis.pwd=redis_password
redis.timeout=5000
```

#### 2. Zookeeper配置

```properties
# Zookeeper连接地址
zk.connectString=localhost:2181

# 会话超时时间（毫秒）
zk.sessionTimeoutMs=60000

# 连接超时时间（毫秒）
zk.connectionTimeoutMs=15000
```

#### 3. RabbitMQ配置

```properties
# RabbitMQ配置
rabbitmq.host=localhost
rabbitmq.user=admin
rabbitmq.password=admin123
rabbitmq.port=5672
```

#### 4. ActiveMQ配置

```properties
# ActiveMQ配置
activemq.url=tcp://localhost:61616
activemq.userName=admin
activemq.password=admin123
```

### 各服务配置

#### 1. Login服务配置

编辑 `Server/dz/game/login/filters/config-develop.properties`：

```properties
# 服务类型
service.type=login

# 服务器编号
service.name=30010001

# Socket监听端口
socket.port=8500
socket.ip=192.168.0.10

# 数据库配置
jdbc.url=jdbc:mysql://localhost:3306/crazy_poker?useUnicode=true&characterEncoding=UTF-8&serverTimezone=UTC
jdbc.username=dzpk
jdbc.password=dzpk_password

# MongoDB配置
mongodb.url=mongodb://dzpk:dzpk_password@localhost:27017/crazy_poker
mongodb.database=crazy_poker

# Zookeeper配置
zk.connectString=localhost:2181
```

#### 2. Room服务配置

编辑 `Server/dz/game/room/filters/config-develop.properties`：

```properties
# 服务类型
service.type=room

# 服务器编号
service.name=30010002

# Socket监听端口
socket.port=8501
socket.ip=192.168.0.10

# Redis配置
redis.ip=localhost
redis.port=6379
redis.pwd=redis_password

# RabbitMQ配置
rabbitmq.host=localhost
rabbitmq.user=admin
rabbitmq.password=admin123
rabbitmq.port=5672

# ActiveMQ配置
activemq.url=tcp://localhost:61616
activemq.userName=admin
activemq.password=admin123
```

#### 3. 其他服务配置

按照相同方式配置其他服务（mtt、omaha、pay等），注意修改：
- 服务编号（service.name）
- 监听端口（socket.port）
- 数据库连接信息

## 编译打包

### 编译单个服务

```bash
# 进入服务目录
cd Server/dz/game/login

# 清理并打包（开发环境）
mvn clean package

# 打包测试环境
mvn clean package -P aws_test

# 打包生产环境
mvn clean package -P aws_online
```

### 批量编译所有服务

创建编译脚本 `build-all.sh`：

```bash
#!/bin/bash

# 服务列表
services=("login" "room" "mtt" "omaha" "aofomaha" "shortCard" "aofroom" "aofShortCard" "pay" "res" "webapi" "webmessage" "yunying" "activemq" "fileupload" "calculator")

# 编译所有服务
for service in "${services[@]}"
do
    echo "编译服务: $service"
    cd Server/dz/game/$service
    mvn clean package -DskipTests
    cd ../../../..
done

echo "所有服务编译完成"
```

运行编译脚本：

```bash
chmod +x build-all.sh
./build-all.sh
```

## 服务启动

### 启动顺序

按照以下顺序启动服务：

1. **基础服务**
   - MySQL
   - MongoDB
   - Redis
   - Zookeeper
   - RabbitMQ
   - ActiveMQ

2. **核心游戏服务**
   - login (登录服务)
   - room (房间服务)

3. **扩展游戏服务**
   - mtt (锦标赛)
   - omaha (奥马哈)
   - aofomaha (All-in奥马哈)
   - shortCard (短牌)
   - aofroom (All-in房间)
   - aofShortCard (All-in短牌)

4. **支持服务**
   - pay (支付)
   - res (资源)
   - webapi (Web API)
   - webmessage (消息)
   - yunying (运营后台)
   - activemq (消息队列)
   - fileupload (文件上传)
   - calculator (计算器)

### 启动单个服务

```bash
# 进入服务目录
cd Server/dz/game/login

# 启动服务
java -jar target/login-develop-v1.3.5-*.jar

# 或者使用nohup后台运行
nohup java -jar target/login-develop-v1.3.5-*.jar > /dev/null 2>&1 &

# 查看日志
tail -f logs/login.log
```

### 批量启动服务

创建启动脚本 `start-all.sh`：

```bash
#!/bin/bash

# 服务列表和端口
declare -A services=(
    ["login"]="8500"
    ["room"]="8501"
    ["mtt"]="8502"
    ["omaha"]="8503"
    ["pay"]="8600"
    ["yunying"]="8663"
    ["webapi"]="8700"
)

# 启动服务
for service in "${!services[@]}"
do
    port=${services[$service]}
    echo "启动服务: $service (端口: $port)"

    cd Server/dz/game/$service
    nohup java -jar target/$service-develop-v*.jar > /dev/null 2>&1 &
    cd ../../../..

    # 等待服务启动
    sleep 5
done

echo "所有服务启动完成"
```

运行启动脚本：

```bash
chmod +x start-all.sh
./start-all.sh
```

### 停止服务

```bash
# 查找Java进程
jps -l

# 或者查找特定服务
ps aux | grep login

# 停止服务
kill -9 <PID>

# 批量停止所有Java服务
pkill -f "java.*jar"
```

### 服务健康检查

```bash
# 检查端口是否监听
netstat -tuln | grep -E '8500|8501|8502|8503'

# 检查服务进程
jps -l

# 查看服务日志
tail -f Server/dz/game/login/logs/login.log
```

## 常见问题

### 1. 端口被占用

```bash
# 查看端口占用
netstat -tuln | grep 8500

# 杀死占用进程
kill -9 <PID>
```

### 2. 数据库连接失败

检查：
- 数据库服务是否启动
- 连接信息是否正确
- 防火墙是否开放端口
- 用户权限是否正确

### 3. 内存不足

```bash
# 增加JVM内存
java -Xms512m -Xmx1024m -jar target/login-develop-v1.3.5-*.jar
```

### 4. Zookeeper连接失败

检查：
- Zookeeper服务是否启动
- 连接地址是否正确
- 网络是否通畅

### 5. Redis连接超时

检查：
- Redis服务是否启动
- 密码是否正确
- 防火墙设置

## 日志管理

### 日志位置

各服务的日志文件位于：

```
Server/dz/game/<service>/logs/
├── login.log
├── room.log
└── ...
```

### 日志配置

日志配置文件为 `log4j2.xml`，位于各服务根目录。

### 查看日志

```bash
# 实时查看日志
tail -f Server/dz/game/login/logs/login.log

# 查看最近100行
tail -n 100 Server/dz/game/login/logs/login.log

# 搜索错误日志
grep "ERROR" Server/dz/game/login/logs/login.log
```

## 监控和维护

### 服务监控

```bash
# 查看所有Java进程
jps -l

# 查看内存使用
jmap -heap <PID>

# 查看线程状态
jstack <PID>
```

### 定期维护

- 定期备份数据库
- 清理日志文件
- 监控系统资源
- 更新安全补丁

## 性能优化

### JVM参数优化

```bash
java -Xms1g -Xmx2g -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -jar target/login-develop-v1.3.5-*.jar
```

### 数据库优化

- 添加适当的索引
- 优化SQL查询
- 配置连接池
- 定期维护表

## 安全建议

1. 修改所有默认密码
2. 配置防火墙规则
3. 限制数据库访问
4. 定期备份数据
5. 监控异常访问
6. 及时更新补丁

## 技术支持

如遇到部署问题，请联系技术支持团队。
