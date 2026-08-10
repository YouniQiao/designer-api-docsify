# isManualNetworkScanning (System API)

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## isManualNetworkScanning

```TypeScript
function isManualNetworkScanning(slotId: int): Promise<boolean>
```

Determine whether the current manual network scan is in progress.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function isManualNetworkScanning(slotId: int): Promise<boolean>--><!--Device-radio-function isManualNetworkScanning(slotId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | the promise return ManualNetworkScanState. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Nonsystem applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
radio.isManualNetworkScanning(0).then((state: boolean) => {
    console.info(`isManualNetworkScanning success, state->${JSON.stringify(state)}`);
}).catch((err: BusinessError) => {
    console.error(`isManualNetworkScanning failed, promise: err->${JSON.stringify(err)}`);
});
```

