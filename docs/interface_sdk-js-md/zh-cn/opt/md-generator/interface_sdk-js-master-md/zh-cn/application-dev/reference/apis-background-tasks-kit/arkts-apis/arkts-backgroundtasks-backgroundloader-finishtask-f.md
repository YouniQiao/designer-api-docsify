# finishTask

## 导入模块

```TypeScript
```

## finishTask

```TypeScript
function finishTask(taskInfo: TaskInfo): void
```

结束后台加载任务。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-backgroundLoader-function finishTask(taskInfo: TaskInfo): void--><!--Device-backgroundLoader-function finishTask(taskInfo: TaskInfo): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [taskInfo](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-cloudmediaassetstatus-i-sys.md) | [TaskInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-taskinfo-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9700004](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700004-workinfo校验失败) |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-系统服务失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
