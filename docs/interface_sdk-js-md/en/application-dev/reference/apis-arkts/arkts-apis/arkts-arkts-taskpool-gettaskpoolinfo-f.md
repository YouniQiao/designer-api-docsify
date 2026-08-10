# getTaskPoolInfo

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## getTaskPoolInfo

```TypeScript
function getTaskPoolInfo(): TaskPoolInfo
```

获取任务池的线程信息和任务信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-taskpool-function getTaskPoolInfo(): TaskPoolInfo--><!--Device-taskpool-function getTaskPoolInfo(): TaskPoolInfo-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [TaskPoolInfo](arkts-arkts-taskpool-taskpoolinfo-c.md) | 任务池的内部信息。 |

## Examples

```TypeScript
let taskpoolInfo: taskpool.TaskPoolInfo = taskpool.getTaskPoolInfo();
```

