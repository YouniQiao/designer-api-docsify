# postDialProceed (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## postDialProceed

```TypeScript
function postDialProceed(callId: int, proceed: boolean, callback: AsyncCallback<void>): void
```

Continues a call by playing a post-dial DTMF string. This API uses an asynchronous callback to return the result.

If the called number is in the format of "common phone number + semicolon (;) + DTMF string", for example,  
**400xxxxxxx;123**, and the listening for **postDialDelay** events is enabled, the system reports a  
**postDialDelay** event when the call is connected. The application can then call this API to send DTMF tones.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function postDialProceed(callId: int, proceed: boolean, callback: AsyncCallback<void>): void--><!--Device-call-function postDialProceed(callId: int, proceed: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Call ID. |
| proceed | boolean | Yes | Whether to send DTMF tones. The default value is **false**. &lt;br&gt;- **true**: yes &lt;br&gt;- **false**: no |
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

call.postDialProceed(1, true, (err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## postDialProceed

```TypeScript
function postDialProceed(callId: int, proceed: boolean): Promise<void>
```

Continues a call by playing a post-dial DTMF string. This API uses a promise to return the result.

If the called number is in the format of "common phone number + semicolon (;) + DTMF string", for example,  
**400xxxxxxx;123**, and the listening for **postDialDelay** events is enabled, the system reports a  
**postDialDelay** event when the call is connected. The application can then call this API to send DTMF tones.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function postDialProceed(callId: int, proceed: boolean): Promise<void>--><!--Device-call-function postDialProceed(callId: int, proceed: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Call ID. |
| proceed | boolean | Yes | Whether to send DTMF tones. The default value is **false**. &lt;br&gt;- **true**: yes &lt;br&gt;- **false**: no |

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

call.postDialProceed(1, true).then(() => {
    console.info(`postDialProceed success.`);
}).catch((err: BusinessError) => {
    console.error(`postDialProceed fail, promise: err->${JSON.stringify(err)}`);
});
```

