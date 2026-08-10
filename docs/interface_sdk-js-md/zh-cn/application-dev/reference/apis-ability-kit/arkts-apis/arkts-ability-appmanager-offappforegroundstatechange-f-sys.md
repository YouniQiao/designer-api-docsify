# offAppForegroundStateChange（系统接口）

## 导入模块

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## offAppForegroundStateChange

```TypeScript
function offAppForegroundStateChange(observer?: AppForegroundStateObserver): void
```

注销应用启动和退出的监听器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function offAppForegroundStateChange(observer?: AppForegroundStateObserver): void--><!--Device-appManager-function offAppForegroundStateChange(observer?: AppForegroundStateObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observer | [AppForegroundStateObserver](arkts-ability-appforegroundstateobserver-i-sys.md) | 否 | 取消注册的应用启动和退出监听器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |
| 201 | Permission denied. |
| 202 | Not system application. |

