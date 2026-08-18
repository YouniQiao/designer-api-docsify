# AsyncRunner

Implements an asynchronous queue, for which you can specify the task execution concurrency and queuing policy.

**Since:** 18

<!--Device-taskpool-export class AsyncRunner--><!--Device-taskpool-export class AsyncRunner-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(runningCapacity: number, waitingCapacity?: number)
```

A constructor used to create an **AsyncRunner** instance. It constructs a non-global asynchronous queue. Even when the parameters passed are the same, it returns different asynchronous queues.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AsyncRunner-constructor(runningCapacity: number, waitingCapacity?: number)--><!--Device-AsyncRunner-constructor(runningCapacity: number, waitingCapacity?: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| runningCapacity | number | Yes |
| waitingCapacity | number | No |

**Examples**

```TypeScript
let runner: taskpool.AsyncRunner = new taskpool.AsyncRunner(5);
```

## constructor

```TypeScript
constructor(name: string, runningCapacity: number, waitingCapacity?: number)
```

A constructor used to create an **AsyncRunner** instance. It constructs a global asynchronous queue. If the queue name is the same as an existing name, the same asynchronous queue is returned. > **NOTE：**> > - The bottom layer uses the singleton mode to ensure that the same instance is obtained when an asynchronous > queue with the same name is created. > > - The task execution concurrency and waiting capacity cannot be modified.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AsyncRunner-constructor(name: string, runningCapacity: number, waitingCapacity?: number)--><!--Device-AsyncRunner-constructor(name: string, runningCapacity: number, waitingCapacity?: number)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| runningCapacity | number | Yes |
| waitingCapacity | number | No |

**Examples**

```TypeScript
let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner("runner1", 5, 5);
```

## execute

```TypeScript
execute(task: Task, priority?: Priority): Promise<Object>
```

Adds a task to the asynchronous queue for execution. Before using this API, you must create an **AsyncRunner** instance. This API uses a promise to return the result. > **NOTE：**> > - Tasks in a task group cannot be added to the asynchronous queue. > > - Tasks in a serial queue cannot be added to the asynchronous queue. > > - Tasks in other asynchronous queues cannot be added to the asynchronous queue. > > - Periodic tasks cannot be added to the asynchronous queue. > > - Delayed tasks cannot be added to the asynchronous queue. > > - Tasks that depend others cannot be added to the asynchronous queue. > > - Tasks that have been executed cannot be added to the asynchronous queue.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AsyncRunner-execute(task: Task, priority?: Priority): Promise<Object>--><!--Device-AsyncRunner-execute(task: Task, priority?: Priority): Promise<Object>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| task | [Task](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-task-i.md) | Yes |
| priority | [Priority](arkts-arkts-taskpool-priority-e.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Object & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200025](../errorcode-utils.md#10200025-failed-to-add-a-task-with-dependent-tasks-to-the-queue) |
| [10200057](../errorcode-utils.md#10200057-task-cannot-be-executed-by-two-apis) |
| [10200051](../errorcode-utils.md#10200051-periodic-task-cannot-be-executed-again) |
| [10200006](../errorcode-utils.md#10200006-worker-data-serialization-exception) |
| [10200054](../errorcode-utils.md#10200054-asynchronous-queue-task-discarded) |

**Examples**

```TypeScript
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
function additionDelay(delay: number): void {
  let start: number = new Date().getTime();
  while (new Date().getTime() - start < delay) {
    continue;
  }
}
async function asyRunner() {
  let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner("runner1", 5, 5);
  for (let i = 0; i < 30; i++) {
    let task:taskpool.Task = new taskpool.Task(additionDelay, 1000);
    runner.execute(task).then(() => {
      console.info("asyncRunner: task" + i + " done.");
    }).catch((e: BusinessError) => {
      console.error("asyncRunner: task" + i + " error." + e.code + "-" + e.message);
    });
  }
}

async function asyRunner2() {
  let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner(5);
  for (let i = 0; i < 20; i++) {
    let task:taskpool.Task = new taskpool.Task(additionDelay, 1000);
    runner.execute(task).then(() => {
      console.info("asyncRunner: task" + i + " done.");
    });
  }
}
```
