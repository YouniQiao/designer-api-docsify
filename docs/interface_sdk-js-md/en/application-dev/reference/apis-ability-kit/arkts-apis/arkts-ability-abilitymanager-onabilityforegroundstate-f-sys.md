# onAbilityForegroundState (System API)

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## onAbilityForegroundState

```TypeScript
function onAbilityForegroundState(observer: AbilityForegroundStateObserver): void
```

Register Ability foreground or background state observer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-abilityManager-function onAbilityForegroundState(observer: AbilityForegroundStateObserver): void--><!--Device-abilityManager-function onAbilityForegroundState(observer: AbilityForegroundStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [AbilityForegroundStateObserver](arkts-ability-abilitymanager-abilityforegroundstateobserver-t-sys.md) | Yes | The ability foreground state observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Connect to system server failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |

