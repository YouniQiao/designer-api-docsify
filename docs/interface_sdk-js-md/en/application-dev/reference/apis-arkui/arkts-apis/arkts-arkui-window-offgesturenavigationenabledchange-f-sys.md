# offGestureNavigationEnabledChange (System API)

## Modules to Import

```TypeScript
import { window } from 'window';
```

## offGestureNavigationEnabledChange

```TypeScript
function offGestureNavigationEnabledChange(callback?: Callback<boolean>): void
```

Unsubscribes from the gesture navigation status change event.

**Since:** 23

<!--Device-window-function offGestureNavigationEnabledChange(callback?: Callback<boolean>): void--><!--Device-window-function offGestureNavigationEnabledChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | No | Callback function that has been used for the subscription. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event are canceled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

