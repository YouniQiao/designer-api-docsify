# getAllBundleCacheSize (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAllBundleCacheSize

```TypeScript
function getAllBundleCacheSize(): Promise<number>
```

Obtains the global cache size. This API uses a promise to return the result.It is not possible to obtain the cache of applications that are currently running or have been granted the "AllowAppDataNotCleared" privilege as specified in the [application configuration guide](../../../../device-dev/subsystems/subsys-app-privilege-config-guide.md).

**Since:** 15

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
