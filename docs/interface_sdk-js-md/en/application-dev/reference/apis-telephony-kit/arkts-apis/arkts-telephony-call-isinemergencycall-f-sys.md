# isInEmergencyCall (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## isInEmergencyCall

```TypeScript
function isInEmergencyCall(callback: AsyncCallback<boolean>): void
```

Checks whether a call is an emergency call. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function isInEmergencyCall(callback: AsyncCallback<boolean>): void--><!--Device-call-function isInEmergencyCall(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback function used to return the result. The value **true** indicates an emergency call, and the value **false** indicates a non-emergency call. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.isInEmergencyCall((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isInEmergencyCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`isInEmergencyCall success, data->${JSON.stringify(data)}`);
    }
});
```


## isInEmergencyCall

```TypeScript
function isInEmergencyCall(): Promise<boolean>
```

Checks whether a call is an emergency call. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function isInEmergencyCall(): Promise<boolean>--><!--Device-call-function isInEmergencyCall(): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates an emergency call, and the value false indicates a non-emergency call. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.isInEmergencyCall().then((data: boolean) => {
    console.info(`isInEmergencyCall success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isInEmergencyCall fail, promise: err->${JSON.stringify(err)}`);
});
```

