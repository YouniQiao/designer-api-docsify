# resetExecFrequency (System API)

## Modules to Import

```TypeScript
import { workScheduler } from 'kits/@kit.BackgroundTasksKit';
```

## resetExecFrequency

```TypeScript
function resetExecFrequency(uid: number): void
```

Reset the execution frequency.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.SET_WORK_SCHEDULER_PROPERTY

**Model restriction:** This API can be used only in the stage model.

<!--Device-workScheduler-function resetExecFrequency(uid: number): void--><!--Device-workScheduler-function resetExecFrequency(uid: number): void-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | number | Yes | App uid. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9700006 | Failed to check the uid. |
| [9700003](../../apis-backgroundtasks-kit/errorcode-workScheduler.md#9700003-system-service-failure) | System service operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

