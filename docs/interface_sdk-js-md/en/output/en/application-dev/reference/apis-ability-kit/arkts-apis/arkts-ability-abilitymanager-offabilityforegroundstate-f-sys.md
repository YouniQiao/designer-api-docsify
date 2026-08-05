# offAbilityForegroundState (System API)

## offAbilityForegroundState

```TypeScript
function offAbilityForegroundState(observer?: AbilityForegroundStateObserver): void
```

Unregister Ability foreground or background state observer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-abilityManager-function offAbilityForegroundState(observer?: AbilityForegroundStateObserver): void--><!--Device-abilityManager-function offAbilityForegroundState(observer?: AbilityForegroundStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The ability foreground state observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Connect to system server failed. |

