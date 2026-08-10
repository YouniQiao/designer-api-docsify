# getPluginBundlePathForSelf

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getPluginBundlePathForSelf

```TypeScript
function getPluginBundlePathForSelf(pluginBundleName: string): string
```

获取指定插件在当前[应用沙箱](../../../file-management/app-sandbox-directory.md)内的安装路径。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-bundleManager-function getPluginBundlePathForSelf(pluginBundleName: string): string--><!--Device-bundleManager-function getPluginBundlePathForSelf(pluginBundleName: string): string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pluginBundleName | string | Yes | 目标插件的包名。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 目标插件在当前应用沙箱内的安装路径。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700001 | The specified bundleName is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Use the actual bundle name of the plugin.
let pluginBundleName = 'com.ohos.pluginDemo';
try {
  let path = bundleManager.getPluginBundlePathForSelf(pluginBundleName);
  hilog.info(0x0000, 'testTag', 'getPluginBundlePathForSelf successfully. path: %{public}s', path);
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getPluginBundlePathForSelf failed. Cause: %{public}s', message);
}
```

