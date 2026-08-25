# executePeriodically

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## executePeriodically

```TypeScript
function executePeriodically(period: number, task: Task, priority?: Priority): void
```

Executes a task periodically. In this execution mode, you can set the task priority and call **cancel()** to cancel the execution. A periodic task cannot be a task in a task group, serial queue, or asynchronous queue. It cannot call **execute()** again or have a dependency relationship.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| period | number | Yes |
| task | [Task](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |
| [10200028](../errorcode-utils.md#10200028-delay-less-than-zero) |
| [10200050](../errorcode-utils.md#10200050-concurrent-task-that-has-been-executed-cannot-be-executed-periodically) |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |


## executePeriodically

```TypeScript
function executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void
```

Executes a generic task periodically, without verifying the parameter type and return value type of the task. The verification of the **executePeriodically** task works in conjunction with **new GenericsTask**, requiring that the parameter and return value types match those specified in **new GenericsTask**.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| period | number | Yes |
| task | [GenericsTask](arkts-arkts-taskpool-genericstask-c.md)&lt;A, R&gt; | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |
| [10200028](../errorcode-utils.md#10200028-delay-less-than-zero) |
| [10200050](../errorcode-utils.md#10200050-concurrent-task-that-has-been-executed-cannot-be-executed-periodically) |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |
