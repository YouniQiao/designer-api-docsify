# getCallRestrictionStatus (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## getCallRestrictionStatus

```TypeScript
function getCallRestrictionStatus(slotId: number, type: CallRestrictionType, callback: AsyncCallback<RestrictionStatus>): void
```

Obtains the call restriction status. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getCallRestrictionStatus(slotId: int, type: CallRestrictionType, callback: AsyncCallback<RestrictionStatus>): void--><!--Device-call-function getCallRestrictionStatus(slotId: int, type: CallRestrictionType, callback: AsyncCallback<RestrictionStatus>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| type | [CallRestrictionType](arkts-telephony-call-callrestrictiontype-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RestrictionStatus](arkts-telephony-call-restrictionstatus-e-sys.md)&gt; | Yes |

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

call.getCallRestrictionStatus(0, 1, (err: BusinessError, data: call.RestrictionStatus) => {
    if (err) {
        console.error(`getCallRestrictionStatus fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`getCallRestrictionStatus success, data->${JSON.stringify(data)}`);
    }
});
```


## getCallRestrictionStatus

```TypeScript
function getCallRestrictionStatus(slotId: number, type: CallRestrictionType): Promise<RestrictionStatus>
```

Obtains the call restriction status. This API uses a promise to return the result.

**Since:** 8

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getCallRestrictionStatus(slotId: int, type: CallRestrictionType): Promise<RestrictionStatus>--><!--Device-call-function getCallRestrictionStatus(slotId: int, type: CallRestrictionType): Promise<RestrictionStatus>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| type | [CallRestrictionType](arkts-telephony-call-callrestrictiontype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[RestrictionStatus](arkts-telephony-call-restrictionstatus-e-sys.md)&gt; |

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

call.getCallRestrictionStatus(0, 1).then((data: call.RestrictionStatus) => {
    console.info(`getCallRestrictionStatus success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getCallRestrictionStatus fail, promise: err->${JSON.stringify(err)}`);
});
```
