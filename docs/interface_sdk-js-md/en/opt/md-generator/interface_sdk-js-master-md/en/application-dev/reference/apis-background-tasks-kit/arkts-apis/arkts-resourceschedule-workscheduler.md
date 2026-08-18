# @ohos.resourceschedule.workScheduler

The **workScheduler** module provides the APIs for registering, canceling, and querying deferred tasks. You can use the APIs to register tasks that do not have high requirements on real-time performance as deferred tasks. The system schedules and executes the deferred tasks at an appropriate time, subject to the storage space, power consumption, and more. For details, see [Deferred Task Scheduling](../../../task-management/work-scheduler.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace workScheduler--><!--Device-unnamed-declare namespace workScheduler-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getWorkStatus](arkts-backgroundtasks-workscheduler-getworkstatus-f.md#getworkstatus) |
| [getWorkStatus](arkts-backgroundtasks-workscheduler-getworkstatus-f.md#getworkstatus) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md#islastworktimeout) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md#islastworktimeout) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md#islastworktimeout) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainallworks) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainallworks) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainallworks) |
| [startWork](arkts-backgroundtasks-workscheduler-startwork-f.md#startwork) |
| [stopAndClearWorks](arkts-backgroundtasks-workscheduler-stopandclearworks-f.md#stopandclearworks) |
| [stopWork](arkts-backgroundtasks-workscheduler-stopwork-f.md#stopwork) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [resetExecFrequency](arkts-backgroundtasks-workscheduler-resetexecfrequency-f-sys.md#resetexecfrequency-system-api) |
| [setExecFrequency](arkts-backgroundtasks-workscheduler-setexecfrequency-f-sys.md#setexecfrequency-system-api) |
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
| [EXECUTE_IMMEDIATE](arkts-backgroundtasks-workscheduler-con-sys.md#executeimmediate) |
| [WORK_SCHEDULER_CONDITION](arkts-backgroundtasks-workscheduler-con-sys.md#workschedulercondition) |
<!--DelEnd-->
