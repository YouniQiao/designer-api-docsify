# stopAndClearWorks

## Modules to Import

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## stopAndClearWorks

```TypeScript
function stopAndClearWorks(): void
```

Stops and clears all the deferred tasks.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9700001](../errorcode-workScheduler.md#9700001-memory-operation-failure) |
| [9700002](../errorcode-workScheduler.md#9700002-parcel-operation-failure) |
| [9700003](../errorcode-workScheduler.md#9700003-system-service-failure) |
