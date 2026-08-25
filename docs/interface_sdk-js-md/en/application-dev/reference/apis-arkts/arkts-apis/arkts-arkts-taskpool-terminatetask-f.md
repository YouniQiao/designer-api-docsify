# terminateTask

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## terminateTask

```TypeScript
function terminateTask(longTask: LongTask): void
```

Terminates a continuous task in the task pool. It is called after the continuous task is complete. After the task is terminated, the thread that executes the task may be reclaimed.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| longTask | [LongTask](arkts-arkts-taskpool-longtask-c.md) | Yes |
