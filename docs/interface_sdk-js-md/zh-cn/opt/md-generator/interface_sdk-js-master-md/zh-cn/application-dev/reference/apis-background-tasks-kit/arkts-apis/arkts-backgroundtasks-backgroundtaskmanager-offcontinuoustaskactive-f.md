# offContinuousTaskActive

## 导入模块

```TypeScript
```

## offContinuousTaskActive

```TypeScript
function offContinuousTaskActive(callback?: Callback<ContinuousTaskActiveInfo>): void
```

取消长时任务激活的监听，使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function offContinuousTaskActive(callback?: Callback<ContinuousTaskActiveInfo>): void--><!--Device-backgroundTaskManager-function offContinuousTaskActive(callback?: Callback<ContinuousTaskActiveInfo>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinuousTaskActiveInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskactiveinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [9800005](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
