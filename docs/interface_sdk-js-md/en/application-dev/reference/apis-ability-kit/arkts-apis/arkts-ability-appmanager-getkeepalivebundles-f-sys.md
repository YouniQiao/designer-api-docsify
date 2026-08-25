# getKeepAliveBundles (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getKeepAliveBundles

```TypeScript
function getKeepAliveBundles(type: KeepAliveAppType, userId?: number): Promise<Array<KeepAliveBundleInfo>>
```

Obtains information about a specified type of keep-alive application of a user. The application information is defined by [KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md). This API uses a promise to return the result. This API can be properly called on PCs/2-in-1 devices. If it is called on other devices, error code 801 is returned. **Required permissions**: ohos.permission.MANAGE_APP_KEEP_ALIVE

**Since:** 14

**Required permissions:** ohos.permission.MANAGE_APP_KEEP_ALIVE

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [KeepAliveAppType](arkts-ability-appmanager-keepaliveapptype-e-sys.md) | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
