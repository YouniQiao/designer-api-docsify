# @ohos.reminderAgentManager(Agent-powered Reminder)

The **reminderAgentManager** module provides APIs related to agent-powered reminders. When your application is frozen or exits, the application's scheduled notification capability will be taken over by a system service running in the background. You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm clocks. For details, see [Agent-powered Reminder](../../../task-management/agent-powered-reminder.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addExcludeDate(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-addexcludedate-f.md) |
| [addNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-addnotificationslot-f.md) |
| [addNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-addnotificationslot-f.md) |
| [cancelAllReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md) |
| [cancelAllReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md) |
| [cancelReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md) |
| [cancelReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md) |
| [cancelReminderOnDisplay(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-cancelreminderondisplay-f.md) |
| [deleteExcludeDates(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-deleteexcludedates-f.md) |
| [getAllValidReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-getallvalidreminders-f.md) |
| [getExcludeDates(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-getexcludedates-f.md) |
| [getValidReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-getvalidreminders-f.md) |
| [getValidReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-getvalidreminders-f.md) |
| [publishReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md) |
| [publishReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md) |
| [removeNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-removenotificationslot-f.md) |
| [removeNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-removenotificationslot-f.md) |
| [subscribeReminderState(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-subscribereminderstate-f.md) |
| [unsubscribeReminderState(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-unsubscribereminderstate-f.md) |
| [updateReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-updatereminder-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButton(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-actionbutton-i.md) |
| [LocalDateTime(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-localdatetime-i.md) |
| [MaxScreenWantAgent(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-maxscreenwantagent-i.md) |
| [NotificationRequestProxy(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-notificationrequestproxy-i.md) |
| [ReminderInfo(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-reminderinfo-i.md) |
| [ReminderRequest(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md) |
| [ReminderRequestAlarm(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-reminderrequestalarm-i.md) |
| [ReminderRequestCalendar(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i.md) |
| [ReminderRequestTimer(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-reminderrequesttimer-i.md) |
| [ReminderState(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-reminderstate-i.md) |
| [WantAgent(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-wantagent-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButton(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-actionbutton-i-sys.md) |
| [DataShareUpdate(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-datashareupdate-i-sys.md) |
| [ReminderRequest(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i-sys.md) |
| [ReminderRequestCalendar(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButtonType(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-actionbuttontype-e.md) |
| [ReminderType(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-remindertype-e.md) |
| [RingChannel(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-ringchannel-e.md) |
| [TimeZoneType(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-timezonetype-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButtonType(Agent-powered Reminder)](arkts-backgroundtasks-reminderagentmanager-actionbuttontype-e-sys.md) |
<!--DelEnd-->
