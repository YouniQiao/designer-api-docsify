# getSignalInformation

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## getSignalInformation

```TypeScript
function getSignalInformation(slotId: number, callback: AsyncCallback<Array<SignalInformation>>): void
```

Obtains the list of signal strength information of the registered network corresponding to a specified SIM card.

**Since:** 23

**Deprecated since:** -1

<!--Device-radio-function getSignalInformation(slotId: int, callback: AsyncCallback<Array<SignalInformation>>): void--><!--Device-radio-function getSignalInformation(slotId: int, callback: AsyncCallback<Array<SignalInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;SignalInformation&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getSignalInformation(slotId, (err: BusinessError, data: Array<radio.SignalInformation>) => {
    if (err) {
        console.error(`getSignalInformation failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`getSignalInformation success, callback: data->${JSON.stringify(data)}`);
});
```


## getSignalInformation

```TypeScript
function getSignalInformation(slotId: number): Promise<Array<SignalInformation>>
```

Obtains the list of signal strength information of the registered network corresponding to a specified SIM card.

**Since:** 23

**Deprecated since:** -1

<!--Device-radio-function getSignalInformation(slotId: int): Promise<Array<SignalInformation>>--><!--Device-radio-function getSignalInformation(slotId: int): Promise<Array<SignalInformation>>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;SignalInformation & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getSignalInformation(slotId).then((data: Array<radio.SignalInformation>) => {
    console.info(`getSignalInformation success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSignalInformation failed, promise: err->${JSON.stringify(err)}`);
});
```
