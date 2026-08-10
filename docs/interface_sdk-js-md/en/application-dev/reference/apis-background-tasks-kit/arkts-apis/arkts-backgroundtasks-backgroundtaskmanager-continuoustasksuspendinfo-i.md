# ContinuousTaskSuspendInfo

长时任务暂停信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-backgroundTaskManager-interface ContinuousTaskSuspendInfo--><!--Device-backgroundTaskManager-interface ContinuousTaskSuspendInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## continuousTaskId

```TypeScript
continuousTaskId: int
```

被暂停的长时任务 Id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskSuspendInfo-continuousTaskId: int--><!--Device-ContinuousTaskSuspendInfo-continuousTaskId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## suspendMessage

```TypeScript
suspendMessage?: SuspendMessage
```

长时任务暂停信息。

**Type:** [SuspendMessage](arkts-backgroundtasks-backgroundtaskmanager-suspendmessage-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinuousTaskSuspendInfo-suspendMessage?: SuspendMessage--><!--Device-ContinuousTaskSuspendInfo-suspendMessage?: SuspendMessage-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## suspendReason

```TypeScript
suspendReason: ContinuousTaskSuspendReason
```

长时任务暂停原因。

**Type:** [ContinuousTaskSuspendReason](arkts-backgroundtasks-backgroundtaskmanager-continuoustasksuspendreason-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskSuspendInfo-suspendReason: ContinuousTaskSuspendReason--><!--Device-ContinuousTaskSuspendInfo-suspendReason: ContinuousTaskSuspendReason-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## suspendState

```TypeScript
suspendState: boolean
```

长时任务状态，false表示激活，true表示暂停。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ContinuousTaskSuspendInfo-suspendState: boolean--><!--Device-ContinuousTaskSuspendInfo-suspendState: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

