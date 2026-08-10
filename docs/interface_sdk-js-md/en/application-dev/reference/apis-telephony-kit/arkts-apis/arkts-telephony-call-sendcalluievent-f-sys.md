# sendCallUiEvent (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## sendCallUiEvent

```TypeScript
function sendCallUiEvent(callId: int, eventName: string): Promise<void>
```

Send call ui event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function sendCallUiEvent(callId: int, eventName: string): Promise<void>--><!--Device-call-function sendCallUiEvent(callId: int, eventName: string): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the identifier of the call. |
| eventName | string | Yes | Indicates the event name. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the sendCallUiEvent. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callId: number = 0;
call.sendCallUiEvent(callId, 'eventName').then(() => {
    console.info(`sendCallUiEvent success.`);
}).catch((err: BusinessError) => {
    console.error(`sendCallUiEvent fail, promise: err->${JSON.stringify(err)}`);
});
```

