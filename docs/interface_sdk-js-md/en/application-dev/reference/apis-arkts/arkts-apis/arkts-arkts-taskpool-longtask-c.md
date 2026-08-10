# LongTask

表示长时任务。**LongTask**继承自  
[Task](arkts-arkts-taskpool-execute-f.md#execute)。长时任务不设置执行时间上限，长时间运行不会触发超时异常，但不支持将同一任务多次执行或者将该任务加入任务组（TaskGroup）。执行长时任务的线程会持续存在，直到任务完成并调用[terminateTask](arkts-arkts-taskpool-terminatetask-f.md#terminatetask)后，该线程在空闲时被回收。

**Inheritance/Implementation:** LongTask extends [Task](arkts-arkts-taskpool-task-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-taskpool-class LongTask extends Task--><!--Device-taskpool-class LongTask extends Task-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

