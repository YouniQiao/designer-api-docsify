# stopManualNetworkScan (System API)

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## stopManualNetworkScan

```TypeScript
function stopManualNetworkScan(slotId: number): Promise<void>
```

Stop ManualNetworkScan.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-radio-function stopManualNetworkScan(slotId: int): Promise<void>--><!--Device-radio-function stopManualNetworkScan(slotId: int): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

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
radio.startManualNetworkScan(0, (err: BusinessError, data: radio.NetworkSearchRealTimeResult) => {
    if (err) {
        console.error(`startManualNetworkScan failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`startManualNetworkScan success, callback: data->${JSON.stringify(data)}`);
    radio.stopManualNetworkScan(0);
});
```
