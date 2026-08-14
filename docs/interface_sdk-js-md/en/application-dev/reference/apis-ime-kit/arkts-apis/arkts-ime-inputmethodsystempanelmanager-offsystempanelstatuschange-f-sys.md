# offSystemPanelStatusChange (System API)

## Modules to Import

```TypeScript
import { inputMethodSystemPanelManager } from 'inputMethodSystemPanelManager';
```

## offSystemPanelStatusChange

```TypeScript
function offSystemPanelStatusChange(callback?: Callback<SystemPanelStatus>): void
```

Unsubscribe from the system panel status change event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodSystemPanelManager-function offSystemPanelStatusChange(callback?: Callback<SystemPanelStatus>): void--><!--Device-inputMethodSystemPanelManager-function offSystemPanelStatusChange(callback?: Callback<SystemPanelStatus>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SystemPanelStatus](arkts-ime-inputmethodsystempanelmanager-systempanelstatus-i-sys.md)&gt; | No | callback triggered when the system panel status changes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | not system application. |

