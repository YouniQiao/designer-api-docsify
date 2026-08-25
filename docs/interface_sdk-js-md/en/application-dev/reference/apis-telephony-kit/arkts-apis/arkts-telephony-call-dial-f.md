# dial

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## dial

```TypeScript
function dial(phoneNumber: string, options: DialOptions, callback: AsyncCallback<boolean>): void
```

Initiates a call. You can set call options as needed. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 6 and deprecated since API version 9. The substitute API is available
> only for system applications.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [dialCall](arkts-telephony-call-dialcall-f-sys.md)

**Required permissions:** ohos.permission.PLACE_CALL

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| options | [DialOptions](arkts-telephony-call-dialoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## dial

```TypeScript
function dial(phoneNumber: string, options?: DialOptions): Promise<boolean>
```

Initiates a call. You can set call options as needed. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 6 and deprecated since API version 9. The substitute API is available
> only for system applications.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [dialCall](arkts-telephony-call-dialcall-f-sys.md)

**Required permissions:** ohos.permission.PLACE_CALL

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


## dial

```TypeScript
function dial(phoneNumber: string, callback: AsyncCallback<boolean>): void
```

Initiates a call. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 6 and deprecated since API version 9. The substitute API is available
> only for system applications.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [dialCall](arkts-telephony-call-dialcall-f-sys.md)

**Required permissions:** ohos.permission.PLACE_CALL

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |
