# @ohos.resourceschedule.workScheduler

本模块提供延迟任务注册、取消、查询的能力。在开发过程中，对于实时性要求不高的任务，可以调用本模块接口注册延迟任务，在系统空闲时根据性能、功耗、热等情况进行调度执行。开发指导请参考 [延迟任务开发指南](../../../task-management/work-scheduler.md)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

## 导入模块

```TypeScript
import { workScheduler } from '@kit.BackgroundTasksKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getWorkStatus](arkts-backgroundtasks-workscheduler-getworkstatus-f.md) |
| [getWorkStatus](arkts-backgroundtasks-workscheduler-getworkstatus-f.md) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md) |
| [isLastWorkTimeOut](arkts-backgroundtasks-workscheduler-islastworktimeout-f.md) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md) |
| [obtainAllWorks](arkts-backgroundtasks-workscheduler-obtainallworks-f.md) |
| [startWork](arkts-backgroundtasks-workscheduler-startwork-f.md) |
| [stopAndClearWorks](arkts-backgroundtasks-workscheduler-stopandclearworks-f.md) |
| [stopWork](arkts-backgroundtasks-workscheduler-stopwork-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [resetExecFrequency](arkts-backgroundtasks-workscheduler-resetexecfrequency-f-sys.md) |
| [setExecFrequency](arkts-backgroundtasks-workscheduler-setexecfrequency-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [WorkInfo](arkts-backgroundtasks-workscheduler-workinfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [FrequencyInfo](arkts-backgroundtasks-workscheduler-frequencyinfo-i-sys.md) |
<!--DelEnd-->

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
