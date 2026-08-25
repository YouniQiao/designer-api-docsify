# installLocalPlugin

## 导入模块

```TypeScript
import { pluginBundleManager } from 'kits/@kit.AbilityKit';
```

## installLocalPlugin

```TypeScript
function installLocalPlugin(pluginFilePaths: Array<string>): Promise<void>
```

为当前应用安装自分发插件（即应用通过自有渠道分发、自主管理的插件）。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pluginFilePaths | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700010](../errorcode-bundle.md#17700010-文件解析失败导致应用安装失败) |
| [17700011](../errorcode-bundle.md#17700011-签名校验失败导致应用安装失败) |
| [17700012](../errorcode-bundle.md#17700012-安装包路径无效或者文件过大导致应用安装失败) |
| [17700015](../errorcode-bundle.md#17700015-多个hap配置信息不同导致应用安装失败) |
| [17700016](../errorcode-bundle.md#17700016-系统磁盘空间不足导致应用安装失败) |
| [17700017](../errorcode-bundle.md#17700017-新安装的应用版本号低于已安装的版本号导致应用安装失败) |
| [17700048](../errorcode-bundle.md#17700048-代码签名校验失败) |
| [17700052](../errorcode-bundle.md#17700052-非开发者模式下不允许安装调试应用) |
| [17700073](../errorcode-bundle.md#17700073-由于设备上存在具有相同包名称但不同签名信息的应用程序导致安装失败) |
| [17700087](../errorcode-bundle.md#17700087-当前设备不支持安装插件) |
| [17700091](../errorcode-bundle.md#17700091-插件与主体同包名) |
