# TaskPoolInfo

任务池的内部信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-taskpool-class TaskPoolInfo--><!--Device-taskpool-class TaskPoolInfo-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## taskInfos

```TypeScript
taskInfos: TaskInfo[]
```

任务的内部信息。不建议修改此值。

**Type:** [TaskInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-taskinfo-i.md)[]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskPoolInfo-taskInfos: TaskInfo[]--><!--Device-TaskPoolInfo-taskInfos: TaskInfo[]-End-->

**System capability:** SystemCapability.Utils.Lang

## threadInfos

```TypeScript
threadInfos: ThreadInfo[]
```

工作线程的内部信息。不建议修改此值。

**Type:** [ThreadInfo](arkts-arkts-taskpool-threadinfo-c.md)[]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TaskPoolInfo-threadInfos: ThreadInfo[]--><!--Device-TaskPoolInfo-threadInfos: ThreadInfo[]-End-->

**System capability:** SystemCapability.Utils.Lang

