# @ohos.reminderAgent(Agent-powered Reminder)

The **reminderAgent** module provides APIs for publishing scheduled reminders through the reminder agent.You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm clocks. When the created reminders are published, the timing and pop-up notification functions of your application will be taken over by the reminder agent in the background when your application is frozen or exits.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager](arkts-reminderagentmanager.md)

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-addnotificationslot-f.md) |
| [addNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-addnotificationslot-f.md) |
| [cancelAllReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-cancelallreminders-f.md) |
| [cancelAllReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-cancelallreminders-f.md) |
| [cancelReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-cancelreminder-f.md) |
| [cancelReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-cancelreminder-f.md) |
| [getValidReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-getvalidreminders-f.md) |
| [getValidReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-getvalidreminders-f.md) |
| [publishReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-publishreminder-f.md) |
| [publishReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-publishreminder-f.md) |
| [removeNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-removenotificationslot-f.md) |
| [removeNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-removenotificationslot-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButton(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-actionbutton-i.md) |
| [LocalDateTime(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-localdatetime-i.md) |
| [MaxScreenWantAgent(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-maxscreenwantagent-i.md) |
| [ReminderRequest(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-reminderrequest-i.md) |
| [ReminderRequestAlarm(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-reminderrequestalarm-i.md) |
| [ReminderRequestCalendar(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-reminderrequestcalendar-i.md) |
| [ReminderRequestTimer(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-reminderrequesttimer-i.md) |
| [WantAgent(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-wantagent-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButtonType(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-actionbuttontype-e.md) |
| [ReminderType(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-remindertype-e.md) |
