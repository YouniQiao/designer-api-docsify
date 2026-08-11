# @ohos.reminderAgentManager(Agent-powered Reminder)

The **reminderAgentManager** module provides APIs related to agent-powered reminders. When your application is frozen or exits, the application's scheduled notification capability will be taken over by a system service running in the background. You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm clocks. For details, see [Agent-powered Reminder](../../../task-management/agent-powered-reminder.md).

**Since:** 9

<!--Device-unnamed-declare namespace reminderAgentManager--><!--Device-unnamed-declare namespace reminderAgentManager-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addExcludeDate](arkts-backgroundtasks-reminderagentmanager-addexcludedate-f.md#addexcludedate) |
| [addNotificationSlot](arkts-backgroundtasks-reminderagentmanager-addnotificationslot-f.md#addnotificationslot) |
| [addNotificationSlot](arkts-backgroundtasks-reminderagentmanager-addnotificationslot-f.md#addnotificationslot-1) |
| [cancelAllReminders](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md#cancelallreminders) |
| [cancelAllReminders](arkts-backgroundtasks-reminderagentmanager-cancelallreminders-f.md#cancelallreminders-1) |
| [cancelReminder](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md#cancelreminder) |
| [cancelReminder](arkts-backgroundtasks-reminderagentmanager-cancelreminder-f.md#cancelreminder-1) |
| [cancelReminderOnDisplay](arkts-backgroundtasks-reminderagentmanager-cancelreminderondisplay-f.md#cancelreminderondisplay) |
| [deleteExcludeDates](arkts-backgroundtasks-reminderagentmanager-deleteexcludedates-f.md#deleteexcludedates) |
| [getAllValidReminders](arkts-backgroundtasks-reminderagentmanager-getallvalidreminders-f.md#getallvalidreminders) |
| [getExcludeDates](arkts-backgroundtasks-reminderagentmanager-getexcludedates-f.md#getexcludedates) |
| [getValidReminders](arkts-backgroundtasks-reminderagentmanager-getvalidreminders-f.md#getvalidreminders) |
| [getValidReminders](arkts-backgroundtasks-reminderagentmanager-getvalidreminders-f.md#getvalidreminders-1) |
| [publishReminder](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md#publishreminder) |
| [publishReminder](arkts-backgroundtasks-reminderagentmanager-publishreminder-f.md#publishreminder-1) |
| [removeNotificationSlot](arkts-backgroundtasks-reminderagentmanager-removenotificationslot-f.md#removenotificationslot) |
| [removeNotificationSlot](arkts-backgroundtasks-reminderagentmanager-removenotificationslot-f.md#removenotificationslot-1) |
| [subscribeReminderState](arkts-backgroundtasks-reminderagentmanager-subscribereminderstate-f.md#subscribereminderstate) |
| [unsubscribeReminderState](arkts-backgroundtasks-reminderagentmanager-unsubscribereminderstate-f.md#unsubscribereminderstate) |
| [updateReminder](arkts-backgroundtasks-reminderagentmanager-updatereminder-f.md#updatereminder) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButton](arkts-backgroundtasks-reminderagentmanager-actionbutton-i-sys.md) |
| [DataShareUpdate](arkts-backgroundtasks-reminderagentmanager-datashareupdate-i-sys.md) |
| [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i-sys.md) |
| [ReminderRequestCalendar](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButtonType](arkts-backgroundtasks-reminderagentmanager-actionbuttontype-e.md) |
| [ReminderType](arkts-backgroundtasks-reminderagentmanager-remindertype-e.md) |
| [RingChannel](arkts-backgroundtasks-reminderagentmanager-ringchannel-e.md) |
| [TimeZoneType](arkts-backgroundtasks-reminderagentmanager-timezonetype-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ActionButtonType](arkts-backgroundtasks-reminderagentmanager-actionbuttontype-e-sys.md) |
<!--DelEnd-->
