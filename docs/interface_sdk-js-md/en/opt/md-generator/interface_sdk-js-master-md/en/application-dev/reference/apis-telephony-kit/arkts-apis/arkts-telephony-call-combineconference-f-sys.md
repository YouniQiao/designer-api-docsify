# combineConference (System API)

## Modules to Import

```TypeScript
```

## combineConference

```TypeScript
function combineConference(callId: number, callback: AsyncCallback<void>): void
```

Combines two calls into a conference call. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-call-function combineConference(callId: int, callback: AsyncCallback<void>): void--><!--Device-call-function combineConference(callId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 8300007 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.combineConference(1, (err: BusinessError) => {
    if (err) {
        console.error(`combineConference fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`combineConference success.`);
    }
});
```


## combineConference

```TypeScript
function combineConference(callId: number): Promise<void>
```

Combines two calls into a conference call. This API uses a promise to return the result.

**Since:** 23

<!--Device-call-function combineConference(callId: int): Promise<void>--><!--Device-call-function combineConference(callId: int): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 8300007 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.combineConference(1).then(() => {
    console.info(`combineConference success.`);
}).catch((err: BusinessError) => {
    console.error(`combineConference fail, promise: err->${JSON.stringify(err)}`);
});
```
