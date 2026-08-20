# onAppForegroundStateChange (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## onAppForegroundStateChange

```TypeScript
function onAppForegroundStateChange(observer: AppForegroundStateObserver): void
```

Register app foreground or background state observer.

**Since:** 23

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onAppForegroundStateChange(observer: AppForegroundStateObserver): void--><!--Device-appManager-function onAppForegroundStateChange(observer: AppForegroundStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | AppForegroundStateObserver | Yes | The app foreground state observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

