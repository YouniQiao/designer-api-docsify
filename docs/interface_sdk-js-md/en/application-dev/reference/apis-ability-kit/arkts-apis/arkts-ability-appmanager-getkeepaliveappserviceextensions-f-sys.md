# getKeepAliveAppServiceExtensions (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getKeepAliveAppServiceExtensions

```TypeScript
function getKeepAliveAppServiceExtensions(): Promise<Array<KeepAliveBundleInfo>>
```

Obtains information about all AppServiceExtensionAbility components that are kept alive. The information is defined by [KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md). This API uses a promise to return the result. This API can be properly called on PCs/2-in-1 devices. If it is called on other devices, error code 801 is returned.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_APP_KEEP_ALIVE

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
