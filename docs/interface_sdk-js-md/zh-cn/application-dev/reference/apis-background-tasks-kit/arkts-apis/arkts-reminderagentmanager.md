# @ohos.reminderAgentManager(后台代理提醒)

本模块提供后台代理提醒的能力，即当应用被冻结或应用退出时，定时提醒功能将被系统服务代理。开发者可以调用本模块接口创建定时提醒，提醒类型支持倒计时、日历、闹钟三种。开发指导请参考 [代理提醒开发指南](../../../task-management/agent-powered-reminder.md)。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Notification.ReminderAgent

## 导入模块

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addExcludeDate(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-addexcludedate-f.md) |
| [addNotificationSlot(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-addnotificationslot-f.md) |
| [addNotificationSlot(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-addnotificationslot-f.md) |
| [cancelAllReminders(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md) |
| [cancelAllReminders(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md) |
| [cancelReminder(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md) |
| [cancelReminder(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md) |
| [cancelReminderOnDisplay(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-cancelreminderondisplay-f.md) |
| [deleteExcludeDates(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-deleteexcludedates-f.md) |
| [getAllValidReminders(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-getallvalidreminders-f.md) |
| [getExcludeDates(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-getexcludedates-f.md) |
| [getValidReminders(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-getvalidreminders-f.md) |
| [getValidReminders(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-getvalidreminders-f.md) |
| [publishReminder(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md) |
| [publishReminder(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md) |
| [removeNotificationSlot(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-removenotificationslot-f.md) |
| [removeNotificationSlot(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-removenotificationslot-f.md) |
| [subscribeReminderState(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-subscribereminderstate-f.md) |
| [unsubscribeReminderState(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-unsubscribereminderstate-f.md) |
| [updateReminder(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-updatereminder-f.md) |

### 接口

| 名称 |
| --- |
| [ActionButton(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-actionbutton-i.md) |
| [LocalDateTime(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-localdatetime-i.md) |
| [MaxScreenWantAgent(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-maxscreenwantagent-i.md) |
| [NotificationRequestProxy(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-notificationrequestproxy-i.md) |
| [ReminderInfo(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md) |
| [ReminderRequest(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) |
| [ReminderRequestAlarm(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-reminderrequestalarm-i.md) |
| [ReminderRequestCalendar(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i.md) |
| [ReminderRequestTimer(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-reminderrequesttimer-i.md) |
| [ReminderState(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-reminderstate-i.md) |
| [WantAgent(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-wantagent-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ActionButton(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-actionbutton-i-sys.md) |
| [DataShareUpdate(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-datashareupdate-i-sys.md) |
| [ReminderRequest(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i-sys.md) |
| [ReminderRequestCalendar(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ActionButtonType(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-actionbuttontype-e.md) |
| [ReminderType(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-remindertype-e.md) |
| [RingChannel(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-ringchannel-e.md) |
| [TimeZoneType(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-timezonetype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ActionButtonType(后台代理提醒)](arkts-backgroundtasks-reminderagentmanager-actionbuttontype-e-sys.md) |
<!--DelEnd-->
