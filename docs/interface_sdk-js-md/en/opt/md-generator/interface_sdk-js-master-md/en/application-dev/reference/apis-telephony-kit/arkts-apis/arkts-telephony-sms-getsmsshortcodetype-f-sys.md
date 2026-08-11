# getSmsShortCodeType (System API)

## Modules to Import

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## getSmsShortCodeType

```TypeScript
function getSmsShortCodeType(slotId: number, destAddr: string): Promise<SmsShortCodeType>
```

Get the SMS short code type of the destination address.

**Since:** 23

**Required permissions:** ohos.permission.SEND_MESSAGES

<!--Device-sms-function getSmsShortCodeType(slotId: int, destAddr: string): Promise<SmsShortCodeType>--><!--Device-sms-function getSmsShortCodeType(slotId: int, destAddr: string): Promise<SmsShortCodeType>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| destAddr | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;SmsShortCodeType&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
