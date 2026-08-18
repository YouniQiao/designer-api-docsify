# onNotifyVisible（系统接口）

## 导入模块

```TypeScript
```

## onNotifyVisible

```TypeScript
function onNotifyVisible(observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void
```

Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change.&lt;/p&gt;

**起始版本：** 23

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function onNotifyVisible(observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void--><!--Device-formObserver-function onNotifyVisible(observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| observerCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## onNotifyVisible

```TypeScript
function onNotifyVisible(
    hostBundleName: string,
    observerCallback: Callback<Array<formInfo.RunningFormInfo>>
  ): void
```

Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change for a particular card host.&lt;/p&gt;

**起始版本：** 23

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function onNotifyVisible(    hostBundleName: string,    observerCallback: Callback<Array<formInfo.RunningFormInfo>>  ): void--><!--Device-formObserver-function onNotifyVisible(    hostBundleName: string,    observerCallback: Callback<Array<formInfo.RunningFormInfo>>  ): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | 是 |
| observerCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
