# setDefaultSmdpAddress (System API)

## Modules to Import

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## setDefaultSmdpAddress

```TypeScript
function setDefaultSmdpAddress(slotId: int, address: string): Promise<ResultCode>
```

Set or update the default SM-DP+ address stored in an eUICC.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function setDefaultSmdpAddress(slotId: int, address: string): Promise<ResultCode>--><!--Device-eSIM-function setDefaultSmdpAddress(slotId: int, address: string): Promise<ResultCode>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number. |
| address | string | Yes | The default SM-DP+ address to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ResultCode&gt; | Returns the result code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 3120002 | System internal error. |
| 3120001 | Service connection failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

eSIM.setDefaultSmdpAddress(1, 'testAddress').then(() => {
    console.info(`setDefaultSmdpAddress invoking succeeded.`);
}).catch((err: BusinessError<void>) => {
    console.error(`setDefaultSmdpAddress, ErrorState: err->${JSON.stringify(err)}`);
});
```

