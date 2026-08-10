# ContinuousTaskNotification

长时任务通知信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-backgroundTaskManager-interface ContinuousTaskNotification--><!--Device-backgroundTaskManager-interface ContinuousTaskNotification-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from 'kits/@kit.BackgroundTasksKit';
```

## contentType

```TypeScript
contentType: notificationManager.ContentType
```

长时任务通知的内容类型。

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

长时任务 Id。

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

长时任务通知 Id。

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

长时任务通知的渠道类型。

**说明：** 长时任务申请或更新成功后不支持提示音。

**Type:** notificationManager.SlotType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ContinuousTaskNotification-slotType: notificationManager.SlotType--><!--Device-ContinuousTaskNotification-slotType: notificationManager.SlotType-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

