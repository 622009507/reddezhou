# 红德州 - Unity客户端配置指南

## 目录

1. [环境准备](#环境准备)
2. [项目导入](#项目导入)
3. [配置说明](#配置说明)
4. [编译打包](#编译打包)
5. [常见问题](#常见问题)

## 环境准备

### 系统要求

#### Windows系统
- 操作系统：Windows 7 SP1及以上
- Unity版本：2019.4.x或更高
- JDK：1.8及以上
- Android SDK：API Level 21及以上
- Xcode：10.0及以上（仅iOS开发需要）

#### macOS系统
- 操作系统：macOS 10.13及以上
- Unity版本：2019.4.x或更高
- JDK：1.8及以上
- Xcode：10.0及以上

### 软件安装

#### 1. 安装Unity Hub

下载并安装Unity Hub：
- 官网：https://unity.com/download
- 选择对应操作系统的版本

#### 2. 安装Unity编辑器

通过Unity Hub安装Unity编辑器：
- 版本：2019.4.x
- 模块：
  - Android Build Support（Android开发）
  - iOS Build Support（iOS开发）
  - Windows Build Support（Windows开发）
  - Mac Build Support（Mac开发）

#### 3. 安装JDK

下载并安装JDK 1.8：
- 官网：https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html
- 配置JAVA_HOME环境变量

#### 4. 安装Android SDK（仅Android开发）

通过Android Studio安装Android SDK：
- 下载Android Studio：https://developer.android.com/studio
- 安装Android SDK
- 配置ANDROID_HOME环境变量

#### 5. 安装Xcode（仅iOS开发）

从Mac App Store安装Xcode：
- 版本：10.0及以上
- 安装Command Line Tools

## 项目导入

### 1. 导入Unity项目

#### 方法一：通过Unity Hub导入

1. 打开Unity Hub
2. 点击"Add"按钮
3. 选择项目目录：`redPoker/redPoker_139.159.248.138`
4. 等待项目导入完成

#### 方法二：通过Unity编辑器导入

1. 打开Unity编辑器
2. 点击"Open"
3. 选择项目目录：`redPoker/redPoker_139.159.248.138`
4. 等待项目导入完成

### 2. 项目结构说明

```
redPoker_139.159.248.138/
├── Assets/                 # Unity资源目录
│   ├── Hotfix/            # 热更新代码
│   │   ├── CrazyPoker/    # 游戏逻辑
│   │   │   ├── Config/    # 配置文件
│   │   │   ├── Module/    # 功能模块
│   │   │   └── Util/      # 工具类
│   │   └── UI/            # UI界面
│   ├── Model/             # 框架代码
│   ├── Res/               # 游戏资源
│   ├── Scenes/            # 游戏场景
│   └── ThirdParty/        # 第三方库
├── Packages/              # Unity包管理
├── ProjectSettings/       # 项目配置
└── UserSettings/          # 用户配置
```

### 3. 项目依赖检查

检查以下依赖是否完整：

#### 必需的包
- TextMeshPro
- Addressables
- DOTween
- BestHTTP

#### 可选的包
- UniRx
- protobuf-net

如果缺少依赖包，通过Unity Package Manager安装。

## 配置说明

### 1. 服务器配置

#### 修改服务器IP地址

编辑文件：`Assets/Hotfix/CrazyPoker/Config/GlobalData.cs`

```csharp
public class GlobalData
{
    // 修改为你的服务器IP
    public string GlobalIP = "139.159.248.138";
    
    // 服务器类型：0-开发服 1-测试服 2-正式服 3-MTT测试服
    public const int DEFAULT_SERVER_TYPE = 1;
}
```

#### 服务器类型说明

| 类型 | 值 | 说明 |
|------|---|------|
| 开发服 | 0 | 本地开发环境 |
| 测试服 | 1 | 测试环境 |
| 正式服 | 2 | 生产环境 |
| MTT测试服 | 3 | 锦标赛测试环境 |

### 2. 端口配置

客户端连接的服务器端口：

| 服务 | 端口 | 说明 |
|------|------|------|
| 登录服务 | 8500 | 用户登录认证 |
| 游戏服务 | 8501 | 游戏逻辑处理 |
| 锦标赛服务 | 8502 | 锦标赛功能 |
| 奥马哈服务 | 8503 | 奥马哈游戏 |
| 支付服务 | 8600 | 支付功能 |
| 资源服务 | 8504 | 资源下载 |
| 消息服务 | 8505 | 消息推送 |
| API服务 | 8700 | HTTP接口 |

### 3. 第三方服务配置

#### 腾讯IM配置

编辑文件：`Assets/Hotfix/UI/UILobby/Component/IMSdkComponent.cs`

```csharp
// 腾讯IM SDK配置
public const int IM_APPID_0 = 1400478370;  // 开发服
public const int IM_APPID_1 = 1400478370;  // 测试服
public const int IM_APPID_2 = 1400478370;  // 正式服
```

#### 腾讯Bugly配置

编辑文件：`Assets/Hotfix/CrazyPoker/Config/GlobalData.cs`

```csharp
// 腾讯Bugly配置
public const string BUGLY_APPID_ANDROID_1 = "***";  // 测试服Android
public const string BUGLY_APPID_ANDROID_2 = "***";  // 正式服Android
public const string BUGLY_APPID_IOS_1 = "***";      // 测试服iOS
public const string BUGLY_APPID_IOS_2 = "***";      // 正式服iOS
```

替换`***`为你的Bugly AppID。

#### 极光推送配置

编辑文件：`Assets/Hotfix/UI/UILobby/Component/JPushSdkComponent.cs`

```csharp
// 极光推送配置
public const string JPUSH_APPKEY = "***";  // 替换为你的AppKey
public const string JPUSH_CHANNEL = "developer";  // 渠道号
```

### 4. 应用配置

#### 应用名称

编辑文件：`ProjectSettings/ProjectSettings.asset`

```yaml
productName: 红德州
```

#### 应用图标

1. 选择`Project Settings` -> `Player`
2. 在`Icons`部分设置应用图标
3. 支持不同分辨率的图标

#### 启动画面

1. 选择`Project Settings` -> `Player`
2. 在`Splash Image`部分设置启动画面
3. 支持横屏和竖屏

### 5. 平台特定配置

#### Android配置

1. 选择`Project Settings` -> `Player`
2. 选择Android平台
3. 配置以下选项：

**包名（Package Name）**
```
com.crazypoker.game
```

**最低API级别**
```
21 (Android 5.0)
```

**目标API级别**
```
30 (Android 11)
```

**权限配置**
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```

**签名配置**
- Debug签名：使用Unity默认签名
- Release签名：配置自己的签名文件

#### iOS配置

1. 选择`Project Settings` -> `Player`
2. 选择iOS平台
3. 配置以下选项：

**Bundle Identifier**
```
com.crazypoker.game
```

**最低iOS版本**
```
10.0
```

**目标iOS版本**
```
14.0
```

**权限配置**
```xml
<key>NSCameraUsageDescription</key>
<string>需要访问摄像头</string>
<key>NSMicrophoneUsageDescription</key>
<string>需要访问麦克风</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>需要访问相册</string>
```

**签名配置**
- 开发证书：配置开发证书和描述文件
- 发布证书：配置发布证书和描述文件

## 编译打包

### 1. Android打包

#### Debug版本

1. 选择`File` -> `Build Settings`
2. 选择Android平台
3. 点击`Switch Platform`
4. 选择`Development Build`和`Script Debugging`
5. 点击`Build`
6. 选择输出目录
7. 等待编译完成

#### Release版本

1. 选择`File` -> `Build Settings`
2. 选择Android平台
3. 点击`Switch Platform`
4. 不选择`Development Build`
5. 配置签名文件
6. 点击`Build`
7. 选择输出目录
8. 等待编译完成

#### APK生成

编译完成后，会生成APK文件：
```
redPoker.apk
```

### 2. iOS打包

#### 生成Xcode项目

1. 选择`File` -> `Build Settings`
2. 选择iOS平台
3. 点击`Switch Platform`
4. 点击`Build`
5. 选择输出目录
6. 等待生成完成

#### 使用Xcode打包

1. 打开生成的Xcode项目
2. 配置签名和描述文件
3. 选择设备或模拟器
4. 点击`Run`运行或`Product` -> `Archive`打包

### 3. Windows打包

1. 选择`File` -> `Build Settings`
2. 选择Windows平台
3. 点击`Switch Platform`
4. 选择`x86_64`架构
5. 点击`Build`
6. 选择输出目录
7. 等待编译完成

### 4. Mac打包

1. 选择`File` -> `Build Settings`
2. 选择Mac平台
3. 点击`Switch Platform`
4. 选择`Intel`或`Intel 64-bit`架构
5. 点击`Build`
6. 选择输出目录
7. 等待编译完成

## 常见问题

### 1. 项目导入失败

**问题**：项目导入时出现错误

**解决方案**：
- 检查Unity版本是否正确
- 检查项目路径是否包含中文或特殊字符
- 检查磁盘空间是否足够
- 重新导入项目

### 2. 编译错误

**问题**：编译时出现错误

**解决方案**：
- 检查JDK版本是否正确
- 检查Android SDK是否完整
- 检查项目依赖是否完整
- 清理项目缓存：`Assets` -> `Reimport All`

### 3. 运行时崩溃

**问题**：应用运行时崩溃

**解决方案**：
- 检查服务器配置是否正确
- 检查网络连接是否正常
- 查看日志文件：`Player.log`
- 使用Bugly查看崩溃日志

### 4. 无法连接服务器

**问题**：客户端无法连接服务器

**解决方案**：
- 检查服务器IP是否正确
- 检查服务器端口是否开放
- 检查网络连接是否正常
- 检查防火墙设置

### 5. 资源加载失败

**问题**：游戏资源加载失败

**解决方案**：
- 检查资源服务是否启动
- 检查资源路径是否正确
- 检查CDN配置是否正确
- 清理资源缓存

### 6. 热更新失败

**问题**：热更新失败

**解决方案**：
- 检查热更新服务器是否启动
- 检查版本号是否正确
- 检查网络连接是否正常
- 清理本地缓存

### 7. 第三方SDK集成失败

**问题**：第三方SDK集成失败

**解决方案**：
- 检查SDK配置是否正确
- 检查AppID是否正确
- 检查权限配置是否完整
- 查看SDK文档

## 性能优化

### 1. 减少包体大小

- 压缩图片资源
- 压缩音频资源
- 使用Addressables管理资源
- 移除未使用的资源

### 2. 提高运行性能

- 使用对象池减少GC
- 优化Draw Call
- 使用LOD优化模型
- 异步加载资源

### 3. 优化内存使用

- 及时释放不用的资源
- 使用纹理压缩
- 优化模型面数
- 减少内存碎片

## 测试

### 1. 功能测试

- 测试登录功能
- 测试游戏功能
- 测试支付功能
- 测试社交功能

### 2. 性能测试

- 测试帧率
- 测试内存使用
- 测试加载时间
- 测试网络延迟

### 3. 兼容性测试

- 测试不同Android版本
- 测试不同iOS版本
- 测试不同屏幕分辨率
- 测试不同设备型号

### 4. 稳定性测试

- 长时间运行测试
- 压力测试
- 异常情况测试
- 网络异常测试

## 发布

### 1. Android发布

1. 准备APK文件
2. 准备应用截图
3. 准备应用描述
4. 上传到应用商店
5. 等待审核

### 2. iOS发布

1. 准备IPA文件
2. 准备应用截图
3. 准备应用描述
4. 上传到App Store
5. 等待审核

## 技术支持

如有问题，请联系技术支持团队。

## 附录

### A. 配置文件清单

| 文件路径 | 说明 |
|---------|------|
| `Assets/Hotfix/CrazyPoker/Config/GlobalData.cs` | 全局配置 |
| `Assets/Hotfix/UI/UILobby/Component/IMSdkComponent.cs` | 腾讯IM配置 |
| `Assets/Hotfix/UI/UILobby/Component/JPushSdkComponent.cs` | 极光推送配置 |
| `ProjectSettings/ProjectSettings.asset` | 项目配置 |

### B. 端口清单

| 端口 | 服务 | 说明 |
|------|------|------|
| 8500 | 登录服务 | 用户登录认证 |
| 8501 | 游戏服务 | 游戏逻辑处理 |
| 8502 | 锦标赛服务 | 锦标赛功能 |
| 8503 | 奥马哈服务 | 奥马哈游戏 |
| 8600 | 支付服务 | 支付功能 |
| 8504 | 资源服务 | 资源下载 |
| 8505 | 消息服务 | 消息推送 |
| 8663 | 运营后台 | 运营管理 |
| 8700 | API服务 | HTTP接口 |

### C. 第三方服务清单

| 服务 | 用途 | 官网 |
|------|------|------|
| 腾讯IM | 即时通讯 | https://cloud.tencent.com/product/im |
| 腾讯Bugly | 崩溃统计 | https://bugly.qq.com |
| 极光推送 | 消息推送 | https://www.jiguang.cn |
| BestHTTP | HTTP通信 | https://besthttp.theperfectedge.com |
| DOTween | 动画引擎 | https://dotween.demigiant.com |

---

**更新日期**：2026-03-22
**版本**：v1.0.0
