# getTaskInfo

## 导入模块

```TypeScript
import { backgroundLoader } from 'kits/@kit.BackgroundTasksKit';
```

## getTaskInfo

```TypeScript
function getTaskInfo(taskId: number): Promise<TaskInfo>
```

获取后台预取任务信息。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| taskId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;TaskInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9700003](../errorcode-workScheduler.md#9700003-系统服务失败) |
| [9700004](../errorcode-workScheduler.md#9700004-参数校验失败) |
