# isImsSwitchEnabledSync (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## isImsSwitchEnabledSync

```TypeScript
function isImsSwitchEnabledSync(slotId: int): boolean
```

Judge whether the Ims switch is enabled.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-call-function isImsSwitchEnabledSync(slotId: int): boolean--><!--Device-call-function isImsSwitchEnabledSync(slotId: int): boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
let slotId: number = 0;
try {
    let isEnabled: boolean = call.isImsSwitchEnabledSync(slotId);
    console.info(`isImsSwitchEnabledSync success : ${isEnabled}`);
} catch (error) {
    console.error(`isImsSwitchEnabledSync fail : err->${JSON.stringify(error)}`);  
}
```

