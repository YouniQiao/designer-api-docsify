# isNewCallAllowed (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## isNewCallAllowed

```TypeScript
function isNewCallAllowed(callback: AsyncCallback<boolean>): void
```

Judge whether to allow another new call.

**Since:** 8

<!--Device-call-function isNewCallAllowed(callback: AsyncCallback<boolean>): void--><!--Device-call-function isNewCallAllowed(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

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
import { BusinessError } from '@kit.BasicServicesKit';

call.isNewCallAllowed((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isNewCallAllowed fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`isNewCallAllowed success, data->${JSON.stringify(data)}`);
    }
});
```


## isNewCallAllowed

```TypeScript
function isNewCallAllowed(): Promise<boolean>
```

Judge whether to allow another new call.

**Since:** 8

<!--Device-call-function isNewCallAllowed(): Promise<boolean>--><!--Device-call-function isNewCallAllowed(): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.isNewCallAllowed().then((data: boolean) => {
    console.info(`isNewCallAllowed success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isNewCallAllowed fail, promise: err->${JSON.stringify(err)}`);
});
```
