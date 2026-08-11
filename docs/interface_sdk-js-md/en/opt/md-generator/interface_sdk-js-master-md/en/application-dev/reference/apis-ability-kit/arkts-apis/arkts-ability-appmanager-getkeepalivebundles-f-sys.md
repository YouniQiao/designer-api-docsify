# getKeepAliveBundles (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getKeepAliveBundles

```TypeScript
function getKeepAliveBundles(type: KeepAliveAppType, userId?: number): Promise<Array<KeepAliveBundleInfo>>
```

Obtains information about a specified type of keep-alive application of a user. The application information is defined by [KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md). This API uses a promise to return the result.This API can be properly called on PCs/2-in-1 devices. If it is called on other devices, error code 801 is returned.  
**Required permissions**: ohos.permission.MANAGE_APP_KEEP_ALIVE

**Since:** 14

**Required permissions:** ohos.permission.MANAGE_APP_KEEP_ALIVE

<!--Device-appManager-function getKeepAliveBundles(type: KeepAliveAppType, userId?: int): Promise<Array<KeepAliveBundleInfo>>--><!--Device-appManager-function getKeepAliveBundles(type: KeepAliveAppType, userId?: int): Promise<Array<KeepAliveBundleInfo>>-End-->

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
| Promise&lt;Array&lt;KeepAliveBundleInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userId = 100;
let type: appManager.KeepAliveAppType = appManager.KeepAliveAppType.THIRD_PARTY;
try {
  appManager.getKeepAliveBundles(type, userId).then((data) => {
    console.info(`getKeepAliveBundles success, data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`getKeepAliveBundles fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] getKeepAliveBundles error: ${code}, ${message}`);
}
```
