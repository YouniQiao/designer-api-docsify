# @ohos.resourceschedule.backgroundLoader

The **BackgroundLoader** module provides the APIs for registering, unregistering and querying tasks. You can use these APIs to register tasks that need to be loaded in the background. The system schedules and executes these deferred tasks at an appropriate time, subject to the storage space, power consumption.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## Modules to Import

```TypeScript
import { backgroundLoader } from '@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [finishTask](arkts-backgroundtasks-backgroundloader-finishtask-f.md) |
| [getTaskInfo](arkts-backgroundtasks-backgroundloader-gettaskinfo-f.md) |
| [registerTask](arkts-backgroundtasks-backgroundloader-registertask-f.md) |
| [unregisterTask](arkts-backgroundtasks-backgroundloader-unregistertask-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TaskInfo](arkts-backgroundtasks-backgroundloader-taskinfo-i.md) |
| [TaskStopInfo](arkts-backgroundtasks-backgroundloader-taskstopinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [StopCode](arkts-backgroundtasks-backgroundloader-stopcode-e.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ON_START](arkts-backgroundtasks-backgroundloader-con.md#on_start) |
| [ON_STOP](arkts-backgroundtasks-backgroundloader-con.md#on_stop) |
