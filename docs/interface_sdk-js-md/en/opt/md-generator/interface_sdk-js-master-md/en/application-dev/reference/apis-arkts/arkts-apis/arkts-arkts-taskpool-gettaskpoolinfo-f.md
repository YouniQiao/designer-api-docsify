# getTaskPoolInfo

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## getTaskPoolInfo

```TypeScript
function getTaskPoolInfo(): TaskPoolInfo
```

Obtains the thread information and task information of the task pool.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-taskpool-function getTaskPoolInfo(): TaskPoolInfo--><!--Device-taskpool-function getTaskPoolInfo(): TaskPoolInfo-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [TaskPoolInfo](arkts-arkts-taskpool-taskpoolinfo-c.md) |

## Examples

```TypeScript
let taskpoolInfo: taskpool.TaskPoolInfo = taskpool.getTaskPoolInfo();
```
