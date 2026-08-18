# TransientTaskInfo

Describes all transient task information.

**Since:** 23

<!--Device-backgroundTaskManager-interface TransientTaskInfo--><!--Device-backgroundTaskManager-interface TransientTaskInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

## Modules to Import

```TypeScript
```

## remainingQuota

```TypeScript
remainingQuota: number
```

Remaining quota of the application on the current day, in ms. <br>Unit:ms

**Type:** number

**Since:** 23

<!--Device-TransientTaskInfo-remainingQuota: int--><!--Device-TransientTaskInfo-remainingQuota: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

## transientTasks

```TypeScript
transientTasks: DelaySuspendInfo[]
```

All information about the requested transient task.

**Type:** DelaySuspendInfo[]

**Since:** 23

<!--Device-TransientTaskInfo-transientTasks: DelaySuspendInfo[]--><!--Device-TransientTaskInfo-transientTasks: DelaySuspendInfo[]-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
