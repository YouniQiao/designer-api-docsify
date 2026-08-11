# @ohos.backgroundTaskManager

本模块提供后台任务管理能力。

当应用或业务模块处于后台（无可见界面）时，如果有需要继续执行或者后续执行的业务，可基于业务类型，申请短时任务延迟挂起（Suspend）或者长时任务避免进入挂起状态。

应用有不可中断且短时间能完成的任务时（如，用户在文件管理器上点击垃圾文件清理，若清理未完成时退到后台，文件管理器需要申请短时任务完成清理），可以使用短时任务机制。

应用中存在用户能够直观感受到的且需要一直在后台运行的业务时（如，后台播放音乐），可以使用长时任务机制。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.resourceschedule.backgroundTaskManager:backgroundTaskManager](arkts-backgroundtaskmanager.md)

<!--Device-unnamed-declare namespace backgroundTaskManager--><!--Device-unnamed-declare namespace backgroundTaskManager-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

## 汇总

### 函数

| 名称 |
| --- |
| [cancelSuspendDelay](arkts-backgroundtasks-backgroundtaskmanager-cancelsuspenddelay-depr-f.md#cancelsuspenddelay) |
| [getRemainingDelayTime](arkts-backgroundtasks-backgroundtaskmanager-getremainingdelaytime-depr-f.md#getremainingdelaytime) |
| [getRemainingDelayTime](arkts-backgroundtasks-backgroundtaskmanager-getremainingdelaytime-depr-f.md#getremainingdelaytime-1) |
| [requestSuspendDelay](arkts-backgroundtasks-backgroundtaskmanager-requestsuspenddelay-depr-f.md#requestsuspenddelay) |
| [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-depr-f.md#startbackgroundrunning) |
| [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-depr-f.md#startbackgroundrunning-1) |
| [stopBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-depr-f.md#stopbackgroundrunning) |
| [stopBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-depr-f.md#stopbackgroundrunning-1) |

### 接口

| 名称 |
| --- |
| [DelaySuspendInfo](arkts-backgroundtasks-backgroundtaskmanager-delaysuspendinfo-depr-i.md) |

### 枚举

| 名称 |
| --- |
| [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-depr-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-depr-e-sys.md) |
<!--DelEnd-->
