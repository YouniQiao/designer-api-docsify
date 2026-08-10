# ReminderRequestCalendar

日历实例对象，用于设置提醒的时间。

**Inheritance/Implementation:** ReminderRequestCalendar extends [ReminderRequest](arkts-backgroundtasks-reminderagent-reminderrequest-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.reminderAgentManager:reminderAgentManager.ReminderRequestCalendar](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i.md)

<!--Device-reminderAgent-interface ReminderRequestCalendar extends ReminderRequest--><!--Device-reminderAgent-interface ReminderRequestCalendar extends ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## dateTime

```TypeScript
dateTime: LocalDateTime
```

指明提醒的目标时间。

**Type:** [LocalDateTime](arkts-backgroundtasks-reminderagentmanager-localdatetime-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequestCalendar.dateTime](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i.md#datetime)

<!--Device-ReminderRequestCalendar-dateTime: LocalDateTime--><!--Device-ReminderRequestCalendar-dateTime: LocalDateTime-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatDays

```TypeScript
repeatDays?: Array<number>
```

指明重复提醒的日期。

**Type:** Array&lt;number&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequestCalendar.repeatDays](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i.md#repeatdays)

<!--Device-ReminderRequestCalendar-repeatDays?: Array<number>--><!--Device-ReminderRequestCalendar-repeatDays?: Array<number>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatMonths

```TypeScript
repeatMonths?: Array<number>
```

指明重复提醒的月份。

**Type:** Array&lt;number&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequestCalendar.repeatMonths](arkts-backgroundtasks-reminderagentmanager-reminderrequestcalendar-i.md#repeatmonths)

<!--Device-ReminderRequestCalendar-repeatMonths?: Array<number>--><!--Device-ReminderRequestCalendar-repeatMonths?: Array<number>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

