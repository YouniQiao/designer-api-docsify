# getSeniorModeStateForApp (System API)

## Modules to Import

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## getSeniorModeStateForApp

```TypeScript
function getSeniorModeStateForApp(bundleName: string, appIndex?: int): Promise<boolean>
```

Get the senior mode state for app.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.READ_ACCESSIBILITY_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-config-function getSeniorModeStateForApp(bundleName: string, appIndex?: int): Promise<boolean>--><!--Device-config-function getSeniorModeStateForApp(bundleName: string, appIndex?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Indicates the bundle name of the application to be queried &lt;br&gt;The bundle name must follow the reverse domain naming convention (e.g., "com.example.app"). |
| appIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | Indicates the index of clone app. &lt;br&gt;The value must be an integer greater than or equal to 0. Default value: 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9300008](../errorcode-accessibility.md#9300008-app-clone-index-invalid) | The appIndex is invalid. Possible causes: &lt;br&gt;1.The appIndex is out of the valid range. &lt;br&gt;2.The application corresponding to the appIndex does not exist. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. &lt;br&gt;The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. &lt;br&gt;A non-system application calls a system API. |
| [9300000](../errorcode-accessibility.md#9300000-accessibility-system-service-abnormal) | System abnormality. |

