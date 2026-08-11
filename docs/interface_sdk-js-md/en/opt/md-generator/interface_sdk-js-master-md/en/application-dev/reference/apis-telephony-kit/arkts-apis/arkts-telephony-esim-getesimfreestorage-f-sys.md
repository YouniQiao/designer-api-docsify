# getEsimFreeStorage (System API)

## Modules to Import

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## getEsimFreeStorage

```TypeScript
function getEsimFreeStorage(): Promise<number>
```

Returns the remaining storage space in KB for the eUICC hardware.

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getEsimFreeStorage(): Promise<int>--><!--Device-eSIM-function getEsimFreeStorage(): Promise<int>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

eSIM.getEsimFreeStorage().then((data) => {
    console.info(`getEsimFreeStorage invoking succeeded.freeStorage: ${data}`);
}).catch((err: BusinessError<void>) => {
    console.error(`getEsimFreeStorage , promise: err->${JSON.stringify(err)}`);
});
```
