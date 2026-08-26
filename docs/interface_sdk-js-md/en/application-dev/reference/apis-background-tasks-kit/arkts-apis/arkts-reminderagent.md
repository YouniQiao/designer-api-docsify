# @ohos.reminderAgent(Agent-powered Reminder)

The **reminderAgent** module provides APIs for publishing scheduled reminders through the reminder agent.You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm clocks. When the created reminders are published, the timing and pop-up notification functions of your application will be taken over by the reminder agent in the background when your application is frozen or exits.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager](arkts-reminderagentmanager.md)

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import reminderAgent from '@kit.BackgroundTasksKit';
import reminderAgentManager from '@kit.BackgroundTasksKitManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-addnotificationslot-f.md) | Adds a notification slot. This API uses an asynchronous callback to return the result. |
| [addNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-addnotificationslot-f.md) | Adds a notification slot. This API uses a promise to return the result. |
| [cancelAllReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-cancelallreminders-f.md) | Cancels all reminders set by the current application. This API uses an asynchronous callback to return the cancellation result. |
| [cancelAllReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-cancelallreminders-f.md) | Cancels all reminders set by the current application. This API uses a promise to return the cancellation result. |
| [cancelReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-cancelreminder-f.md) | Cancels the reminder with the specified ID. This API uses an asynchronous callback to return the cancellation result. |
| [cancelReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-cancelreminder-f.md) | Cancels the reminder with the specified ID. This API uses a promise to return the cancellation result. |
| [getValidReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-getvalidreminders-f.md) | Obtains all valid (not yet expired) reminders set by the current application. This API uses an asynchronous callback to return the result. |
| [getValidReminders(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-getvalidreminders-f.md) | Obtains all valid (not yet expired) reminders set by the current application. This API uses a promise to return the reminders. |
| [publishReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-publishreminder-f.md) | Publishes a reminder through the reminder agent. This API uses an asynchronous callback to return the result. It can be called only when notification is enabled for the application through [Notification.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification) |
| [publishReminder(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-publishreminder-f.md) | Publishes a reminder through the reminder agent. This API uses a promise to return the result. It can be called only when notification is enabled for the application through [Notification.requestEnableNotification](../../apis-notification-kit/arkts-apis/arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification) |
| [removeNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-removenotificationslot-f.md) | Removes a notification slot of a specified type. This API uses an asynchronous callback to return the result. |
| [removeNotificationSlot(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-removenotificationslot-f.md) | Removes a notification slot of a specified type. This API uses a promise to return the result. |

### Interfaces

| Name | Description |
| --- | --- |
| [ActionButton(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-actionbutton-i.md) | Defines a button displayed in the reminder notification. |
| [LocalDateTime(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-localdatetime-i.md) | Sets the time information for a calendar reminder. |
| [MaxScreenWantAgent(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-maxscreenwantagent-i.md) | Provides the information about the target package and ability to start automatically when the reminder is displayed in full-screen mode. This API is reserved. |
| [ReminderRequest(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-reminderrequest-i.md) | Defines the reminder to publish. |
| [ReminderRequestAlarm(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-reminderrequestalarm-i.md) | Defines a reminder for an alarm. |
| [ReminderRequestCalendar(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-reminderrequestcalendar-i.md) | Defines a reminder for a calendar event. |
| [ReminderRequestTimer(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-reminderrequesttimer-i.md) | Defines a reminder for a scheduled timer. |
| [WantAgent(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-wantagent-i.md) | Sets the package and ability that are redirected to when the reminder notification is clicked. |

### Enums

| Name | Description |
| --- | --- |
| [ActionButtonType(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-actionbuttontype-e.md) | Enumerates the button types. |
| [ReminderType(Agent-powered Reminder)](arkts-backgroundtasks-reminderagent-remindertype-e.md) | Enumerates reminder types. |
