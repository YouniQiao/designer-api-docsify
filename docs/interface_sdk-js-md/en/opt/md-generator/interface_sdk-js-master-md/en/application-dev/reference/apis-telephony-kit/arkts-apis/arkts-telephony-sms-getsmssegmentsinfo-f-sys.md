# getSmsSegmentsInfo (System API)

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## getSmsSegmentsInfo

```TypeScript
function getSmsSegmentsInfo(slotId: number, message: string, force7bit: boolean, callback: AsyncCallback<SmsSegmentsInfo>): void
```

Obtains SMS message segment information. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean, callback: AsyncCallback<SmsSegmentsInfo>): void--><!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean, callback: AsyncCallback<SmsSegmentsInfo>): void-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| message | string | Yes |
| force7bit | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SmsSegmentsInfo](arkts-telephony-sms-smssegmentsinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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
sms.getSmsSegmentsInfo(slotId, "message", false, (err: BusinessError, data: sms.SmsSegmentsInfo) => {
      console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getSmsSegmentsInfo

```TypeScript
function getSmsSegmentsInfo(slotId: number, message: string, force7bit: boolean): Promise<SmsSegmentsInfo>
```

Obtains SMS message segment information. This API uses a promise to return the result.

**Since:** 8

<!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean): Promise<SmsSegmentsInfo>--><!--Device-sms-function getSmsSegmentsInfo(slotId: int, message: string, force7bit: boolean): Promise<SmsSegmentsInfo>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| message | string | Yes |
| force7bit | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SmsSegmentsInfo](arkts-telephony-sms-smssegmentsinfo-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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
let promise = sms.getSmsSegmentsInfo(slotId, "message", false);
promise.then((data: sms.SmsSegmentsInfo) => {
    console.info(`getSmsSegmentsInfo success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSmsSegmentsInfo failed, promise: err->${JSON.stringify(err)}`);
});
```
