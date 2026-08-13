# @ohos.reminderAgentManager

本模块提供后台代理提醒的能力，即当应用被冻结或应用退出时，定时提醒功能将被系统服务代理。开发者可以调用本模块接口创建定时提醒，提醒类型支持倒计时、日历、闹钟三种。开发指导请参考 [代理提醒开发指南](../../../task-management/agent-powered-reminder.md)。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace reminderAgentManager--><!--Device-unnamed-declare namespace reminderAgentManager-End-->

**系统能力：** SystemCapability.Notification.ReminderAgent

## 汇总

### 函数

| 名称 |
| --- |
| [addExcludeDate](arkts-backgroundtasks-reminderagentmanager-addexcludedate-f.md#addExcludeDate) |
| [addNotificationSlot](arkts-backgroundtasks-reminderagentmanager-addnotificationslot-f.md#addNotificationSlot) |
| [addNotificationSlot](arkts-backgroundtasks-reminderagentmanager-addnotificationslot-f.md#addNotificationSlot) |
| [cancelAllReminders](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md#cancelAllReminders) |
| [cancelAllReminders](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md#cancelAllReminders) |
| [cancelReminder](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md#cancelReminder) |
| [cancelReminder](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md#cancelReminder) |
| [cancelReminderOnDisplay](arkts-backgroundtasks-reminderagentmanager-cancelreminderondisplay-f.md#cancelReminderOnDisplay) |
| [deleteExcludeDates](arkts-backgroundtasks-reminderagentmanager-deleteexcludedates-f.md#deleteExcludeDates) |
| [getAllValidReminders](arkts-backgroundtasks-reminderagentmanager-getallvalidreminders-f.md#getAllValidReminders) |
| [getExcludeDates](arkts-backgroundtasks-reminderagentmanager-getexcludedates-f.md#getExcludeDates) |
| [getValidReminders](arkts-backgroundtasks-reminderagentmanager-getvalidreminders-f.md#getValidReminders) |
| [getValidReminders](arkts-backgroundtasks-reminderagentmanager-getvalidreminders-f.md#getValidReminders) |
| [publishReminder](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md#publishReminder) |
| [publishReminder](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md#publishReminder) |
| [removeNotificationSlot](arkts-backgroundtasks-reminderagentmanager-removenotificationslot-f.md#removeNotificationSlot) |
| [removeNotificationSlot](arkts-backgroundtasks-reminderagentmanager-removenotificationslot-f.md#removeNotificationSlot) |
| [subscribeReminderState](arkts-backgroundtasks-reminderagentmanager-subscribereminderstate-f.md#subscribeReminderState) |
| [unsubscribeReminderState](arkts-backgroundtasks-reminderagentmanager-unsubscribereminderstate-f.md#unsubscribeReminderState) |
| [updateReminder](arkts-backgroundtasks-reminderagentmanager-updatereminder-f.md#updateReminder) |

### 接口

| 名称 |
| --- |
| [ActionButton](arkts-backgroundtasks-reminderagentmanager-actionbutton-i.md) |
| [LocalDateTime](arkts-backgroundtasks-reminderagentmanager-localdatetime-i.md) |
| [MaxScreenWantAgent](arkts-backgroundtasks-reminderagentmanager-maxscreenwantagent-i.md) |
| [NotificationRequestProxy](arkts-backgroundtasks-reminderagentmanager-notificationrequestproxy-i.md) |
| [ReminderInfo](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md) |
| [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) |
| [ReminderRequestAlarm](arkts-backgroundtasks-reminderagentmanager-reminderrequestalarm-i.md) |
| [ReminderRequestCalendar](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i.md) |
| [ReminderRequestTimer](arkts-backgroundtasks-reminderagentmanager-reminderrequesttimer-i.md) |
| [ReminderState](arkts-backgroundtasks-reminderagentmanager-reminderstate-i.md) |
| [WantAgent](arkts-backgroundtasks-reminderagentmanager-wantagent-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ActionButton](arkts-backgroundtasks-reminderagentmanager-actionbutton-i-sys.md) |
| [DataShareUpdate](arkts-backgroundtasks-reminderagentmanager-datashareupdate-i-sys.md) |
| [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i-sys.md) |
| [ReminderRequestCalendar](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ActionButtonType](arkts-backgroundtasks-reminderagentmanager-actionbuttontype-e.md) |
| [ReminderType](arkts-backgroundtasks-reminderagentmanager-remindertype-e.md) |
| [RingChannel](arkts-backgroundtasks-reminderagentmanager-ringchannel-e.md) |
| [TimeZoneType](arkts-backgroundtasks-reminderagentmanager-timezonetype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ActionButtonType](arkts-backgroundtasks-reminderagentmanager-actionbuttontype-e-sys.md) |
<!--DelEnd-->
