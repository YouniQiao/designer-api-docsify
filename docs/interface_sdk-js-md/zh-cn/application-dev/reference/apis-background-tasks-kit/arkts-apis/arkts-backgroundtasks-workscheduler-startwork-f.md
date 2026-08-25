# startWork

## 导入模块

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## startWork

```TypeScript
function startWork(work: WorkInfo): void
```

申请延迟任务，成功后会把任务添加到执行队列，满足触发条件后由系统调度执行。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| work | [WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9700001](../errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../errorcode-workScheduler.md#9700003-系统服务失败) |
| [9700004](../errorcode-workScheduler.md#9700004-参数校验失败) |
| [9700005](../errorcode-workScheduler.md#9700005-startwork失败) |
