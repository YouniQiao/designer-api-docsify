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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-pluginBundleManager-function installLocalPlugin(pluginFilePaths: Array<string>): Promise<void>--><!--Device-pluginBundleManager-function installLocalPlugin(pluginFilePaths: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pluginFilePaths | Array&lt;string&gt; | 是 | 插件文件路径数组，表示要安装的插件文件的路径列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 17700015 | Failed to install the plugin because they have different configuration information. |
| 17700012 | Failed to install the plugin because the HSP path is invalid or the HSP is too large. |
| 17700010 | Failed to install the plugin because the plugin fails to be parsed. |
| 17700011 | Failed to install the plugin because the plugin signature fails to be verified. |
| 17700091 | Failed to install the plugin because the plugin name is the same as the host bundle name. |
| 17700073 | Failed to install the plugin because a plugin with the same &lt;br&gt;bundle name but different signature information exists on the device. |
| 201 | Calling interface without permission 'ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN'. |
| 17700087 | Failed to install the plugin because the current device does not support plugins. |
| 17700052 | Failed to install the plugin because debug bundle cannot be installed under non-developer mode. |
| 17700016 | Failed to install the plugin because of insufficient system disk space. |
| 17700048 | Failed to install the plugin because the code signature verification failed. |
| 17700017 | Failed to install the plugin since the version of the plugin to install is too early. |

