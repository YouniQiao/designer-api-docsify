# isManualNetworkScanning (System API)

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## isManualNetworkScanning

```TypeScript
function isManualNetworkScanning(slotId: number): Promise<boolean>
```

Determine whether the current manual network scan is in progress.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function isManualNetworkScanning(slotId: int): Promise<boolean>--><!--Device-radio-function isManualNetworkScanning(slotId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
radio.isManualNetworkScanning(0).then((state: boolean) => {
    console.info(`isManualNetworkScanning success, state->${JSON.stringify(state)}`);
}).catch((err: BusinessError) => {
    console.error(`isManualNetworkScanning failed, promise: err->${JSON.stringify(err)}`);
});
```
