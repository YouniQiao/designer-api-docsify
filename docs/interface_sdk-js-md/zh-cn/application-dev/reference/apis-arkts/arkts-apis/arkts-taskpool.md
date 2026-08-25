# @ohos.taskpool

任务池（taskpool）为应用程序提供多线程运行环境，降低资源消耗并提升系统性能，开发者无需关心线程的生命周期。 使用任务池API可创建后台任务（Task），执行或取消任务等操作。理论上，任务池API允许创建的任务数量不受限制，但由于内存限制， 不建议无限制地创建大量任务。此外，不建议在任务中执行阻塞操作，尤其是无限期阻塞操作，因为阻塞操作会占用工作线程，影响其他任务的调度和应用性能。 创建同一优先级的任务时，可以自行决定其执行顺序。任务的实际执行顺序与任务提交到任务池的顺序一致。任务的默认优先级为MEDIUM。 当同一时间待执行的任务数量大于任务池工作线程数量，任务池会根据负载均衡机制进行扩容，增加工作线程数量，减少整体等待时长。 同样，当执行的任务数量减少，工作线程数量大于执行任务数量，部分工作线程处于空闲状态，任务池会根据负载均衡机制进行缩容，减少工作线程数量。 任务池API返回错误码。如需了解各错误码的详细信息，请参阅文档[语言基础类库错误码](../errorcode-utils.md)。 请查阅[TaskPool注意事项](../../../arkts-utils/taskpool-introduction.md#taskpool注意事项)，了解使用TaskPool时的相关注意点。 文档中涉及以下任务概念：  
- 任务组任务：对应为[TaskGroup](arkts-arkts-taskpool-taskgroup-c.md)任务。  
- 串行队列任务：对应为[SequenceRunner](arkts-arkts-taskpool-sequencerunner-c.md)任务。  
- 异步队列任务：对应为[AsyncRunner](arkts-arkts-taskpool-asyncrunner-c.md)任务。  
- 周期任务：由[executePeriodically](arkts-arkts-taskpool-executeperiodically-f.md)执行的任务。

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## 汇总

### 函数

| 名称 |
| --- |
| [cancel](arkts-arkts-taskpool-cancel-f.md) |
| [cancel](arkts-arkts-taskpool-cancel-f.md) |
| [cancel](arkts-arkts-taskpool-cancel-f.md) |
| [execute](arkts-arkts-taskpool-execute-f.md) |
| [execute](arkts-arkts-taskpool-execute-f.md) |
| [execute](arkts-arkts-taskpool-execute-f.md) |
| [execute](arkts-arkts-taskpool-execute-f.md) |
| [execute](arkts-arkts-taskpool-execute-f.md) |
| [execute](arkts-arkts-taskpool-execute-f.md) |
| [execute](arkts-arkts-taskpool-execute-f.md) |
| [execute](arkts-arkts-taskpool-execute-f.md) |
| [executeDelayed](arkts-arkts-taskpool-executedelayed-f.md) |
| [executeDelayed](arkts-arkts-taskpool-executedelayed-f.md) |
| [executePeriodically](arkts-arkts-taskpool-executeperiodically-f.md) |
| [executePeriodically](arkts-arkts-taskpool-executeperiodically-f.md) |
| [getTask](arkts-arkts-taskpool-gettask-f.md) |
| [getTaskPoolInfo](arkts-arkts-taskpool-gettaskpoolinfo-f.md) |
| [isConcurrent](arkts-arkts-taskpool-isconcurrent-f.md) |
| [terminateTask](arkts-arkts-taskpool-terminatetask-f.md) |

### 类

| 名称 |
| --- |
| [AsyncRunner](arkts-arkts-taskpool-asyncrunner-c.md) |
| [GenericsTask](arkts-arkts-taskpool-genericstask-c.md) |
| [LongTask](arkts-arkts-taskpool-longtask-c.md) |
| [SequenceRunner](arkts-arkts-taskpool-sequencerunner-c.md) |
| [Task](arkts-arkts-taskpool-task-c.md) |
| [TaskGroup](arkts-arkts-taskpool-taskgroup-c.md) |
| [TaskInfo](arkts-arkts-taskpool-taskinfo-c.md) |
| [TaskPoolInfo](arkts-arkts-taskpool-taskpoolinfo-c.md) |
| [ThreadInfo](arkts-arkts-taskpool-threadinfo-c.md) |

### 接口

| 名称 |
| --- |
| [Configs](arkts-arkts-taskpool-configs-i.md) |
| [TaskResult](arkts-arkts-taskpool-taskresult-i.md) |

### 枚举

| 名称 |
| --- |
| [Priority](arkts-arkts-taskpool-priority-e.md) |
| [State](arkts-arkts-taskpool-state-e.md) |

### 类型

| 名称 |
| --- |
| [CallbackFunction](arkts-arkts-taskpool-callbackfunction-t.md) |
| [CallbackFunctionWithError](arkts-arkts-taskpool-callbackfunctionwitherror-t.md) |
