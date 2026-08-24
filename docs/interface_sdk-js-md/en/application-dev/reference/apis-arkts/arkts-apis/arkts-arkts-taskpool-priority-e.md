# Priority

Enumerates the priorities available for created tasks. The task priority applies during task execution. The worker thread priority is updated with the task priority. For details about the mappings, see QoS Level.

**Since:** 9

<!--Device-taskpool-enum Priority--><!--Device-taskpool-enum Priority-End-->

**System capability:** SystemCapability.Utils.Lang

## HIGH

```TypeScript
HIGH = 0
```

The task has a high priority.This API can be used in atomic services since API version 11.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Priority-HIGH = 0--><!--Device-Priority-HIGH = 0-End-->

**System capability:** SystemCapability.Utils.Lang

## MEDIUM

```TypeScript
MEDIUM = 1
```

The task has a medium priority.This API can be used in atomic services since API version 11.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Priority-MEDIUM = 1--><!--Device-Priority-MEDIUM = 1-End-->

**System capability:** SystemCapability.Utils.Lang

## LOW

```TypeScript
LOW = 2
```

The task has a low priority.This API can be used in atomic services since API version 11.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Priority-LOW = 2--><!--Device-Priority-LOW = 2-End-->

**System capability:** SystemCapability.Utils.Lang

## IDLE

```TypeScript
IDLE = 3
```

The task is a background task.This API can be used in atomic services since API version 12.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Priority-IDLE = 3--><!--Device-Priority-IDLE = 3-End-->

**System capability:** SystemCapability.Utils.Lang

**Examples**

```TypeScript
@Concurrent
function printArgs(args: number): number {
  let t: number = Date.now();
  while (Date.now() - t < 1000) { // 1000: delay 1s
    continue;
  }
  console.info("printArgs: " + args);
  return args;
}

let allCount = 100; // 100: test number
let taskArray: Array<taskpool.Task> = [];
// Create 400 tasks and add them to taskArray.
for (let i: number = 0; i < allCount; i++) {
  let task1: taskpool.Task = new taskpool.Task(printArgs, i);
  taskArray.push(task1);
  let task2: taskpool.Task = new taskpool.Task(printArgs, i * 10); // 10: test number
  taskArray.push(task2);
  let task3: taskpool.Task = new taskpool.Task(printArgs, i * 100); // 100: test number
  taskArray.push(task3);
  let task4: taskpool.Task = new taskpool.Task(printArgs, i * 1000); // 1000: test number
  taskArray.push(task4);
}

// Obtain different tasks from taskArray and specify different priorities for execution.
for (let i: number = 0; i < taskArray.length; i+=4) { // 4: Four tasks are executed each time. When obtaining tasks cyclically, obtain the four items following the last batch to ensure that different tasks are obtained each time.
  taskpool.execute(taskArray[i], taskpool.Priority.HIGH);
  taskpool.execute(taskArray[i + 1], taskpool.Priority.LOW);
  taskpool.execute(taskArray[i + 2], taskpool.Priority.MEDIUM);
  taskpool.execute(taskArray[i + 3], taskpool.Priority.IDLE);
}
```

