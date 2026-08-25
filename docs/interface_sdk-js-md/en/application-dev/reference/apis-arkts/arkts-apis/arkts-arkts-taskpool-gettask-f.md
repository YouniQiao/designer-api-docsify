# getTask

## Modules to Import

```TypeScript
import { taskpool } from '@kit.ArkTS';
```

## getTask

```TypeScript
function getTask(taskId: number, taskName?: string): Task | undefined
```

Obtains the corresponding task instance by task ID, or by task ID and task name.

> **NOTE：**&gt;
> - If no task instance is found based on the input task ID, **undefined** is returned.&gt;
> - If the corresponding task instance can be queried based on the input task ID but the thread that calls the
> **getTask** method is different from the thread that creates the task instance, **undefined** is returned.&gt;
> - If taskId and taskName are both passed, and the name of the task instance queried via task ID does not match
> the provided task name, **undefined** is returned.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| taskId | number | Yes |
| taskName | string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Task \| undefined |

**Examples**

```TypeScript
import { taskpool } from '@kit.ArkTS';

@Concurrent
function addNum(num1: number, num2: number) {
  return num1 + num2;
}

function checkTask() {
  try {
    taskpool.getTask(null);
  } catch (e) {
    console.error("error:" + e);
    // error:BusinessError: Parameter error. The input parameters are invalid, the type of the first param must be number.
  }

  let task1:taskpool.Task = new taskpool.Task("addNum", addNum, 1, 2);
  let task2:taskpool.Task | undefined = taskpool.getTask(task1.taskId, "addNum"); // task2 is not undefined
  let task3:taskpool.Task | undefined = taskpool.getTask(task1.taskId, "add"); // task3 is undefined
  let task4:taskpool.Task | undefined = taskpool.getTask(0); // task4 is undefined
}

function dealTask() {
  let task1:taskpool.Task = new taskpool.Task(addNum, 1, 2);
  let task2:taskpool.Task | undefined = taskpool.getTask(task1.taskId);
  if (task2 === undefined) {
    return;
  }

  taskpool.execute(task2).then((result) => {
    console.info("task2 result: " + result); // task2 result: 3
  })
}
```
