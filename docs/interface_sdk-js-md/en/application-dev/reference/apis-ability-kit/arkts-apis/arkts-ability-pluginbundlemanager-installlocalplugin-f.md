# installLocalPlugin

## Modules to Import

```TypeScript
import { pluginBundleManager } from '@kit.AbilityKit';
```

## installLocalPlugin

```TypeScript
function installLocalPlugin(pluginFilePaths: Array<string>): Promise<void>
```

Install the plugin for self application.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pluginFilePaths | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17700010](../errorcode-bundle.md#17700010-bundle-installation-failure-due-to-file-parsing-failure) |
| [17700011](../errorcode-bundle.md#17700011-bundle-installation-failure-due-to-signature-verification-failure) |
| [17700012](../errorcode-bundle.md#17700012-bundle-installation-failure-due-to-invalid-file-path-or-too-large-file) |
| [17700015](../errorcode-bundle.md#17700015-bundle-installation-failure-due-to-different-configuration-information-of-multiple-haps) |
| [17700016](../errorcode-bundle.md#17700016-bundle-installation-failure-due-to-insufficient-system-disk-space) |
| [17700017](../errorcode-bundle.md#17700017-bundle-installation-failure-because-the-version-to-install-is-too-earlier) |
| [17700048](../errorcode-bundle.md#17700048-code-signature-verification-failure) |
| [17700052](../errorcode-bundle.md#17700052-installation-of-debugging-applications-allowed-only-in-developer-mode) |
| [17700073](../errorcode-bundle.md#17700073-installation-failure-caused-by-an-application-with-the-same-bundle-name-but-different-signature-information) |
| [17700087](../errorcode-bundle.md#17700087-unsupported-plugin-installation) |
| [17700091](../errorcode-bundle.md#17700091-plugin-installation-failure-because-of-the-same-plugin-name-and-host-bundle-name) |
