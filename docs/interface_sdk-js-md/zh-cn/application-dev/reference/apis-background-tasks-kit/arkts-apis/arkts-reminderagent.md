# @ohos.reminderAgent(后台代理提醒)

本模块提供后台代理提醒的能力。开发应用时，开发者可以调用相关接口创建定时提醒，包括倒计时、日历、闹钟这三类提醒类型。使用后台代理提醒能力后，应用被冻结或退出后，计时和弹出提醒的功能将被后台系统服务代理。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [reminderAgentManager](arkts-reminderagentmanager.md)

**系统能力：** SystemCapability.Notification.ReminderAgent

## 导入模块

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addNotificationSlot(后台代理提醒)](arkts-backgroundtasks-reminderagent-addnotificationslot-f.md) |
| [addNotificationSlot(后台代理提醒)](arkts-backgroundtasks-reminderagent-addnotificationslot-f.md) |
| [cancelAllReminders(后台代理提醒)](arkts-backgroundtasks-reminderagent-cancelallreminders-f.md) |
| [cancelAllReminders(后台代理提醒)](arkts-backgroundtasks-reminderagent-cancelallreminders-f.md) |
| [cancelReminder(后台代理提醒)](arkts-backgroundtasks-reminderagent-cancelreminder-f.md) |
| [cancelReminder(后台代理提醒)](arkts-backgroundtasks-reminderagent-cancelreminder-f.md) |
| [getValidReminders(后台代理提醒)](arkts-backgroundtasks-reminderagent-getvalidreminders-f.md) |
| [getValidReminders(后台代理提醒)](arkts-backgroundtasks-reminderagent-getvalidreminders-f.md) |
| [publishReminder(后台代理提醒)](arkts-backgroundtasks-reminderagent-publishreminder-f.md) |
| [publishReminder(后台代理提醒)](arkts-backgroundtasks-reminderagent-publishreminder-f.md) |
| [removeNotificationSlot(后台代理提醒)](arkts-backgroundtasks-reminderagent-removenotificationslot-f.md) |
| [removeNotificationSlot(后台代理提醒)](arkts-backgroundtasks-reminderagent-removenotificationslot-f.md) |

### 接口

| 名称 |
| --- |
| [ActionButton(后台代理提醒)](arkts-backgroundtasks-reminderagent-actionbutton-i.md) |
| [LocalDateTime(后台代理提醒)](arkts-backgroundtasks-reminderagent-localdatetime-i.md) |
| [MaxScreenWantAgent(后台代理提醒)](arkts-backgroundtasks-reminderagent-maxscreenwantagent-i.md) |
| [ReminderRequest(后台代理提醒)](arkts-backgroundtasks-reminderagent-reminderrequest-i.md) |
| [ReminderRequestAlarm(后台代理提醒)](arkts-backgroundtasks-reminderagent-reminderrequestalarm-i.md) |
| [ReminderRequestCalendar(后台代理提醒)](arkts-backgroundtasks-reminderagent-reminderrequestcalendar-i.md) |
| [ReminderRequestTimer(后台代理提醒)](arkts-backgroundtasks-reminderagent-reminderrequesttimer-i.md) |
| [WantAgent(后台代理提醒)](arkts-backgroundtasks-reminderagent-wantagent-i.md) |

### 枚举

| 名称 |
| --- |
| [ActionButtonType(后台代理提醒)](arkts-backgroundtasks-reminderagent-actionbuttontype-e.md) |
| [ReminderType(后台代理提醒)](arkts-backgroundtasks-reminderagent-remindertype-e.md) |
