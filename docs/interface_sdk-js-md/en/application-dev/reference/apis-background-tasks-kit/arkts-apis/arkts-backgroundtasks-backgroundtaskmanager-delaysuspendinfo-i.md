# DelaySuspendInfo

Defines the information about the transient task.

**Since:** 23

<!--Device-backgroundTaskManager-interface DelaySuspendInfo--><!--Device-backgroundTaskManager-interface DelaySuspendInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## actualDelayTime

```TypeScript
actualDelayTime: int
```

Actual duration of the transient task requested by the application, in milliseconds. <br>Unit:ms

Note: The maximum duration of a transient task is 3 minutes in normal cases. In the case of a low battery ( [BatteryCapacityLevel](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-batteryinfo-batterycapacitylevel-e.md) set to **LEVEL_LOW**), the maximum duration is decreased to 1 minute.

**Type:** int

**Since:** 23

<!--Device-DelaySuspendInfo-actualDelayTime: int--><!--Device-DelaySuspendInfo-actualDelayTime: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

## requestId

```TypeScript
requestId: int
```

Request ID of the transient task.

**Type:** int

**Since:** 23

<!--Device-DelaySuspendInfo-requestId: int--><!--Device-DelaySuspendInfo-requestId: int-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

