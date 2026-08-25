# getCallTransferInfo

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## getCallTransferInfo

```TypeScript
function getCallTransferInfo(type: CallTransferType, number: string): Promise<CallTransferResult>
```

Obtains call transfer information with the phone number. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_CALL_TRANSFER_INFO

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [CallTransferType](arkts-telephony-call-calltransfertype-e.md) | Yes |
| number | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CallTransferResult](arkts-telephony-call-calltransferresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8401002](../errorcode-telephony.md#8401002-incorrect-number) |
| [8401003](../errorcode-telephony.md#8401003-frequent-operations) |
