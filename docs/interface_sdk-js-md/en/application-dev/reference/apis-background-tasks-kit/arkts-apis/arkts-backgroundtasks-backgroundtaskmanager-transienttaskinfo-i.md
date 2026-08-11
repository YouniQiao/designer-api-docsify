# TransientTaskInfo

Describes all transient task information.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-backgroundTaskManager-interface TransientTaskInfo--><!--Device-backgroundTaskManager-interface TransientTaskInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## remainingQuota

```TypeScript
remainingQuota: int
```

Remaining quota of the application on the current day, in ms.&lt;br&gt;Unit:ms

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-TransientTaskInfo-remainingQuota: int--><!--Device-TransientTaskInfo-remainingQuota: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

## transientTasks

```TypeScript
transientTasks: DelaySuspendInfo[]
```

All information about the requested transient task.

**Type:** [DelaySuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-delaysuspendinfo-i.md)[]

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-TransientTaskInfo-transientTasks: DelaySuspendInfo[]--><!--Device-TransientTaskInfo-transientTasks: DelaySuspendInfo[]-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

