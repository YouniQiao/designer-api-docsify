# setShowNumber (System API)

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## setShowNumber

```TypeScript
function setShowNumber(slotId: int, teleNumber: string, callback: AsyncCallback<void>): void
```

Set the SIM card number in the specified slot.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function setShowNumber(slotId: int, teleNumber: string, callback: AsyncCallback<void>): void--><!--Device-sim-function setShowNumber(slotId: int, teleNumber: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| teleNumber | string | Yes | Indicates SIM card number. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback of setShowNumber. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300004 | No SIM card found. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let number: string = '+861xxxxxxxxxx';
sim.setShowNumber(0, number, (err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## setShowNumber

```TypeScript
function setShowNumber(slotId: int, teleNumber: string): Promise<void>
```

Set the SIM card number in the specified slot.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function setShowNumber(slotId: int, teleNumber: string): Promise<void>--><!--Device-sim-function setShowNumber(slotId: int, teleNumber: string): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| teleNumber | string | Yes | Indicates SIM card number. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setShowNumber. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300004 | No SIM card found. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let number: string = '+861xxxxxxxxxx';
sim.setShowNumber(0, number).then(() => {
    console.info(`setShowNumber success.`);
}).catch((err: BusinessError) => {
    console.error(`setShowNumber failed, promise: err->${JSON.stringify(err)}`);
});
```

