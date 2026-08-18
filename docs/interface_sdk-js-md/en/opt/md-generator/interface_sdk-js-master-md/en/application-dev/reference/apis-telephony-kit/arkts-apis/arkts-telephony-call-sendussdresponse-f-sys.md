# sendUssdResponse (System API)

## Modules to Import

```TypeScript
```

## sendUssdResponse

```TypeScript
function sendUssdResponse(slotId: number, content: string): void
```

Sends a response to the Unstructured Supplementary Service Data (USSD) service to the carrier.

**Since:** 26.0.0

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function sendUssdResponse(slotId: int, content: string): void--><!--Device-call-function sendUssdResponse(slotId: int, content: string): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| content | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { call } from '@kit.TelephonyKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

function testSendUssdResponse() {
    const slotId: number = 0;
    const content: string = "OK";

    try {
        call.sendUssdResponse(slotId, content);
    } catch (error) {
        const err = error as BusinessError;
        hilog.error(0x0000, 'testTag', `Failed to send USSD response. Code: ${err.code}, Message: ${err.message}`);
    }
}
```
