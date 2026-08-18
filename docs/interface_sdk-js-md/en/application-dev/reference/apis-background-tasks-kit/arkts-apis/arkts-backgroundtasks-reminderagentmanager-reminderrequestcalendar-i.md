# ReminderRequestCalendar

ReminderRequestCalendar extends ReminderRequest Defines a reminder for a calendar event.

**Inheritance/Implementation:** ReminderRequestCalendar extends [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#reminderrequest)

**Since:** 23

<!--Device-reminderAgentManager-interface ReminderRequestCalendar--><!--Device-reminderAgentManager-interface ReminderRequestCalendar-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## dateTime

```TypeScript
dateTime: LocalDateTime
```

Reminder time.

**Type:** LocalDateTime

**Since:** 23

<!--Device-ReminderRequestCalendar-dateTime: LocalDateTime--><!--Device-ReminderRequestCalendar-dateTime: LocalDateTime-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## daysOfWeek

```TypeScript
daysOfWeek?: Array<int>
```

Days of a week when the reminder repeats. The value ranges from 1 to 7, corresponding to the data from Monday to Sunday. This parameter is left empty by default.

**Type:** Array&lt;int&gt;

**Since:** 23

<!--Device-ReminderRequestCalendar-daysOfWeek?: Array<int>--><!--Device-ReminderRequestCalendar-daysOfWeek?: Array<int>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## endDateTime

```TypeScript
endDateTime?: LocalDateTime
```

End time of the reminder.

**Type:** LocalDateTime

**Since:** 23

<!--Device-ReminderRequestCalendar-endDateTime?: LocalDateTime--><!--Device-ReminderRequestCalendar-endDateTime?: LocalDateTime-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatDays

```TypeScript
repeatDays?: Array<int>
```

Day in which the reminder repeats. The value range is [1, 31]. This parameter is left empty by default. This parameter must be used together with **repeatMonths**.

**Type:** Array&lt;int&gt;

**Since:** 23

<!--Device-ReminderRequestCalendar-repeatDays?: Array<int>--><!--Device-ReminderRequestCalendar-repeatDays?: Array<int>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatMonths

```TypeScript
repeatMonths?: Array<int>
```

Month in which the reminder repeats. The value range is [1, 12]. This parameter is left empty by default. This parameter must be used together with **repeatDays**.

**Type:** Array&lt;int&gt;

**Since:** 23

<!--Device-ReminderRequestCalendar-repeatMonths?: Array<int>--><!--Device-ReminderRequestCalendar-repeatMonths?: Array<int>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

