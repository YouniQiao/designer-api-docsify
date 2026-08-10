# unregisterTask

## 导入模块

```TypeScript
import { backgroundLoader } from 'kits/@kit.BackgroundTasksKit';
```

## unregisterTask

```TypeScript
function unregisterTask(taskInfo: TaskInfo): void
```

取消注册后台加载任务。

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-backgroundLoader-function unregisterTask(taskInfo: TaskInfo): void--><!--Device-backgroundLoader-function unregisterTask(taskInfo: TaskInfo): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskInfo | [TaskInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-taskinfo-i.md) | 是 |  |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 9700004 | Check on taskInfo failed. |
| 9700003 | System service operation failed. |
| 201 | Permission denied. |

