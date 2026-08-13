# onSeniorModeStateChangeForApp (System API)

## Modules to Import

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## onSeniorModeStateChangeForApp

```TypeScript
function onSeniorModeStateChangeForApp(callback: Callback<AppSeniorModeInfo>): void
```

Register an observer for anyone application's senior mode state changes.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_ACCESSIBILITY_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-config-function onSeniorModeStateChangeForApp(callback: Callback<AppSeniorModeInfo>): void--><!--Device-config-function onSeniorModeStateChangeForApp(callback: Callback<AppSeniorModeInfo>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AppSeniorModeInfo](arkts-accessibility-config-appseniormodeinfo-i-sys.md)&gt; | Yes | Asynchronous callback interface. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. &lt;br&gt;The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. &lt;br&gt;A non-system application calls a system API. |

