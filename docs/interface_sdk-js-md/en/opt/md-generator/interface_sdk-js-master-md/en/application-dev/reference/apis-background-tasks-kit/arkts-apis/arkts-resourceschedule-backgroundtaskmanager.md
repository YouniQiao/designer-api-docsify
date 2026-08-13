# @ohos.resourceschedule.backgroundTaskManager

The **backgroundTaskManager** module provides APIs to request background tasks. You can use the APIs to request transient tasks, continuous tasks, or efficiency resources to prevent the application process from being terminated or suspended when your application is switched to the background. For details, see [Continuous Task](../../../task-management/continuous-task.md) and [Transient Task](../../../task-management/transient-task.md).

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace backgroundTaskManager--><!--Device-unnamed-declare namespace backgroundTaskManager-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

## Modules to Import

```TypeScript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [applyEfficiencyResources](arkts-backgroundtasks-backgroundtaskmanager-applyefficiencyresources-f-sys.md#applyEfficiencyResources-(System-API)) |
| [getAllEfficiencyResources](arkts-backgroundtasks-backgroundtaskmanager-getallefficiencyresources-f-sys.md#getAllEfficiencyResources-(System-API)) |
| [getBackgroundTaskState](arkts-backgroundtasks-backgroundtaskmanager-getbackgroundtaskstate-f-sys.md#getBackgroundTaskState-(System-API)) |
| [obtainAllContinuousTasks](arkts-backgroundtasks-backgroundtaskmanager-obtainallcontinuoustasks-f-sys.md#obtainAllContinuousTasks-(System-API)) |
| [resetAllEfficiencyResources](arkts-backgroundtasks-backgroundtaskmanager-resetallefficiencyresources-f-sys.md#resetAllEfficiencyResources-(System-API)) |
| [setBackgroundTaskState](arkts-backgroundtasks-backgroundtaskmanager-setbackgroundtaskstate-f-sys.md#setBackgroundTaskState-(System-API)) |
| [subscribeContinuousTaskState](arkts-backgroundtasks-backgroundtaskmanager-subscribecontinuoustaskstate-f-sys.md#subscribeContinuousTaskState-(System-API)) |
| [unsubscribeContinuousTaskState](arkts-backgroundtasks-backgroundtaskmanager-unsubscribecontinuoustaskstate-f-sys.md#unsubscribeContinuousTaskState-(System-API)) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ContinuousTaskRequest](arkts-backgroundtasks-backgroundtaskmanager-continuoustaskrequest-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BackgroundTaskStateInfo](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskstateinfo-i-sys.md) |
| [BackgroundTaskSubscriber](arkts-backgroundtasks-backgroundtaskmanager-backgroundtasksubscriber-i-sys.md) |
| [EfficiencyResourcesInfo](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcesinfo-i-sys.md) |
| [EfficiencyResourcesRequest](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcesrequest-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e-sys.md) |
| [BackgroundTaskMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundtaskmode-e-sys.md) |
| [EfficiencyResourcesCpuLevel](arkts-backgroundtasks-backgroundtaskmanager-efficiencyresourcescpulevel-e-sys.md) |
| [ResourceType](arkts-backgroundtasks-backgroundtaskmanager-resourcetype-e-sys.md) |
<!--DelEnd-->
