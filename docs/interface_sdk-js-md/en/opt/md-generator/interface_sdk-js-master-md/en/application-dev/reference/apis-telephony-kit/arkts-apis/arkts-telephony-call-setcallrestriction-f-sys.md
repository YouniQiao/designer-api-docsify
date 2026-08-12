# setCallRestriction (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## setCallRestriction

```TypeScript
function setCallRestriction(slotId: number, info: CallRestrictionInfo, callback: AsyncCallback<void>): void
```

Set call barring status.

**Since:** 8

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setCallRestriction(slotId: int, info: CallRestrictionInfo, callback: AsyncCallback<void>): void--><!--Device-call-function setCallRestriction(slotId: int, info: CallRestrictionInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| info | [CallRestrictionInfo](arkts-telephony-call-callrestrictioninfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callRestrictionInfo: call.CallRestrictionInfo = {
    type: call.CallRestrictionType.RESTRICTION_TYPE_ALL_OUTGOING,
    password: "123456",
    mode: call.CallRestrictionMode.RESTRICTION_MODE_ACTIVATION
}
call.setCallRestriction(0, callRestrictionInfo, (err: BusinessError) => {
    if (err) {
        console.error(`setCallRestriction fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`setCallRestriction success.`);
    }
});
```


## setCallRestriction

```TypeScript
function setCallRestriction(slotId: number, info: CallRestrictionInfo): Promise<void>
```

Set call barring status.

**Since:** 8

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setCallRestriction(slotId: int, info: CallRestrictionInfo): Promise<void>--><!--Device-call-function setCallRestriction(slotId: int, info: CallRestrictionInfo): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| info | [CallRestrictionInfo](arkts-telephony-call-callrestrictioninfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callRestrictionInfo: call.CallRestrictionInfo = {
    type: call.CallRestrictionType.RESTRICTION_TYPE_ALL_INCOMING,
    password: "123456",
    mode: call.CallRestrictionMode.RESTRICTION_MODE_ACTIVATION
}
call.setCallRestriction(0, callRestrictionInfo).then(() => {
    console.info(`setCallRestriction success.`);
}).catch((err: BusinessError) => {
    console.error(`setCallRestriction fail, promise: err->${JSON.stringify(err)}`);
});
```
