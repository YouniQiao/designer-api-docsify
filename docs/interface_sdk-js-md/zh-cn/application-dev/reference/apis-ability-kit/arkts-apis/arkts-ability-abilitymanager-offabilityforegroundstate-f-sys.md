# offAbilityForegroundState（系统接口）

## 导入模块

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## offAbilityForegroundState

```TypeScript
function offAbilityForegroundState(observer?: AbilityForegroundStateObserver): void
```

取消注册Ability启动和退出的观测器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-abilityManager-function offAbilityForegroundState(observer?: AbilityForegroundStateObserver): void--><!--Device-abilityManager-function offAbilityForegroundState(observer?: AbilityForegroundStateObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observer | [AbilityForegroundStateObserver](arkts-ability-abilitymanager-abilityforegroundstateobserver-t-sys.md) | 否 | Ability状态观测器，用于观测Ability的启动和退出。如果未配置该参数，则取消当前应用注册的所有observer。如果配置 了该参数，则取消该observer。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Connect to system server failed. |
| 201 | Permission denied. |
| 202 | Not system application. |

