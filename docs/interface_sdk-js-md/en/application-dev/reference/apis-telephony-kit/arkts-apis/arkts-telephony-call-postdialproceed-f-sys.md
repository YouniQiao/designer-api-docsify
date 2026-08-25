# postDialProceed (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## postDialProceed

```TypeScript
function postDialProceed(callId: number, proceed: boolean, callback: AsyncCallback<void>): void
```

Continues a call by playing a post-dial DTMF string. This API uses an asynchronous callback to return the result.If the called number is in the format of "common phone number + semicolon (;) + DTMF string", for example, **400xxxxxxx;123**, and the listening for **postDialDelay** events is enabled, the system reports a **postDialDelay** event when the call is connected. The application can then call this API to send DTMF tones.

**Since:** 11

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |
| proceed | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |


## postDialProceed

```TypeScript
function postDialProceed(callId: number, proceed: boolean): Promise<void>
```

Continues a call by playing a post-dial DTMF string. This API uses a promise to return the result.If the called number is in the format of "common phone number + semicolon (;) + DTMF string", for example, **400xxxxxxx;123**, and the listening for **postDialDelay** events is enabled, the system reports a **postDialDelay** event when the call is connected. The application can then call this API to send DTMF tones.

**Since:** 11

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |
| proceed | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
