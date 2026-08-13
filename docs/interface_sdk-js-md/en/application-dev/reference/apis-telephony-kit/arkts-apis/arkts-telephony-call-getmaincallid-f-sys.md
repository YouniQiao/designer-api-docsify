# getMainCallId (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## getMainCallId

```TypeScript
function getMainCallId(callId: int, callback: AsyncCallback<int>): void
```

Obtains the main call ID. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-call-function getMainCallId(callId: int, callback: AsyncCallback<int>): void--><!--Device-call-function getMainCallId(callId: int, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Call ID. |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;int&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getMainCallId(1, (err: BusinessError, data: number) => {
    if (err) {
        console.error(`getMainCallId fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`getMainCallId success, data->${JSON.stringify(data)}`);
    }
});
```


## getMainCallId

```TypeScript
function getMainCallId(callId: int): Promise<int>
```

Obtains the main call ID. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-call-function getMainCallId(callId: int): Promise<int>--><!--Device-call-function getMainCallId(callId: int): Promise<int>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Call ID. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getMainCallId(1).then((data: number) => {
    console.info(`getMainCallId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getMainCallId fail, promise: err->${JSON.stringify(err)}`);
});
```

