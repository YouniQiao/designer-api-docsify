# formatPhoneNumberToE164

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## formatPhoneNumberToE164

```TypeScript
function formatPhoneNumberToE164(phoneNumber: string, countryCode: string, callback: AsyncCallback<string>): void
```

Converts a phone number into the E.164 format. This API uses an asynchronous callback to return the result. The phone number must match the specified country code. For example, for a China phone number, the country code must be **CN**. Otherwise, **null** will be returned.

**Since:** 23

**Deprecated since:** -1

<!--Device-call-function formatPhoneNumberToE164(phoneNumber: string, countryCode: string, callback: AsyncCallback<string>): void--><!--Device-call-function formatPhoneNumberToE164(phoneNumber: string, countryCode: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| countryCode | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.formatPhoneNumberToE164("138xxxxxxxx", "CN", (err: BusinessError, data: string) => {
    if (err) {
        console.error(`formatPhoneNumberToE164 fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`formatPhoneNumberToE164 success, data->${JSON.stringify(data)}`);
    }
});
```


## formatPhoneNumberToE164

```TypeScript
function formatPhoneNumberToE164(phoneNumber: string, countryCode: string): Promise<string>
```

Converts a phone number into the E.164 format. This API uses a promise to return the result. The phone number must match the specified country code. For example, for a China phone number, the country code must be **CN**. Otherwise, **null** will be returned. All country codes are supported.

**Since:** 23

**Deprecated since:** -1

<!--Device-call-function formatPhoneNumberToE164(phoneNumber: string, countryCode: string): Promise<string>--><!--Device-call-function formatPhoneNumberToE164(phoneNumber: string, countryCode: string): Promise<string>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| countryCode | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.formatPhoneNumberToE164("138xxxxxxxx", "CN").then((data: string) => {
    console.info(`formatPhoneNumberToE164 success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`formatPhoneNumberToE164 fail, promise: err->${JSON.stringify(err)}`);
});
```
