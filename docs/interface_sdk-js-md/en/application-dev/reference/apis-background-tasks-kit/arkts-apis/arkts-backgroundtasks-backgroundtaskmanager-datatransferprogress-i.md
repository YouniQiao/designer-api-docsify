# DataTransferProgress

长时任务通知进度信息。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

<!--Device-backgroundTaskManager-export interface DataTransferProgress--><!--Device-backgroundTaskManager-export interface DataTransferProgress-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## continuousTaskId

```TypeScript
continuousTaskId: int
```

长时任务ID。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataTransferProgress-continuousTaskId: int--><!--Device-DataTransferProgress-continuousTaskId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## progressInfo

```TypeScript
progressInfo: ProgressInfo
```

通知进度信息。

**Type:** [ProgressInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-progressinfo-i.md)

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataTransferProgress-progressInfo: ProgressInfo--><!--Device-DataTransferProgress-progressInfo: ProgressInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## wantAgent

```TypeScript
wantAgent?: WantAgent
```

通知参数，用于指定点击长时任务通知后跳转的界面。

**Type:** [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md)

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataTransferProgress-wantAgent?: WantAgent--><!--Device-DataTransferProgress-wantAgent?: WantAgent-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

