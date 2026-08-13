# setCallRestriction (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## setCallRestriction

```TypeScript
function setCallRestriction(slotId: int, info: CallRestrictionInfo, callback: AsyncCallback<void>): void
```

Sets the call restriction status. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setCallRestriction(slotId: int, info: CallRestrictionInfo, callback: AsyncCallback<void>): void--><!--Device-call-function setCallRestriction(slotId: int, info: CallRestrictionInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Card slot ID. &lt;br&gt;- **0**: card slot 1. &lt;br&gt;- **1**: card slot 2. |
| info | [CallRestrictionInfo](arkts-telephony-call-callrestrictioninfo-i-sys.md) | Yes | Call restriction information. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

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
function setCallRestriction(slotId: int, info: CallRestrictionInfo): Promise<void>
```

Sets the call restriction status. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setCallRestriction(slotId: int, info: CallRestrictionInfo): Promise<void>--><!--Device-call-function setCallRestriction(slotId: int, info: CallRestrictionInfo): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Card slot ID. &lt;br&gt;- **0**: card slot 1. &lt;br&gt;- **1**: card slot 2. |
| info | [CallRestrictionInfo](arkts-telephony-call-callrestrictioninfo-i-sys.md) | Yes | Call restriction information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

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

