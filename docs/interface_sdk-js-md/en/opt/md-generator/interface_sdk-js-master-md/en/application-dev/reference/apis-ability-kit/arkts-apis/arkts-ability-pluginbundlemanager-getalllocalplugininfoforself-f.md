# getAllLocalPluginInfoForSelf

## Modules to Import

```TypeScript
import { pluginBundleManager } from '@kit.AbilityKit';
```

## getAllLocalPluginInfoForSelf

```TypeScript
function getAllLocalPluginInfoForSelf(): Promise<Array<PluginBundleInfo>>
```

Obtains information about all local plugins installed on the current application.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginBundleManager-function getAllLocalPluginInfoForSelf(): Promise<Array<PluginBundleInfo>>--><!--Device-pluginBundleManager-function getAllLocalPluginInfoForSelf(): Promise<Array<PluginBundleInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;PluginBundleInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
