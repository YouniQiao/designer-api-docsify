# getImsShortMessageFormat (System API)

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## getImsShortMessageFormat

```TypeScript
function getImsShortMessageFormat(callback: AsyncCallback<string>): void
```

Obtains the SMS format supported by the IMS, for example, **3gpp**, **3gpp2**, or **unknown**. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-sms-function getImsShortMessageFormat(callback: AsyncCallback<string>): void--><!--Device-sms-function getImsShortMessageFormat(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

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

sms.getImsShortMessageFormat((err: BusinessError, data: string) => {
      console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getImsShortMessageFormat

```TypeScript
function getImsShortMessageFormat(): Promise<string>
```

Obtains the SMS format supported by the IMS, for example, **3gpp**, **3gpp2**, or **unknown**. This API uses a promise to return the result.

**Since:** 8

<!--Device-sms-function getImsShortMessageFormat(): Promise<string>--><!--Device-sms-function getImsShortMessageFormat(): Promise<string>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |

## Examples

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getImsShortMessageFormat().then((data: string) => {
    console.info(`getImsShortMessageFormat success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getImsShortMessageFormat failed, promise: err->${JSON.stringify(err)}`);
});
```
