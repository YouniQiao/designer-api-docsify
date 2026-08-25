# stopAndClearWorks

## 导入模块

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## stopAndClearWorks

```TypeScript
function stopAndClearWorks(): void
```

停止和取消当前应用所有的延迟任务。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9700001](../errorcode-workScheduler.md#9700001-内存操作失败) |
| [9700002](../errorcode-workScheduler.md#9700002-parcel读写操作失败) |
| [9700003](../errorcode-workScheduler.md#9700003-系统服务失败) |
