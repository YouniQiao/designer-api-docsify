# onAbilityForegroundState (System API)

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## onAbilityForegroundState

```TypeScript
function onAbilityForegroundState(observer: AbilityForegroundStateObserver): void
```

注册Ability的启动和退出的观测器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-abilityManager-function onAbilityForegroundState(observer: AbilityForegroundStateObserver): void--><!--Device-abilityManager-function onAbilityForegroundState(observer: AbilityForegroundStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [AbilityForegroundStateObserver](arkts-ability-abilitymanager-abilityforegroundstateobserver-t-sys.md) | Yes | Ability状态观测器，用于观测Ability的启动和退出。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Connect to system server failed. |
| 201 | Permission denied. |
| 202 | Not system application. |

