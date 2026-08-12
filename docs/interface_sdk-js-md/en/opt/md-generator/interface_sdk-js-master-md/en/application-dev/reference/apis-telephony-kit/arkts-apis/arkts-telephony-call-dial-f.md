# dial

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## dial

```TypeScript
function dial(phoneNumber: string, options: DialOptions, callback: AsyncCallback<boolean>): void
```

Makes a call.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialCall)

**Required permissions:** ohos.permission.PLACE_CALL

<!--Device-call-function dial(phoneNumber: string, options: DialOptions, callback: AsyncCallback<boolean>): void--><!--Device-call-function dial(phoneNumber: string, options: DialOptions, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| options | [DialOptions](arkts-telephony-call-dialoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dialOptions: call.DialOptions = {
    extras: false
}
call.dial("138xxxxxxxx", dialOptions, (err: BusinessError, data: boolean) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## dial

```TypeScript
function dial(phoneNumber: string, options?: DialOptions): Promise<boolean>
```

Makes a call.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialCall)

**Required permissions:** ohos.permission.PLACE_CALL

<!--Device-call-function dial(phoneNumber: string, options?: DialOptions): Promise<boolean>--><!--Device-call-function dial(phoneNumber: string, options?: DialOptions): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| options | [DialOptions](arkts-telephony-call-dialoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let dialOptions: call.DialOptions = {
    extras: false
}
call.dial("138xxxxxxxx", dialOptions).then((data: boolean) => {
    console.info(`dial success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`dial fail, promise: err->${JSON.stringify(err)}`);
});
```


## dial

```TypeScript
function dial(phoneNumber: string, callback: AsyncCallback<boolean>): void
```

Makes a call.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialCall)

**Required permissions:** ohos.permission.PLACE_CALL

<!--Device-call-function dial(phoneNumber: string, callback: AsyncCallback<boolean>): void--><!--Device-call-function dial(phoneNumber: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.dial("138xxxxxxxx", (err: BusinessError, data: boolean) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```
