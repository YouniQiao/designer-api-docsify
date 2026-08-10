# ThreadInfo

工作线程的内部信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-taskpool-class ThreadInfo--><!--Device-taskpool-class ThreadInfo-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## priority

```TypeScript
priority?: Priority
```

当前线程的优先级。如果返回为空，表示当前没有任务执行。不建议修改此值。

**Type:** [Priority](arkts-arkts-taskpool-priority-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadInfo-priority?: Priority--><!--Device-ThreadInfo-priority?: Priority-End-->

**System capability:** SystemCapability.Utils.Lang

## taskIds

```TypeScript
taskIds?: number[]
```

在当前线程上运行的任务ID列表。如果返回为空，表示当前没有任务执行。不建议修改此值。

**Type:** number[]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadInfo-taskIds?: number[]--><!--Device-ThreadInfo-taskIds?: number[]-End-->

**System capability:** SystemCapability.Utils.Lang

## tid

```TypeScript
tid: number
```

工作线程的标识符。如果返回为空，表示当前没有任务执行。不建议修改此值。

**Type:** number

**Default:** 0

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ThreadInfo-tid: number--><!--Device-ThreadInfo-tid: number-End-->

**System capability:** SystemCapability.Utils.Lang

