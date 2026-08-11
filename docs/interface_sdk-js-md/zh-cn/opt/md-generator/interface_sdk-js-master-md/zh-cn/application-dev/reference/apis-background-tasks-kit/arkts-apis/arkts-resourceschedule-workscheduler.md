# @ohos.resourceschedule.workScheduler

本模块提供延迟任务注册、取消、查询的能力。在开发过程中，对于实时性要求不高的任务，可以调用本模块接口注册延迟任务，在系统空闲时根据性能、功耗、热等情况进行调度执行。开发指导请参考  
[延迟任务开发指南](../../../task-management/work-scheduler.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace workScheduler--><!--Device-unnamed-declare namespace workScheduler-End-->

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

## 汇总

### 函数

| 名称 |
| --- |
| [getWorkStatus](arkts-backgroundtasks-workscheduler-getworkstatus-f.md#getworkstatus) |
| [getWorkStatus](arkts-backgroundtasks-workscheduler-getworkstatus-f.md#getworkstatus-1) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md#islastworktimeout) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md#islastworktimeout-1) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md#islastworktimeout-2) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainallworks) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainallworks-1) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md#obtainallworks-2) |
| [startWork](arkts-backgroundtasks-workscheduler-startwork-f.md#startwork) |
| [stopAndClearWorks](arkts-backgroundtasks-workscheduler-stopandclearworks-f.md#stopandclearworks) |
| [stopWork](arkts-backgroundtasks-workscheduler-stopwork-f.md#stopwork) |

### 接口

| 名称 |
| --- |
| [WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [BatteryStatus](arkts-backgroundtasks-workscheduler-batterystatus-e.md) |
| [ChargingType](arkts-backgroundtasks-workscheduler-chargingtype-e.md) |
| [NetworkType](arkts-backgroundtasks-workscheduler-networktype-e.md) |
| [StorageRequest](arkts-backgroundtasks-workscheduler-storagerequest-e.md) |

<!--Del-->
### 常量（系统接口）

| 名称 |
| --- |
| [EXECUTE_IMMEDIATE](arkts-backgroundtasks-workscheduler-con-sys.md#execute_immediate) |
| [WORK_SCHEDULER_CONDITION](arkts-backgroundtasks-workscheduler-con-sys.md#work_scheduler_condition) |
<!--DelEnd-->
