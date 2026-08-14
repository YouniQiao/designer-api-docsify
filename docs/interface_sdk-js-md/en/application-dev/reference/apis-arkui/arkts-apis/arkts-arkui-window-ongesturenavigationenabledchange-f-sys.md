# onGestureNavigationEnabledChange (System API)

## Modules to Import

```TypeScript
import { window } from 'window';
```

## onGestureNavigationEnabledChange

```TypeScript
function onGestureNavigationEnabledChange(callback: Callback<boolean>): void
```

Subscribes to the gesture navigation status change event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-window-function onGestureNavigationEnabledChange(callback: Callback<boolean>): void--><!--Device-window-function onGestureNavigationEnabledChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | Yes | Callback used to return the gesture navigation status. true if enabled, false otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

