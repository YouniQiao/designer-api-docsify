# setSeniorModeStateForApp (System API)

## Modules to Import

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## setSeniorModeStateForApp

```TypeScript
function setSeniorModeStateForApp(appSeniorModeInfos: Array<AppSeniorModeInfo>): Promise<void>
```

Set the senior mode state for app.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-config-function setSeniorModeStateForApp(appSeniorModeInfos: Array<AppSeniorModeInfo>): Promise<void>--><!--Device-config-function setSeniorModeStateForApp(appSeniorModeInfos: Array<AppSeniorModeInfo>): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appSeniorModeInfos | Array&lt;[AppSeniorModeInfo](arkts-accessibility-config-appseniormodeinfo-i-sys.md)&gt; | Yes | Indicates the list of app package names and statuses for which the advanced mode needs to be set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9300008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300008-app-clone-index-invalid) | The appIndex is invalid. Possible causes: &lt;br&gt;1.The appIndex is out of the valid range. &lt;br&gt;2.The application corresponding to the appIndex does not exist. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. &lt;br&gt;The application does not have the permission required to call the API. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. &lt;br&gt;A non-system application calls a system API. |
| [9300000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300000-accessibility-system-service-abnormal) | System abnormality. |

