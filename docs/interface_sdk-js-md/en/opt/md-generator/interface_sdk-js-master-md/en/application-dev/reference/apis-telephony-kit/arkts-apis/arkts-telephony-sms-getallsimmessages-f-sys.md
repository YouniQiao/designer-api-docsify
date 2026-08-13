# getAllSimMessages (System API)

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## getAllSimMessages

```TypeScript
function getAllSimMessages(slotId: number, callback: AsyncCallback<Array<SimShortMessage>>): void
```

Obtains all SIM card messages. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.RECEIVE_SMS

<!--Device-sms-function getAllSimMessages(slotId: int, callback: AsyncCallback<Array<SimShortMessage>>): void--><!--Device-sms-function getAllSimMessages(slotId: int, callback: AsyncCallback<Array<SimShortMessage>>): void-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[SimShortMessage](arkts-telephony-sms-simshortmessage-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
sms.getAllSimMessages(slotId, (err: BusinessError, data: sms.SimShortMessage[]) => {
      console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getAllSimMessages

```TypeScript
function getAllSimMessages(slotId: number): Promise<Array<SimShortMessage>>
```

Obtains all SIM card messages. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.RECEIVE_SMS

<!--Device-sms-function getAllSimMessages(slotId: int): Promise<Array<SimShortMessage>>--><!--Device-sms-function getAllSimMessages(slotId: int): Promise<Array<SimShortMessage>>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[SimShortMessage](arkts-telephony-sms-simshortmessage-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
let promise = sms.getAllSimMessages(slotId);
promise.then((data: sms.SimShortMessage[]) => {
    console.info(`getAllSimMessages success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getAllSimMessages failed, promise: err->${JSON.stringify(err)}`);
});
```
