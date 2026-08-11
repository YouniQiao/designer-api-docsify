# @ohos.resourceschedule.backgroundLoader

The **BackgroundLoader** module provides the APIs for registering, unregistering and querying tasks. You can use these APIs to register tasks that need to be loaded in the background. The system schedules and executes these deferred tasks at an appropriate time, subject to the storage space, power consumption.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace backgroundLoader--><!--Device-unnamed-declare namespace backgroundLoader-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## Modules to Import

```TypeScript
import { backgroundLoader } from 'kits/@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [finishTask](arkts-backgroundtasks-backgroundloader-finishtask-f.md#finishtask) |
| [getTaskInfo](arkts-backgroundtasks-backgroundloader-gettaskinfo-f.md#gettaskinfo) |
| [registerTask](arkts-backgroundtasks-backgroundloader-registertask-f.md#registertask) |
| [unregisterTask](arkts-backgroundtasks-backgroundloader-unregistertask-f.md#unregistertask) |

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
