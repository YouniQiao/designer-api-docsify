# SequenceRunner

Implements a serial queue, in which all tasks are executed in sequence.

**Since:** 11

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(priority?: Priority)
```

A constructor used to create a **SequenceRunner** instance.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

## constructor

```TypeScript
constructor(name: string, priority?: Priority)
```

A constructor used to create a **SequenceRunner** instance. This instance represents a global serial queue. If the passed-in name is the same as an existing name, the same serial queue is returned.

> **NOTE：**&gt;
> - The bottom layer uses the singleton mode to ensure that the same instance is obtained when a serial queue
> with the same name is created.&gt;
> - The priority of a serial queue cannot be modified.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

## execute

```TypeScript
execute(task: Task): Promise<Object>
```

Adds a task to the serial queue for execution. Before using this API, you must create a **SequenceRunner** instance. Tasks in another task group, serial queue, or asynchronous queue, dependent tasks, and tasks that have been executed cannot be added to the serial queue. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Tasks that depend others cannot be added to the serial queue.&gt;
> - The failure or cancellation of a task does not affect the execution of subsequent tasks in the serial queue.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [Task](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Object & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200003](../errorcode-utils.md#10200003-failed-to-initialize-the-worker-instance) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200025](../errorcode-utils.md#10200025-failed-to-add-a-task-with-dependent-tasks-to-the-queue) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |
