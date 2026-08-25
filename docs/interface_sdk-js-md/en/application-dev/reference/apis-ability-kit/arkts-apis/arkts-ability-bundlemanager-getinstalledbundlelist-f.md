# getInstalledBundleList

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getInstalledBundleList

```TypeScript
function getInstalledBundleList(bundleFlags: number): Promise<Array<BundleInfo>>
```

Obtains all the bundle information in the system based on the given bundle flags. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_GET_INSTALLED_BUNDLE_LIST

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;BundleInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
