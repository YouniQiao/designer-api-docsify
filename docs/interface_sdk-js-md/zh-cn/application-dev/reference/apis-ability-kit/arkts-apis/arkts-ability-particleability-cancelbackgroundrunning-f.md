# cancelBackgroundRunning

## 导入模块

```TypeScript
import { particleAbility } from 'kits/@kit.AbilityKit';
```

## cancelBackgroundRunning

```TypeScript
function cancelBackgroundRunning(callback: AsyncCallback<void>): void
```

向系统申请取消长时任务。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [stopBackgroundRunning](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-f.md)

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## cancelBackgroundRunning

```TypeScript
function cancelBackgroundRunning(): Promise<void>
```

向系统申请取消长时任务。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [stopBackgroundRunning](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-f.md)

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
