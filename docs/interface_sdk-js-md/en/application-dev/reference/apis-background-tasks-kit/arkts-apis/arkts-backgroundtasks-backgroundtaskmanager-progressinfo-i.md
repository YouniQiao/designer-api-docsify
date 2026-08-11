# ProgressInfo

Notify progress data.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

<!--Device-backgroundTaskManager-export interface ProgressInfo--><!--Device-backgroundTaskManager-export interface ProgressInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## fileName

```TypeScript
fileName: string
```

Notification content.

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressInfo-fileName: string--><!--Device-ProgressInfo-fileName: string-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## isMute

```TypeScript
isMute?: boolean
```

Whether to ring when the download progress reaches 100%.

**Type:** boolean

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressInfo-isMute?: boolean--><!--Device-ProgressInfo-isMute?: boolean-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## progressValue

```TypeScript
progressValue?: int
```

Download progress. If this field does not exist, the progress ring will not be displayed.The value should be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressInfo-progressValue?: int--><!--Device-ProgressInfo-progressValue?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## title

```TypeScript
title: string
```

Notification title.

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressInfo-title: string--><!--Device-ProgressInfo-title: string-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

