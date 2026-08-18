# getCallWaitingStatus (System API)

## Modules to Import

```TypeScript
```

## getCallWaitingStatus

```TypeScript
function getCallWaitingStatus(slotId: number, callback: AsyncCallback<CallWaitingStatus>): void
```

Obtains the call waiting status. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getCallWaitingStatus(slotId: int, callback: AsyncCallback<CallWaitingStatus>): void--><!--Device-call-function getCallWaitingStatus(slotId: int, callback: AsyncCallback<CallWaitingStatus>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CallWaitingStatus](arkts-telephony-call-callwaitingstatus-e-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getCallWaitingStatus(0, (err: BusinessError, data: call.CallWaitingStatus) => {
    if (err) {
        console.error(`getCallWaitingStatus fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`getCallWaitingStatus success, data->${JSON.stringify(data)}`);
    }
});
```


## getCallWaitingStatus

```TypeScript
function getCallWaitingStatus(slotId: number): Promise<CallWaitingStatus>
```

Obtains the call waiting status. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getCallWaitingStatus(slotId: int): Promise<CallWaitingStatus>--><!--Device-call-function getCallWaitingStatus(slotId: int): Promise<CallWaitingStatus>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CallWaitingStatus](arkts-telephony-call-callwaitingstatus-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getCallWaitingStatus(0).then((data: call.CallWaitingStatus) => {
    console.info(`getCallWaitingStatus success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getCallWaitingStatus fail, promise: err->${JSON.stringify(err)}`);
});
```
