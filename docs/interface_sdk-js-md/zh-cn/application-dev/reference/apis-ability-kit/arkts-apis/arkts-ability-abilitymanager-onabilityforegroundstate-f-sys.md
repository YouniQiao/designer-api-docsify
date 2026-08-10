# onAbilityForegroundState（系统接口）

## 导入模块

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## onAbilityForegroundState

```TypeScript
function onAbilityForegroundState(observer: AbilityForegroundStateObserver): void
```

注册Ability的启动和退出的观测器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-abilityManager-function onAbilityForegroundState(observer: AbilityForegroundStateObserver): void--><!--Device-abilityManager-function onAbilityForegroundState(observer: AbilityForegroundStateObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observer | [AbilityForegroundStateObserver](arkts-ability-abilitymanager-abilityforegroundstateobserver-t-sys.md) | 是 | Ability状态观测器，用于观测Ability的启动和退出。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Connect to system server failed. |
| 201 | Permission denied. |
| 202 | Not system application. |

