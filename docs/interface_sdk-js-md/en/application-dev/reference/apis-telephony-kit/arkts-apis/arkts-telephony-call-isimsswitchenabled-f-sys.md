# isImsSwitchEnabled (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## isImsSwitchEnabled

```TypeScript
function isImsSwitchEnabled(slotId: int, callback: AsyncCallback<boolean>): void
```

Checks whether the IMS service is enabled. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-call-function isImsSwitchEnabled(slotId: int, callback: AsyncCallback<boolean>): void--><!--Device-call-function isImsSwitchEnabled(slotId: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Card slot ID. &lt;br&gt;- **0**: card slot 1. &lt;br&gt;- **1**: card slot 2. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** indicates that the IMS service is enabled, and the value **false** indicates the opposite. The value **true** indicates that the IMS service is enabled, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.isImsSwitchEnabled(0, (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isImsSwitchEnabled fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`isImsSwitchEnabled success, data->${JSON.stringify(data)}`);
    }
});
```


## isImsSwitchEnabled

```TypeScript
function isImsSwitchEnabled(slotId: int): Promise<boolean>
```

Checks whether the IMS service is enabled. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-call-function isImsSwitchEnabled(slotId: int): Promise<boolean>--><!--Device-call-function isImsSwitchEnabled(slotId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Card slot ID. &lt;br&gt;- **0**: card slot 1. &lt;br&gt;- **1**: card slot 2. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the IMS service is enabled, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.isImsSwitchEnabled(0).then((data: boolean) => {
    console.info(`isImsSwitchEnabled success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isImsSwitchEnabled fail, promise: err->${JSON.stringify(err)}`);
});
```

