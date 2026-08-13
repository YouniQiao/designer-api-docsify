# getCallTransferInfo

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## getCallTransferInfo

```TypeScript
function getCallTransferInfo(type: CallTransferType, number: string): Promise<CallTransferResult>
```

Obtains call transfer information with the phone number. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_CALL_TRANSFER_INFO

<!--Device-call-function getCallTransferInfo(type: CallTransferType, number: string): Promise<CallTransferResult>--><!--Device-call-function getCallTransferInfo(type: CallTransferType, number: string): Promise<CallTransferResult>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [CallTransferType](arkts-telephony-call-calltransfertype-e-sys.md) | Yes |
| number | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CallTransferResult](arkts-telephony-call-calltransferresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8401002](../errorcode-telephony.md#8401002-incorrect-number) |
| [8401003](../errorcode-telephony.md#8401003-frequent-operations) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { call } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let type: call.CallTransferType = call.CallTransferType.TRANSFER_TYPE_UNCONDITIONAL;
let number: string = "138xxxxxxxx";

call.getCallTransferInfo(type, number)
    .then((data: call.CallTransferResult) => {
        console.info(`getCallTransferInfo success, data->${JSON.stringify(data)}`);
    })
    .catch((err:BusinessError) => {
        console.error(`getCallTransferInfo fail, err->${JSON.stringify(err)}`);
    });
```
