# getAllBundleInstallInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAllBundleInstallInfo

```TypeScript
function getAllBundleInstallInfo(): Promise<Array<Record<string, Object>>>
```

Obtains the extended install information about all applications in the system. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;Record & lt;string, Object & gt; & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
