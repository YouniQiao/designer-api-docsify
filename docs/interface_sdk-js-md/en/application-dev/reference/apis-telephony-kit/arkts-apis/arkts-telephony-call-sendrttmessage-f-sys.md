# sendRttMessage (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## sendRttMessage

```TypeScript
function sendRttMessage(callId: int, rttMessage: string): Promise<void>
```

Send rtt message.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PLACE_CALL

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
| [rttMessage](arkts-telephony-call-rttmessageinfo-i-sys.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
