# offAbilityFirstFrameStateChange (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## offAbilityFirstFrameStateChange

```TypeScript
function offAbilityFirstFrameStateChange(observer?: AbilityFirstFrameStateObserver): void
```

取消注册监听Ability首帧绘制完成事件观察者对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offAbilityFirstFrameStateChange(observer?: AbilityFirstFrameStateObserver): void--><!--Device-appManager-function offAbilityFirstFrameStateChange(observer?: AbilityFirstFrameStateObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [AbilityFirstFrameStateObserver](arkts-ability-appmanager-abilityfirstframestateobserver-t-sys.md) | No | 表示待取消的Ability首帧绘制完成事件观察者对象，不填表示取消所有监听对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |

