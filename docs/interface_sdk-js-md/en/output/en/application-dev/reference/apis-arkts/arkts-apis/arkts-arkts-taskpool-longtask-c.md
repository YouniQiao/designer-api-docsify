# LongTask

Describes a continuous task. **LongTask** inherits from [Task]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. No upper limit is set for the execution time of a continuous task, and no timeout exception is thrown if a continuous task runs for a long period of time. However, a continuous task cannot be executed in a task group or executed for multiple times. The thread for executing a continuous task exists until [terminateTask]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is called after the execution is complete. The thread is reclaimed when it is idle.

**Inheritance/Implementation:** LongTask extends [Task](arkts-arkts-taskpool-task-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-taskpool-class LongTask extends Task--><!--Device-taskpool-class LongTask extends Task-End-->

**System capability:** SystemCapability.Utils.Lang

