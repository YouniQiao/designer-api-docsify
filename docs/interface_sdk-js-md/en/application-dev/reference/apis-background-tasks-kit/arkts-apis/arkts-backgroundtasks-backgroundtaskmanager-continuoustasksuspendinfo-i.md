# ContinuousTaskSuspendInfo

Describes the information about a suspended continuous task.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-backgroundTaskManager-interface ContinuousTaskSuspendInfo--><!--Device-backgroundTaskManager-interface ContinuousTaskSuspendInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## continuousTaskId

```TypeScript
continuousTaskId: int
```

ID of the suspended continuous task.

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskSuspendInfo-continuousTaskId: int--><!--Device-ContinuousTaskSuspendInfo-continuousTaskId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## suspendMessage

```TypeScript
suspendMessage?: SuspendMessage
```

Describes the information about a suspended continuous task.

**Type:** SuspendMessage

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinuousTaskSuspendInfo-suspendMessage?: SuspendMessage--><!--Device-ContinuousTaskSuspendInfo-suspendMessage?: SuspendMessage-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## suspendReason

```TypeScript
suspendReason: ContinuousTaskSuspendReason
```

Reason why the continuous task is suspended.

**Type:** ContinuousTaskSuspendReason

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskSuspendInfo-suspendReason: ContinuousTaskSuspendReason--><!--Device-ContinuousTaskSuspendInfo-suspendReason: ContinuousTaskSuspendReason-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## suspendState

```TypeScript
suspendState: boolean
```

Continuous task state. The value **false** indicates that the task is activated, and the value **true** indicates that the task is suspended.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskSuspendInfo-suspendState: boolean--><!--Device-ContinuousTaskSuspendInfo-suspendState: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

