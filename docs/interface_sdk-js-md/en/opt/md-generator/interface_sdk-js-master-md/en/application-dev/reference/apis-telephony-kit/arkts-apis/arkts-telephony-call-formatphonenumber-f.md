# formatPhoneNumber

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## formatPhoneNumber

```TypeScript
function formatPhoneNumber(phoneNumber: string, options: NumberFormatOptions, callback: AsyncCallback<string>): void
```

Formats a phone number based on specified formatting options. This API uses an asynchronous callback to return the result.

A formatted phone number is a standard numeric string, for example, 555 0100.

**Since:** 7

<!--Device-call-function formatPhoneNumber(phoneNumber: string, options: NumberFormatOptions, callback: AsyncCallback<string>): void--><!--Device-call-function formatPhoneNumber(phoneNumber: string, options: NumberFormatOptions, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| options | [NumberFormatOptions](arkts-telephony-call-numberformatoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: call.NumberFormatOptions = {
    countryCode: "CN"
}
call.formatPhoneNumber("138xxxxxxxx", options, (err: BusinessError, data: string) => {
    if (err) {
        console.error(`formatPhoneNumber fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`formatPhoneNumber success, data->${JSON.stringify(data)}`);
    }
});
```


## formatPhoneNumber

```TypeScript
function formatPhoneNumber(phoneNumber: string, options?: NumberFormatOptions): Promise<string>
```

Formats a phone number based on specified formatting options. This API uses a promise to return the result.

A formatted phone number is a standard numeric string, for example, 555 0100.

**Since:** 7

<!--Device-call-function formatPhoneNumber(phoneNumber: string, options?: NumberFormatOptions): Promise<string>--><!--Device-call-function formatPhoneNumber(phoneNumber: string, options?: NumberFormatOptions): Promise<string>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| options | [NumberFormatOptions](arkts-telephony-call-numberformatoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: call.NumberFormatOptions = {
    countryCode: "CN"
}
call.formatPhoneNumber("138xxxxxxxx", options).then((data: string) => {
    console.info(`formatPhoneNumber success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`formatPhoneNumber fail, promise: err->${JSON.stringify(err)}`);
});
```


## formatPhoneNumber

```TypeScript
function formatPhoneNumber(phoneNumber: string, callback: AsyncCallback<string>): void
```

Formats a phone number. This API uses an asynchronous callback to return the result.

A formatted phone number is a standard numeric string, for example, 555 0100.

**Since:** 7

<!--Device-call-function formatPhoneNumber(phoneNumber: string, callback: AsyncCallback<string>): void--><!--Device-call-function formatPhoneNumber(phoneNumber: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.formatPhoneNumber("138xxxxxxxx", (err: BusinessError, data: string) => {
    if (err) {
        console.error(`formatPhoneNumber fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`formatPhoneNumber success, data->${JSON.stringify(data)}`);
    }
});
```
