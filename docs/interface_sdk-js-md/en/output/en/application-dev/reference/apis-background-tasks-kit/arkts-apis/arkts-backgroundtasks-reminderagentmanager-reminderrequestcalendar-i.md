# ReminderRequestCalendar

ReminderRequestCalendar extends ReminderRequest Defines a reminder for a calendar event.

**Inheritance/Implementation:** ReminderRequestCalendar extends [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface ReminderRequestCalendar extends ReminderRequest--><!--Device-reminderAgentManager-interface ReminderRequestCalendar extends ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## dateTime

```TypeScript
dateTime: LocalDateTime
```

Reminder time.

**Type:** LocalDateTime

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ReminderRequestCalendar-dateTime: LocalDateTime--><!--Device-ReminderRequestCalendar-dateTime: LocalDateTime-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## daysOfWeek

```TypeScript
daysOfWeek?: Array<int>
```

Days of a week when the reminder repeats. The value ranges from 1 to 7, corresponding to the data from Monday to Sunday. This parameter is left empty by default.

**Type:** Array&lt;int&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ReminderRequestCalendar-daysOfWeek?: Array<int>--><!--Device-ReminderRequestCalendar-daysOfWeek?: Array<int>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## endDateTime

```TypeScript
endDateTime?: LocalDateTime
```

End time of the reminder.

**Type:** LocalDateTime

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ReminderRequestCalendar-endDateTime?: LocalDateTime--><!--Device-ReminderRequestCalendar-endDateTime?: LocalDateTime-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatDays

```TypeScript
repeatDays?: Array<int>
```

Day in which the reminder repeats. The value range is [1, 31]. This parameter is left empty by default. This parameter must be used together with **repeatMonths**.

**Type:** Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ReminderRequestCalendar-repeatDays?: Array<int>--><!--Device-ReminderRequestCalendar-repeatDays?: Array<int>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatMonths

```TypeScript
repeatMonths?: Array<int>
```

Month in which the reminder repeats. The value range is [1, 12]. This parameter is left empty by default. This parameter must be used together with **repeatDays**.

**Type:** Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ReminderRequestCalendar-repeatMonths?: Array<int>--><!--Device-ReminderRequestCalendar-repeatMonths?: Array<int>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

