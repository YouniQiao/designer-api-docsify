# sendRttMessage (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## sendRttMessage

```TypeScript
function sendRttMessage(callId: number, rttMessage: string): Promise<void>
```

Send rtt message.

**Since:** 22

**Required permissions:** ohos.permission.PLACE_CALL

<!--Device-call-function sendRttMessage(callId: int, rttMessage: string): Promise<void>--><!--Device-call-function sendRttMessage(callId: int, rttMessage: string): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |
| [rttMessage](arkts-telephony-call-rttmessageinfo-i-sys.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
