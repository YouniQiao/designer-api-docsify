# getAllNewPreinstalledApplicationInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getAllNewPreinstalledApplicationInfo

```TypeScript
function getAllNewPreinstalledApplicationInfo(): Promise<Array<PreinstalledApplicationInfo>>
```

Obtains PreinstalledApplicationInfo of all newly added preinstalled applications during device OTA upgrade.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getAllNewPreinstalledApplicationInfo(): Promise<Array<PreinstalledApplicationInfo>>--><!--Device-bundleManager-function getAllNewPreinstalledApplicationInfo(): Promise<Array<PreinstalledApplicationInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;PreinstalledApplicationInfo&gt;&gt; | Returns a list of PreinstalledApplicationInfo objects. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

