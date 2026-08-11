# setCallRestrictionPassword (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## setCallRestrictionPassword

```TypeScript
function setCallRestrictionPassword(slotId: number, oldPassword: string, newPassword: string, callback: AsyncCallback<void>): void
```

Set call barring password.

**Since:** 10

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setCallRestrictionPassword(slotId: int, oldPassword: string, newPassword: string, callback: AsyncCallback<void>): void--><!--Device-call-function setCallRestrictionPassword(slotId: int, oldPassword: string, newPassword: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| oldPassword | string | Yes |
| newPassword | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.setCallRestrictionPassword(0, "123456", "654321", (err: BusinessError) => {
    if (err) {
        console.error(`setCallRestrictionPassword fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`setCallRestrictionPassword success.`);
    }
});
```


## setCallRestrictionPassword

```TypeScript
function setCallRestrictionPassword(slotId: number, oldPassword: string, newPassword: string): Promise<void>
```

Set call barring password.

**Since:** 10

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setCallRestrictionPassword(slotId: int, oldPassword: string, newPassword: string): Promise<void>--><!--Device-call-function setCallRestrictionPassword(slotId: int, oldPassword: string, newPassword: string): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| oldPassword | string | Yes |
| newPassword | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.setCallRestrictionPassword(0, "123456", "654321").then(() => {
    console.info(`setCallRestrictionPassword success.`);
}).catch((err: BusinessError) => {
    console.error(`setCallRestrictionPassword fail, promise: err->${JSON.stringify(err)}`);
});
```
