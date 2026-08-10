# getAllLocalPluginInfoForSelf

## Modules to Import

```TypeScript
import { pluginBundleManager } from 'kits/@kit.AbilityKit';
```

## getAllLocalPluginInfoForSelf

```TypeScript
function getAllLocalPluginInfoForSelf(): Promise<Array<PluginBundleInfo>>
```

查询当前应用中所有自分发插件的信息。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginBundleManager-function getAllLocalPluginInfoForSelf(): Promise<Array<PluginBundleInfo>>--><!--Device-pluginBundleManager-function getAllLocalPluginInfoForSelf(): Promise<Array<PluginBundleInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;PluginBundleInfo&gt;&gt; | Promise对象，返回当前应用已安装的所有本地插件信息列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Calling interface without permission 'ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN'. |

