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

**Deprecated since:** -1

**Required permissions:** ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginBundleManager-function uninstallLocalPlugin(pluginBundleName: string): Promise<void>--><!--Device-pluginBundleManager-function uninstallLocalPlugin(pluginBundleName: string): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pluginBundleName](arkts-ability-pluginbundleinfo-i-sys.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17700092](../errorcode-bundle.md#17700092-plugin-uninstall-failure-because-of-nonexistent-plugin-bundle-name) |
| [201](../../errorcode-universal.md#201-permission-denied) |
