# answerCall (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## answerCall

```TypeScript
function answerCall(callId: number, callback: AsyncCallback<void>): void
```

Answers a call. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ANSWER_CALL

<!--Device-call-function answerCall(callId: int, callback: AsyncCallback<void>): void--><!--Device-call-function answerCall(callId: int, callback: AsyncCallback<void>): void-End-->

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.answerCall(1, (err: BusinessError) => {
    if (err) {
        console.error(`answerCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`answerCall success.`);
    }
});
```


## answerCall

```TypeScript
function answerCall(callId?: number): Promise<void>
```

Answers a call. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ANSWER_CALL

<!--Device-call-function answerCall(callId?: int): Promise<void>--><!--Device-call-function answerCall(callId?: int): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.answerCall(1).then(() => {
    console.info(`answerCall success.`);
}).catch((err: BusinessError) => {
    console.error(`answerCall fail, promise: err->${JSON.stringify(err)}`);
});
```


## answerCall

```TypeScript
function answerCall(callback: AsyncCallback<void>): void
```

Answers a call. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ANSWER_CALL or ohos.permission.MANAGE_CALL_FOR_DEVICES

<!--Device-call-function answerCall(callback: AsyncCallback<void>): void--><!--Device-call-function answerCall(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.answerCall((err: BusinessError) => {
    if (err) {
        console.error(`answerCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`answerCall success.`);
    }
});
```


## answerCall

```TypeScript
function answerCall(videoState: VideoStateType, callId: number): Promise<void>
```

Answers a call. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ANSWER_CALL

<!--Device-call-function answerCall(videoState: VideoStateType, callId: int): Promise<void>--><!--Device-call-function answerCall(videoState: VideoStateType, callId: int): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| videoState | [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md) | Yes |
| callId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.answerCall(0, 1).then(() => {
    console.info(`answerCall success.`);
}).catch((err: BusinessError) => {
    console.error(`answerCall fail, promise: err->${JSON.stringify(err)}`);
});
```


## answerCall

```TypeScript
function answerCall(videoState: VideoStateType, callId: number, isRtt: boolean): Promise<void>
```

Answers the incoming rtt

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ANSWER_CALL

<!--Device-call-function answerCall(videoState: VideoStateType, callId: int, isRtt: boolean): Promise<void>--><!--Device-call-function answerCall(videoState: VideoStateType, callId: int, isRtt: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| videoState | [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md) | Yes |
| callId | number | Yes |
| isRtt | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
