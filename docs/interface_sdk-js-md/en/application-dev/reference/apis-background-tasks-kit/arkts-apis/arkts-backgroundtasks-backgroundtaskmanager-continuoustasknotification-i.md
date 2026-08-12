# ContinuousTaskNotification

Describes the information about a continuous-task notification.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-backgroundTaskManager-interface ContinuousTaskNotification--><!--Device-backgroundTaskManager-interface ContinuousTaskNotification-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## contentType

```TypeScript
contentType: notificationManager.ContentType
```

Content type of a continuous-task notification.

**Type:** notificationManager.ContentType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ContinuousTaskNotification-contentType: notificationManager.ContentType--><!--Device-ContinuousTaskNotification-contentType: notificationManager.ContentType-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## continuousTaskId

```TypeScript
continuousTaskId?: int
```

ID of a continuous task.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ContinuousTaskNotification-continuousTaskId?: int--><!--Device-ContinuousTaskNotification-continuousTaskId?: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## notificationId

```TypeScript
notificationId: int
```

ID of the continuous-task notification.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ContinuousTaskNotification-notificationId: int--><!--Device-ContinuousTaskNotification-notificationId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## slotType

```TypeScript
slotType: notificationManager.SlotType
```

Slot type of a continuous-task notification.

Note: After a continuous task is successfully requested or updated, no prompt tone is played.

**Type:** notificationManager.SlotType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ContinuousTaskNotification-slotType: notificationManager.SlotType--><!--Device-ContinuousTaskNotification-slotType: notificationManager.SlotType-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

