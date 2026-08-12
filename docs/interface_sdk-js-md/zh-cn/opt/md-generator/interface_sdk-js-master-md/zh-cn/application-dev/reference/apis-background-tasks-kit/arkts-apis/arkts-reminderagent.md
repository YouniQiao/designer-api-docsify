# @ohos.reminderAgent(后台代理提醒)

本模块提供后台代理提醒的能力。

开发应用时，开发者可以调用相关接口创建定时提醒，包括倒计时、日历、闹钟这三类提醒类型。使用后台代理提醒能力后，应用被冻结或退出后，计时和弹出提醒的功能将被后台系统服务代理。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [reminderAgentManager](arkts-reminderagentmanager.md#reminderAgentManager)

<!--Device-unnamed-declare namespace reminderAgent--><!--Device-unnamed-declare namespace reminderAgent-End-->

**系统能力：** SystemCapability.Notification.ReminderAgent

## 汇总

### 函数

| 名称 |
| --- |
| [addNotificationSlot](arkts-backgroundtasks-reminderagent-addnotificationslot-f.md#addnotificationslot) |
| [addNotificationSlot](arkts-backgroundtasks-reminderagent-addnotificationslot-f.md#addnotificationslot-1) |
| [cancelAllReminders](arkts-backgroundtasks-reminderagent-cancelallreminders-f.md#cancelallreminders) |
| [cancelAllReminders](arkts-backgroundtasks-reminderagent-cancelallreminders-f.md#cancelallreminders-1) |
| [cancelReminder](arkts-backgroundtasks-reminderagent-cancelreminder-f.md#cancelreminder) |
| [cancelReminder](arkts-backgroundtasks-reminderagent-cancelreminder-f.md#cancelreminder-1) |
| [getValidReminders](arkts-backgroundtasks-reminderagent-getvalidreminders-f.md#getvalidreminders) |
| [getValidReminders](arkts-backgroundtasks-reminderagent-getvalidreminders-f.md#getvalidreminders-1) |
| [publishReminder](arkts-backgroundtasks-reminderagent-publishreminder-f.md#publishreminder) |
| [publishReminder](arkts-backgroundtasks-reminderagent-publishreminder-f.md#publishreminder-1) |
| [removeNotificationSlot](arkts-backgroundtasks-reminderagent-removenotificationslot-f.md#removenotificationslot) |
| [removeNotificationSlot](arkts-backgroundtasks-reminderagent-removenotificationslot-f.md#removenotificationslot-1) |

### 接口

| 名称 |
| --- |
| [ActionButton](arkts-backgroundtasks-reminderagent-actionbutton-i.md) |
| [LocalDateTime](arkts-backgroundtasks-reminderagent-localdatetime-i.md) |
| [MaxScreenWantAgent](arkts-backgroundtasks-reminderagent-maxscreenwantagent-i.md) |
| [ReminderRequest](arkts-backgroundtasks-reminderagent-reminderrequest-i.md) |
| [ReminderRequestAlarm](arkts-backgroundtasks-reminderagent-reminderrequestalarm-i.md) |
| [ReminderRequestCalendar](arkts-backgroundtasks-reminderagent-reminderrequestcalendar-i.md) |
| [ReminderRequestTimer](arkts-backgroundtasks-reminderagent-reminderrequesttimer-i.md) |
| [WantAgent](arkts-backgroundtasks-reminderagent-wantagent-i.md) |

### 枚举

| 名称 |
| --- |
| [ActionButtonType](arkts-backgroundtasks-reminderagent-actionbuttontype-e.md) |
| [ReminderType](arkts-backgroundtasks-reminderagent-remindertype-e.md) |
