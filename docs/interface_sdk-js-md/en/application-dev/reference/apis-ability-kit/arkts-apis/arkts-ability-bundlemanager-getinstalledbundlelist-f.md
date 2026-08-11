# getInstalledBundleList

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getInstalledBundleList

```TypeScript
function getInstalledBundleList(bundleFlags: int): Promise<Array<BundleInfo>>
```

Obtains all the bundle information in the system based on the given bundle flags.This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_GET_INSTALLED_BUNDLE_LIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getInstalledBundleList(bundleFlags: int): Promise<Array<BundleInfo>>--><!--Device-bundleManager-function getInstalledBundleList(bundleFlags: int): Promise<Array<BundleInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Information contained in the returned BundleInfo. For details, see {@link BundleFlag}. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BundleInfo&gt;&gt; | Promise used to return the list of installed applications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

