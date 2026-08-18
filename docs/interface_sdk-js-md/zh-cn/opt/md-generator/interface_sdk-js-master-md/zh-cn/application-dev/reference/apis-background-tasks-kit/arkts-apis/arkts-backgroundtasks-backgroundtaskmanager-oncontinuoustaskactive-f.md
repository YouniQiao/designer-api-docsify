# onContinuousTaskActive

## 导入模块

```TypeScript
```

## onContinuousTaskActive

```TypeScript
function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void
```

注册长时任务激活的监听，使用callback异步回调。应用回前台激活暂停的长时任务。

**起始版本：** 23

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void--><!--Device-backgroundTaskManager-function onContinuousTaskActive(callback: Callback<ContinuousTaskActiveInfo>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinuousTaskActiveInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskactiveinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9800005](../../apis-backgroundtasks-kit/errorcode-backgroundTaskMgr.md#9800005-长时任务校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
