# offAppForegroundStateChange (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## offAppForegroundStateChange

```TypeScript
function offAppForegroundStateChange(observer?: AppForegroundStateObserver): void
```

注销应用启动和退出的监听器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offAppForegroundStateChange(observer?: AppForegroundStateObserver): void--><!--Device-appManager-function offAppForegroundStateChange(observer?: AppForegroundStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [AppForegroundStateObserver](arkts-ability-appforegroundstateobserver-i-sys.md) | No | 取消注册的应用启动和退出监听器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |

