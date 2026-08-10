# onAppForegroundStateChange（系统接口）

## 导入模块

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## onAppForegroundStateChange

```TypeScript
function onAppForegroundStateChange(observer: AppForegroundStateObserver): void
```

注册应用启动和退出的监听器，可用于系统应用监听所有应用的启动和退出。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onAppForegroundStateChange(observer: AppForegroundStateObserver): void--><!--Device-appManager-function onAppForegroundStateChange(observer: AppForegroundStateObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observer | [AppForegroundStateObserver](arkts-ability-appforegroundstateobserver-i-sys.md) | 是 | 应用状态监听器，用于监听应用的启动和退出。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |

