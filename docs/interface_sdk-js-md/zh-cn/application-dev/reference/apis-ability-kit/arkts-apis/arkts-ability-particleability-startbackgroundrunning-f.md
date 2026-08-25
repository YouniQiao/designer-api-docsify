# startBackgroundRunning

## 导入模块

```TypeScript
import { particleAbility } from 'kits/@kit.AbilityKit';
```

## startBackgroundRunning

```TypeScript
function startBackgroundRunning(id: number, request: NotificationRequest, callback: AsyncCallback<void>): void
```

向系统申请长时任务。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [startBackgroundRunning](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md)

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| request | [NotificationRequest](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationrequest-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(id: number, request: NotificationRequest): Promise<void>
```

向系统申请长时任务。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [startBackgroundRunning](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md)

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| request | [NotificationRequest](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationrequest-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
