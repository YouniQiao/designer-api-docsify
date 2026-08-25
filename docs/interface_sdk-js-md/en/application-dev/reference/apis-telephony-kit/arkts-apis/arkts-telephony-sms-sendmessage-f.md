# sendMessage

## Modules to Import

```TypeScript
import { sms } from 'kits/@kit.TelephonyKit';
```

## sendMessage

```TypeScript
function sendMessage(options: SendMessageOptions): void
```

Sends an SMS message.

> **NOTE：**&gt;
> This API is supported since API version 6 and deprecated since API version 10. You are advised to use
> [sendShortMessage](arkts-telephony-sms-sendshortmessage-f.md).

**Since:** 6

**Deprecated since:** 10

**Substitutes:** [sendShortMessage](arkts-telephony-sms-sendshortmessage-f.md)

**Required permissions:** ohos.permission.SEND_MESSAGES

**System capability:** SystemCapability.Telephony.SmsMms

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SendMessageOptions](../../apis-arkui/arkts-apis/arkts-arkui-featureability-sendmessageoptions-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
