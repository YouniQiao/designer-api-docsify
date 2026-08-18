# getDefaultSmsSimId

## Modules to Import

```TypeScript
```

## getDefaultSmsSimId

```TypeScript
function getDefaultSmsSimId(callback: AsyncCallback<number>): void
```

Obtains the default ID of the SIM card used to send SMS messages. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-sms-function getDefaultSmsSimId(callback: AsyncCallback<int>): void--><!--Device-sms-function getDefaultSmsSimId(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8301001](../errorcode-telephony.md#8301001-sim-card-not-activated) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSimId((err: BusinessError, data: number) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getDefaultSmsSimId

```TypeScript
function getDefaultSmsSimId(): Promise<number>
```

Obtains the default ID of the SIM card used to send SMS messages. This API uses a promise to return the result.

**Since:** 23

<!--Device-sms-function getDefaultSmsSimId(): Promise<int>--><!--Device-sms-function getDefaultSmsSimId(): Promise<int>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [8301001](../errorcode-telephony.md#8301001-sim-card-not-activated) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let promise = sms.getDefaultSmsSimId();
promise.then((data: number) => {
    console.info(`getDefaultSmsSimId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultSmsSimId failed, promise: err->${JSON.stringify(err)}`);
});
```
