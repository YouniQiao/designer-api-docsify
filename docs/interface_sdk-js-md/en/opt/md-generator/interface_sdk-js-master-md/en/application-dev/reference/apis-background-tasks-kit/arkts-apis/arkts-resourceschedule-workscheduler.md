# @ohos.resourceschedule.workScheduler

The **workScheduler** module provides the APIs for registering, canceling, and querying deferred tasks. You can use the APIs to register tasks that do not have high requirements on real-time performance as deferred tasks. The system schedules and executes the deferred tasks at an appropriate time, subject to the storage space, power consumption, and more. For details, see [Deferred Task Scheduling](../../../task-management/work-scheduler.md).

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace workScheduler--><!--Device-unnamed-declare namespace workScheduler-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## Modules to Import

```TypeScript
import { workScheduler } from '@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getWorkStatus](arkts-backgroundtasks-workscheduler-getworkstatus-f.md#getWorkStatus) |
| [getWorkStatus](arkts-backgroundtasks-workscheduler-getworkstatus-f.md#getWorkStatus) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md#isLastWorkTimeOut) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md#isLastWorkTimeOut) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md#isLastWorkTimeOut) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainAllWorks) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainAllWorks) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainAllWorks) |
| [startWork](arkts-backgroundtasks-workscheduler-startwork-f.md#startWork) |
| [stopAndClearWorks](arkts-backgroundtasks-workscheduler-stopandclearworks-f.md#stopAndClearWorks) |
| [stopWork](arkts-backgroundtasks-workscheduler-stopwork-f.md#stopWork) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [resetExecFrequency](arkts-backgroundtasks-workscheduler-resetexecfrequency-f-sys.md#resetExecFrequency-(System-API)) |
| [setExecFrequency](arkts-backgroundtasks-workscheduler-setexecfrequency-f-sys.md#setExecFrequency-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FrequencyInfo](arkts-backgroundtasks-workscheduler-frequencyinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BatteryStatus](arkts-backgroundtasks-workscheduler-batterystatus-e.md) |
| [ChargingType](arkts-backgroundtasks-workscheduler-chargingtype-e.md) |
| [NetworkType](arkts-backgroundtasks-workscheduler-networktype-e.md) |
| [StorageRequest](arkts-backgroundtasks-workscheduler-storagerequest-e.md) |

<!--Del-->
### Constants（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EXECUTE_IMMEDIATE](arkts-backgroundtasks-workscheduler-con-sys.md#EXECUTE_IMMEDIATE) |
| [WORK_SCHEDULER_CONDITION](arkts-backgroundtasks-workscheduler-con-sys.md#WORK_SCHEDULER_CONDITION) |
<!--DelEnd-->
