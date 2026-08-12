# uninstallLocalPlugin

## Modules to Import

```TypeScript
import { pluginBundleManager } from '@kit.AbilityKit';
```

## uninstallLocalPlugin

```TypeScript
function uninstallLocalPlugin(pluginBundleName: string): Promise<void>
```

Uninstall the plugin for self application.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginBundleManager-function uninstallLocalPlugin(pluginBundleName: string): Promise<void>--><!--Device-pluginBundleManager-function uninstallLocalPlugin(pluginBundleName: string): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pluginBundleName | string | Yes | Indicates the bundle name of plugin application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17700092](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700092-plugin-uninstall-failure-because-of-nonexistent-plugin-bundle-name) | Failed to uninstall the plugin because the specified plugin is not found. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Calling interface without permission 'ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN'. |

