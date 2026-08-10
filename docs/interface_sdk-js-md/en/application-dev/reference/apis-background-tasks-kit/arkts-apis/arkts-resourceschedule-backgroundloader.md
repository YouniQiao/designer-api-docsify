# @ohos.resourceschedule.backgroundLoader

后台预取接口

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace backgroundLoader--><!--Device-unnamed-declare namespace backgroundLoader-End-->

**System capability:** SystemCapability.ResourceSchedule.WorkScheduler

## Modules to Import

```TypeScript
import { backgroundLoader } from 'kits/@kit.BackgroundTasksKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [finishTask](arkts-backgroundtasks-backgroundloader-finishtask-f.md#finishtask) | 结束后台加载任务。 |
| [getTaskInfo](arkts-backgroundtasks-backgroundloader-gettaskinfo-f.md#gettaskinfo) | 获取后台预取任务信息。 |
| [registerTask](arkts-backgroundtasks-backgroundloader-registertask-f.md#registertask) | 注册后台加载任务。使用 callee.on(ON_START)来接受系统测触发的任务 |
| [unregisterTask](arkts-backgroundtasks-backgroundloader-unregistertask-f.md#unregistertask) | 取消注册后台加载任务。 |

### Interfaces

| Name | Description |
| --- | --- |
| [TaskInfo](arkts-backgroundtasks-backgroundloader-taskinfo-i.md) | 任务信息 |
| [TaskStopInfo](arkts-backgroundtasks-backgroundloader-taskstopinfo-i.md) | 停止任务的信息。 |

### Enums

| Name | Description |
| --- | --- |
| [StopCode](arkts-backgroundtasks-backgroundloader-stopcode-e.md) | 枚举停止代码， 用于ON_STOP函数。 |

### Constants

| Name | Description |
| --- | --- |
| [ON_START](arkts-backgroundtasks-backgroundloader-con.md#on_start) | 监听任务启动的方法 |
| [ON_STOP](arkts-backgroundtasks-backgroundloader-con.md#on_stop) | 监听任务结束的方法 |

