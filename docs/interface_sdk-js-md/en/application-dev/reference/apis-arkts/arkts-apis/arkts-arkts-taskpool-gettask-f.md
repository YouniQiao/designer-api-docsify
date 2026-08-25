# getTask

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
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
