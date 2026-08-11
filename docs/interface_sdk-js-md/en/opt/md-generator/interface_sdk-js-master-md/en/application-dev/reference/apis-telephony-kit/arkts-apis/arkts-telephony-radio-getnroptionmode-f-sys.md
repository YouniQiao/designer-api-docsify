# getNROptionMode (System API)

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getNROptionMode

```TypeScript
function getNROptionMode(slotId: number, callback: AsyncCallback<NROptionMode>): void
```

Get the option mode of NR.

**Since:** 10

<!--Device-radio-function getNROptionMode(slotId: int, callback: AsyncCallback<NROptionMode>): void--><!--Device-radio-function getNROptionMode(slotId: int, callback: AsyncCallback<NROptionMode>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NROptionMode&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNROptionMode(slotId, (err: BusinessError, data: radio.NROptionMode) => {
    if (err) {
        console.error(`getNROptionMode failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`getNROptionMode success, callback: data->${JSON.stringify(data)}`);
});
```


## getNROptionMode

```TypeScript
function getNROptionMode(slotId: number): Promise<NROptionMode>
```

Get the option mode of NR.

**Since:** 10

<!--Device-radio-function getNROptionMode(slotId: int): Promise<NROptionMode>--><!--Device-radio-function getNROptionMode(slotId: int): Promise<NROptionMode>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;NROptionMode&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNROptionMode(slotId).then((data: radio.NROptionMode) => {
    console.info(`getNROptionMode success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNROptionMode failed, promise: err->${JSON.stringify(err)}`);
});
```
