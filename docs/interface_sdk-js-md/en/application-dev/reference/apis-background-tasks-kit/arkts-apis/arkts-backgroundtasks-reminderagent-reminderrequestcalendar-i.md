# ReminderRequestCalendar

Defines a reminder for a calendar event.

**Inheritance/Implementation:** ReminderRequestCalendar extends [ReminderRequest](arkts-backgroundtasks-reminderagent-reminderrequest-i.md#ReminderRequest)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [ReminderRequestCalendar](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i.md#ReminderRequestCalendar)

<!--Device-reminderAgent-interface ReminderRequestCalendar extends ReminderRequest--><!--Device-reminderAgent-interface ReminderRequestCalendar extends ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgent } from '@kit.BackgroundTasksKit';
```

## dateTime

```TypeScript
dateTime: LocalDateTime
```

Reminder time.

**Type:** LocalDateTime

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [dateTime](reminderAgentManager.ReminderRequestCalendar.dateTime)

<!--Device-ReminderRequestCalendar-dateTime: LocalDateTime--><!--Device-ReminderRequestCalendar-dateTime: LocalDateTime-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatDays

```TypeScript
repeatDays?: Array<number>
```

Date on which the reminder repeats.

**Type:** Array&lt;number&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [repeatDays](reminderAgentManager.ReminderRequestCalendar.repeatDays)

<!--Device-ReminderRequestCalendar-repeatDays?: Array<number>--><!--Device-ReminderRequestCalendar-repeatDays?: Array<number>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatMonths

```TypeScript
repeatMonths?: Array<number>
```

Month in which the reminder repeats.

**Type:** Array&lt;number&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [repeatMonths](reminderAgentManager.ReminderRequestCalendar.repeatMonths)

<!--Device-ReminderRequestCalendar-repeatMonths?: Array<number>--><!--Device-ReminderRequestCalendar-repeatMonths?: Array<number>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

