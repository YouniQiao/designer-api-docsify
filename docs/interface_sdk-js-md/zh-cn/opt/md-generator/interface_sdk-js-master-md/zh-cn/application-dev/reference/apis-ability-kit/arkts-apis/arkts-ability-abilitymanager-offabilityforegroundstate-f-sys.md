# offAbilityForegroundState（系统接口）

## offAbilityForegroundState

```TypeScript
function offAbilityForegroundState(observer?: AbilityForegroundStateObserver): void
```

取消注册Ability启动和退出的观测器。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-abilityManager-function offAbilityForegroundState(observer?: AbilityForegroundStateObserver): void--><!--Device-abilityManager-function offAbilityForegroundState(observer?: AbilityForegroundStateObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [AbilityForegroundStateObserver](arkts-ability-abilitymanager-abilityforegroundstateobserver-t-sys.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
