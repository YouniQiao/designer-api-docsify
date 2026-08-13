# controlCamera (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## controlCamera

```TypeScript
function controlCamera(callId: int, cameraId: string): Promise<void>
```

Uses the specified camera to make a video call. If **cameraId** is left empty, the camera is disabled. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function controlCamera(callId: int, cameraId: string): Promise<void>--><!--Device-call-function controlCamera(callId: int, cameraId: string): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Call ID. You can obtain the value by subscribing to **callDetailsChange** events. |
| cameraId | string | Yes | Camera ID. For details about how to obtain the camera ID, see the [getSupportedCameras](../../apis-camera-kit/arkts-apis/arkts-camera-camera-cameramanager-i.md#getSupportedCameras) API in camera management. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result of starting, closing, or switching a camera. |

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

call.controlCamera(1, "1").then(() => {
    console.info(`controlCamera success.`);
}).catch((err: BusinessError) => {
    console.error(`controlCamera fail, promise: err->${JSON.stringify(err)}`);
});
```

