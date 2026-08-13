# getAllSimMessages (System API)

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## getAllSimMessages

```TypeScript
function getAllSimMessages(slotId: int, callback: AsyncCallback<Array<SimShortMessage>>): void
```

Obtains all SIM card messages. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.RECEIVE_SMS

<!--Device-sms-function getAllSimMessages(slotId: int, callback: AsyncCallback<Array<SimShortMessage>>): void--><!--Device-sms-function getAllSimMessages(slotId: int, callback: AsyncCallback<Array<SimShortMessage>>): void-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | SIM card slot ID. &lt;br&gt;- **0**: card slot 1 &lt;br&gt;- **1**: card slot 2 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;[SimShortMessage](arkts-telephony-sms-simshortmessage-i-sys.md)&gt;&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
sms.getAllSimMessages(slotId, (err: BusinessError, data: sms.SimShortMessage[]) => {
      console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getAllSimMessages

```TypeScript
function getAllSimMessages(slotId: int): Promise<Array<SimShortMessage>>
```

Obtains all SIM card messages. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.RECEIVE_SMS

<!--Device-sms-function getAllSimMessages(slotId: int): Promise<Array<SimShortMessage>>--><!--Device-sms-function getAllSimMessages(slotId: int): Promise<Array<SimShortMessage>>-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | SIM card slot ID. &lt;br&gt;- **0**: card slot 1 &lt;br&gt;- **1**: card slot 2 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[SimShortMessage](arkts-telephony-sms-simshortmessage-i-sys.md)&gt;&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
let promise = sms.getAllSimMessages(slotId);
promise.then((data: sms.SimShortMessage[]) => {
    console.info(`getAllSimMessages success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getAllSimMessages failed, promise: err->${JSON.stringify(err)}`);
});
```

