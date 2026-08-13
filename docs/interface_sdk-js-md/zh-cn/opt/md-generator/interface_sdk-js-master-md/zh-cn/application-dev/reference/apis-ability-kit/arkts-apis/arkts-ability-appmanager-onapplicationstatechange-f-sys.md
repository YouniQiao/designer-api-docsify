# onApplicationStateChange（系统接口）

## onApplicationStateChange

```TypeScript
function onApplicationStateChange(observer: ApplicationStateObserver, filter: AppStateFilter): number
```

注册应用程序的状态监听器，并通过设置过滤条件来筛选所需监听的应用生命周期变化事件。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, filter: AppStateFilter): int--><!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, filter: AppStateFilter): int-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [ApplicationStateObserver](arkts-ability-applicationstateobserver-c.md) | 是 |
| filter | [AppStateFilter](arkts-ability-appmanager-appstatefilter-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
