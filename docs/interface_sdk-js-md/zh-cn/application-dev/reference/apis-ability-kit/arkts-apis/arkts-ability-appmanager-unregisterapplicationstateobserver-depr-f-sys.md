# unregisterApplicationStateObserver（系统接口）

## 导入模块

```TypeScript
```

## unregisterApplicationStateObserver

```TypeScript
function unregisterApplicationStateObserver(observerId: number, callback: AsyncCallback<void>): void
```

取消注册应用程序状态观测器。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-ability-appmanager-off-f.md#offapplicationstate)

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| observerId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## unregisterApplicationStateObserver

```TypeScript
function unregisterApplicationStateObserver(observerId: number): Promise<void>
```

取消注册应用程序状态观测器。使用Promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](arkts-ability-appmanager-off-f.md#offapplicationstate)

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| observerId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
