# @ohos.reminderAgent(Agent-powered Reminder)

The **reminderAgent** module provides APIs for publishing scheduled reminders through the reminder agent.

You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm clocks. When the created reminders are published, the timing and pop-up notification functions of your application will be taken over by the reminder agent in the background when your application is frozen or exits.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager](arkts-reminderagentmanager.md#reminderAgentManager)

<!--Device-unnamed-declare namespace reminderAgent--><!--Device-unnamed-declare namespace reminderAgent-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgent } from '@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButton](arkts-backgroundtasks-reminderagent-actionbutton-i.md) |
| [LocalDateTime](arkts-backgroundtasks-reminderagent-localdatetime-i.md) |
| [MaxScreenWantAgent](arkts-backgroundtasks-reminderagent-maxscreenwantagent-i.md) |
| [ReminderRequest](arkts-backgroundtasks-reminderagent-reminderrequest-i.md) |
| [ReminderRequestAlarm](arkts-backgroundtasks-reminderagent-reminderrequestalarm-i.md) |
| [ReminderRequestCalendar](arkts-backgroundtasks-reminderagent-reminderrequestcalendar-i.md) |
| [ReminderRequestTimer](arkts-backgroundtasks-reminderagent-reminderrequesttimer-i.md) |
| [WantAgent](arkts-backgroundtasks-reminderagent-wantagent-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButtonType](arkts-backgroundtasks-reminderagent-actionbuttontype-e.md) |
| [ReminderType](arkts-backgroundtasks-reminderagent-remindertype-e.md) |
