# @ohos.reminderAgentManager

The **reminderAgentManager** module provides APIs related to agent-powered reminders. When your application is frozen or exits, the application's scheduled notification capability will be taken over by a system service running in the background. You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm clocks. For details, see [Agent-powered Reminder](../../../task-management/agent-powered-reminder.md).

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace reminderAgentManager--><!--Device-unnamed-declare namespace reminderAgentManager-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
