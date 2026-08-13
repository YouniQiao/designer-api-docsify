# @ohos.resourceschedule.backgroundTaskManager

本模块提供申请后台任务的接口。当应用退至后台时，开发者可以通过本模块接口为应用申请短时、长时任务，避免应用进程被终止或挂起。开发指导请参考 [长时任务开发指南](../../../task-management/continuous-task.md)、[短时任务开发指南](../../../task-management/transient-task.md)。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace backgroundTaskManager--><!--Device-unnamed-declare namespace backgroundTaskManager-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## 汇总

### 函数

| 名称 |
| --- |
| [cancelSuspendDelay](arkts-backgroundtasks-backgroundtaskmanager-cancelsuspenddelay-f.md#cancelSuspendDelay) |
| [getAllContinuousTasks](arkts-backgroundtasks-backgroundtaskmanager-getallcontinuoustasks-f.md#getAllContinuousTasks) |
| [getAllContinuousTasks](arkts-backgroundtasks-backgroundtaskmanager-getallcontinuoustasks-f.md#getAllContinuousTasks) |
| [getRemainingDelayTime](arkts-backgroundtasks-backgroundtaskmanager-getremainingdelaytime-f.md#getRemainingDelayTime) |
| [getRemainingDelayTime](arkts-backgroundtasks-backgroundtaskmanager-getremainingdelaytime-f.md#getRemainingDelayTime) |
| [getTransientTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-gettransienttaskinfo-f.md#getTransientTaskInfo) |
| [offContinuousTaskActive](arkts-backgroundtasks-backgroundtaskmanager-offcontinuoustaskactive-f.md#offContinuousTaskActive) |
| [offContinuousTaskCancel](arkts-backgroundtasks-backgroundtaskmanager-offcontinuoustaskcancel-f.md#offContinuousTaskCancel) |
| [offContinuousTaskSuspend](arkts-backgroundtasks-backgroundtaskmanager-offcontinuoustasksuspend-f.md#offContinuousTaskSuspend) |
| [off_continuousTaskActive](arkts-backgroundtasks-backgroundtaskmanager-offcontinuoustaskactive-f.md) |
| [off_continuousTaskCancel](arkts-backgroundtasks-backgroundtaskmanager-offcontinuoustaskcancel-f.md) |
| [off_continuousTaskSuspend](arkts-backgroundtasks-backgroundtaskmanager-offcontinuoustasksuspend-f.md) |
| [onContinuousTaskActive](arkts-backgroundtasks-backgroundtaskmanager-oncontinuoustaskactive-f.md#onContinuousTaskActive) |
| [onContinuousTaskCancel](arkts-backgroundtasks-backgroundtaskmanager-oncontinuoustaskcancel-f.md#onContinuousTaskCancel) |
| [onContinuousTaskSuspend](arkts-backgroundtasks-backgroundtaskmanager-oncontinuoustasksuspend-f.md#onContinuousTaskSuspend) |
| [on_continuousTaskActive](arkts-backgroundtasks-backgroundtaskmanager-oncontinuoustaskactive-f.md) |
| [on_continuousTaskCancel](arkts-backgroundtasks-backgroundtaskmanager-oncontinuoustaskcancel-f.md) |
| [on_continuousTaskSuspend](arkts-backgroundtasks-backgroundtaskmanager-oncontinuoustasksuspend-f.md) |
| [requestSuspendDelay](arkts-backgroundtasks-backgroundtaskmanager-requestsuspenddelay-f.md#requestSuspendDelay) |
| [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md#startBackgroundRunning) |
| [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md#startBackgroundRunning) |
| [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md#startBackgroundRunning) |
| [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md#startBackgroundRunning) |
| [stopBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-f.md#stopBackgroundRunning) |
| [stopBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-f.md#stopBackgroundRunning) |
| [stopBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-f.md#stopBackgroundRunning) |
| [updateBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-updatebackgroundrunning-f.md#updateBackgroundRunning) |
| [updateBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-updatebackgroundrunning-f.md#updateBackgroundRunning) |
| [updateDataTransferProgress](arkts-backgroundtasks-backgroundtaskmanager-updatedatatransferprogress-f.md#updateDataTransferProgress) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [applyEfficiencyResources](arkts-backgroundtasks-backgroundtaskmanager-applyefficiencyresources-f-sys.md#applyEfficiencyResources（系统接口）) |
| [getAllEfficiencyResources](arkts-backgroundtasks-backgroundtaskmanager-getallefficiencyresources-f-sys.md#getAllEfficiencyResources（系统接口）) |
| [getBackgroundTaskState](arkts-backgroundtasks-backgroundtaskmanager-getbackgroundtaskstate-f-sys.md#getBackgroundTaskState（系统接口）) |
| [obtainAllContinuousTasks](arkts-backgroundtasks-backgroundtaskmanager-obtainallcontinuoustasks-f-sys.md#obtainAllContinuousTasks（系统接口）) |
| [resetAllEfficiencyResources](arkts-backgroundtasks-backgroundtaskmanager-resetallefficiencyresources-f-sys.md#resetAllEfficiencyResources（系统接口）) |
| [setBackgroundTaskState](arkts-backgroundtasks-backgroundtaskmanager-setbackgroundtaskstate-f-sys.md#setBackgroundTaskState（系统接口）) |
| [subscribeContinuousTaskState](arkts-backgroundtasks-backgroundtaskmanager-subscribecontinuoustaskstate-f-sys.md#subscribeContinuousTaskState（系统接口）) |
| [unsubscribeContinuousTaskState](arkts-backgroundtasks-backgroundtaskmanager-unsubscribecontinuoustaskstate-f-sys.md#unsubscribeContinuousTaskState（系统接口）) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [ContinuousTaskRequest](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskrequest-c.md) |

### 接口

| 名称 |
| --- |
| [ContinuousTaskActiveInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskactiveinfo-i.md) |
| [ContinuousTaskCancelInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskcancelinfo-i.md) |
| [ContinuousTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskinfo-i.md) |
| [ContinuousTaskNotification](arkts-backgroundtasks-backgroundtaskmanager-continuoustasknotification-i.md) |
| [ContinuousTaskSuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-continuoustasksuspendinfo-i.md) |
| [DataTransferProgress](arkts-backgroundtasks-backgroundtaskmanager-datatransferprogress-i.md) |
| [DelaySuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-delaysuspendinfo-i.md) |
| [ProgressInfo](arkts-backgroundtasks-backgroundtaskmanager-progressinfo-i.md) |
| [SuspendMessage](arkts-backgroundtasks-backgroundtaskmanager-suspendmessage-i.md) |
| [TransientTaskInfo](arkts-backgroundtasks-backgroundtaskmanager-transienttaskinfo-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [BackgroundTaskStateInfo](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskstateinfo-i-sys.md) |
| [BackgroundTaskSubscriber](arkts-backgroundtasks-backgroundtaskmanager-backgroundtasksubscriber-i-sys.md) |
| [EfficiencyResourcesInfo](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcesinfo-i-sys.md) |
| [EfficiencyResourcesRequest](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcesrequest-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md) |
| [BackgroundModeType](arkts-backgroundtasks-backgroundtaskmanager-backgroundmodetype-e.md) |
| [BackgroundSubMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundsubmode-e.md) |
| [BackgroundTaskMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskmode-e.md) |
| [BackgroundTaskSubmode](arkts-backgroundtasks-backgroundtaskmanager-backgroundtasksubmode-e.md) |
| [ContinuousTaskCancelReason](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskcancelreason-e.md) |
| [ContinuousTaskDetailedCancelReason](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskdetailedcancelreason-e.md) |
| [ContinuousTaskSuspendReason](arkts-backgroundtasks-backgroundtaskmanager-continuoustasksuspendreason-e.md) |
| [UserAuthResult](arkts-backgroundtasks-backgroundtaskmanager-userauthresult-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e-sys.md) |
| [BackgroundTaskMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskmode-e-sys.md) |
| [EfficiencyResourcesCpuLevel](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcescpulevel-e-sys.md) |
| [ResourceType](arkts-backgroundtasks-backgroundtaskmanager-resourcetype-e-sys.md) |
<!--DelEnd-->
