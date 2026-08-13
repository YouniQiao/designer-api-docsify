# makeCall

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## makeCall

```TypeScript
function makeCall(phoneNumber: string, callback: AsyncCallback<void>): void
```

Launches the call screen and displays the dialed number. This API uses an asynchronous callback to return the result. This API can be called only in a UIAbility.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-call-function makeCall(phoneNumber: string, callback: AsyncCallback<void>): void--><!--Device-call-function makeCall(phoneNumber: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

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
// The tel URI format is supported since API version 15, for example, tel:13xxxx.
call.makeCall("138xxxxxxxx", (err: BusinessError) => {
    if (err) {
        console.error(`makeCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`makeCall success`);
    }
});
```


## makeCall

```TypeScript
function makeCall(phoneNumber: string): Promise<void>
```

Launches the call screen and displays the dialed number. This API uses a promise to return the result. This API can be called only in a UIAbility.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-call-function makeCall(phoneNumber: string): Promise<void>--><!--Device-call-function makeCall(phoneNumber: string): Promise<void>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

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
// The tel URI format is supported since API version 15, for example, tel:13xxxx.
call.makeCall("138xxxxxxxx").then(() => {
    console.info(`makeCall success`);
}).catch((err: BusinessError) => {
    console.error(`makeCall fail, promise: err->${JSON.stringify(err)}`);
});
```


## makeCall

```TypeScript
function makeCall(phoneNumber: string, options?: MakeCallOptions): Promise<void>
```

Launches the call screen and displays the dialed number. This API uses a promise to return the result. This API can be called only in a UIAbility.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-call-function makeCall(phoneNumber: string, options?: MakeCallOptions): Promise<void>--><!--Device-call-function makeCall(phoneNumber: string, options?: MakeCallOptions): Promise<void>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| options | [MakeCallOptions](arkts-telephony-call-makecalloptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { call } from '@kit.TelephonyKit';

// Set whether to return to the current application after the call ends.
let makeOptions: call.MakeCallOptions = {
  isHideDialScreen: true
}

call.makeCall("138xxxxxxxx", makeOptions).then(() => {
    console.info(`makeCall success`);
}).catch((err: BusinessError) => {
    console.error(`makeCall fail, promise: err->${JSON.stringify(err)}`);
});
```


## makeCall

```TypeScript
function makeCall(context: Context, phoneNumber: string): Promise<void>
```

Launches the call screen and displays the dialed number. This API uses a promise to return the result. You need to declare the **ohos.permission.START_ABILITIES_FROM_BACKGROUND** permission if you want to call the API in the background.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-call-function makeCall(context: Context, phoneNumber: string): Promise<void>--><!--Device-call-function makeCall(context: Context, phoneNumber: string): Promise<void>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| phoneNumber | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |

## Examples

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// Obtain the application context.
let context = this.getUIContext().getHostContext() as Context;
// The tel URI format is supported since API version 15, for example, tel:13xxxx.
call.makeCall(context, "138xxxxxxxx").then(() => {
    console.info(`makeCall success`);
}).catch((err: BusinessError) => {
    console.error(`makeCall fail, promise: err->${JSON.stringify(err)}`);
});
```
