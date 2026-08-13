# onApplicationStateChange

## onApplicationStateChange

```TypeScript
function onApplicationStateChange(observer: ApplicationStateObserver): number
```

注册所有应用程序的状态监听器。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver): int--><!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver): int-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [ApplicationStateObserver](arkts-ability-applicationstateobserver-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |


## onApplicationStateChange

```TypeScript
function onApplicationStateChange(observer: ApplicationStateObserver, bundleNameList: Array<string>): number
```

注册指定应用程序的状态监听器。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, bundleNameList: Array<string>): int--><!--Device-appManager-function onApplicationStateChange(observer: ApplicationStateObserver, bundleNameList: Array<string>): int-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [ApplicationStateObserver](arkts-ability-applicationstateobserver-c.md) | 是 |
| bundleNameList | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
