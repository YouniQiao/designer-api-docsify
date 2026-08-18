# ContinuousTaskCancelInfo

Describes the information about the cancellation of a continuous task.

**Since:** 23

<!--Device-backgroundTaskManager-interface ContinuousTaskCancelInfo--><!--Device-backgroundTaskManager-interface ContinuousTaskCancelInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## Modules to Import

```TypeScript
```

## detailedReason

```TypeScript
detailedReason?: ContinuousTaskDetailedCancelReason
```

Detailed reason for canceling the continuous task.

**Type:** [ContinuousTaskDetailedCancelReason](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskdetailedcancelreason-e.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinuousTaskCancelInfo-detailedReason?: ContinuousTaskDetailedCancelReason--><!--Device-ContinuousTaskCancelInfo-detailedReason?: ContinuousTaskDetailedCancelReason-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## id

```TypeScript
id: number
```

ID of the continuous task canceled.

**Type:** number

**Since:** 23

<!--Device-ContinuousTaskCancelInfo-id: int--><!--Device-ContinuousTaskCancelInfo-id: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## reason

```TypeScript
reason: ContinuousTaskCancelReason
```

Reason for canceling the continuous task.

**Type:** [ContinuousTaskCancelReason](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskcancelreason-e.md)

**Since:** 23

<!--Device-ContinuousTaskCancelInfo-reason: ContinuousTaskCancelReason--><!--Device-ContinuousTaskCancelInfo-reason: ContinuousTaskCancelReason-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
