# DataTransferProgress

Information about continuousTask notification progress.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

<!--Device-backgroundTaskManager-export interface DataTransferProgress--><!--Device-backgroundTaskManager-export interface DataTransferProgress-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## continuousTaskId

```TypeScript
continuousTaskId: int
```

Continuous task ID. The value should be an integer.

**Type:** int

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataTransferProgress-continuousTaskId: int--><!--Device-DataTransferProgress-continuousTaskId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## progressInfo

```TypeScript
progressInfo: ProgressInfo
```

Notify progress data.

**Type:** ProgressInfo

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataTransferProgress-progressInfo: ProgressInfo--><!--Device-DataTransferProgress-progressInfo: ProgressInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## wantAgent

```TypeScript
wantAgent?: WantAgent
```

Notification parameters, which are used to specify the target page that is redirected to when a continuous task notification is clicked.

**Type:** WantAgent

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataTransferProgress-wantAgent?: WantAgent--><!--Device-DataTransferProgress-wantAgent?: WantAgent-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

