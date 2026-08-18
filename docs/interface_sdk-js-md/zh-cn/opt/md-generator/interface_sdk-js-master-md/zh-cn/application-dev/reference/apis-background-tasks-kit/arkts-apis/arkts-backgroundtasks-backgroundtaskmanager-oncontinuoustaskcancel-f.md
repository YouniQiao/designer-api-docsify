# onContinuousTaskCancel

## 导入模块

```TypeScript
```

## onContinuousTaskCancel

```TypeScript
function onContinuousTaskCancel(callback: Callback<ContinuousTaskCancelInfo>): void
```

注册长时任务取消的监听，使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function onContinuousTaskCancel(callback: Callback<ContinuousTaskCancelInfo>): void--><!--Device-backgroundTaskManager-function onContinuousTaskCancel(callback: Callback<ContinuousTaskCancelInfo>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinuousTaskCancelInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskcancelinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
