# Job

Represents a handle to a task's result, used to await the completion of a task.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class Job--><!--Device-unnamed-export class Job-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## Await

```TypeScript
Await(): T
```

Waits for the completion of the job and returns the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Job-Await(): T--><!--Device-Job-Await(): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| T | The result of the task. |

