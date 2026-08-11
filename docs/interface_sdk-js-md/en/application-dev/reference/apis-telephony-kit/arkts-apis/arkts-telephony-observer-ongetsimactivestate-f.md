# onGetSimActiveState

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## onGetSimActiveState

```TypeScript
function onGetSimActiveState(slotId: int, callback: Callback<boolean>): void
```

Subscribe to sim active state change events using a callback-based approach as an asynchronous method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-observer-function onGetSimActiveState(slotId: int, callback: Callback<boolean>): void--><!--Device-observer-function onGetSimActiveState(slotId: int, callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the ID of the target card slot. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | Indicates the callback for sim active state |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let sislotId = 0;
let simActiveState: Callback<boolean> = (isSimActive: boolean) => {
    console.info(`simActiveState slotId ${JSON.stringify(isSimActive)}`);
}
observer.onGetSimActiveState(sislotId, simActiveState);
```

