# ReminderRequestAlarm

Defines a reminder for an alarm.

**Inheritance/Implementation:** ReminderRequestAlarm extends [ReminderRequest](arkts-backgroundtasks-reminderagent-reminderrequest-i.md#ReminderRequest)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [ReminderRequestAlarm](arkts-backgroundtasks-reminderagentmanager-reminderrequestalarm-i.md#ReminderRequestAlarm)

<!--Device-reminderAgent-interface ReminderRequestAlarm--><!--Device-reminderAgent-interface ReminderRequestAlarm-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgent } from '@kit.BackgroundTasksKit';
```

## daysOfWeek

```TypeScript
daysOfWeek?: Array<number>
```

Days of a week when the reminder repeats. The value ranges from 1 to 7, corresponding to the data from Monday to Sunday.

**Type:** Array&lt;number&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** daysOfWeek

<!--Device-ReminderRequestAlarm-daysOfWeek?: Array<number>--><!--Device-ReminderRequestAlarm-daysOfWeek?: Array<number>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## hour

```TypeScript
hour: number
```

Hour portion of the reminder time.

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** hour

<!--Device-ReminderRequestAlarm-hour: number--><!--Device-ReminderRequestAlarm-hour: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## minute

```TypeScript
minute: number
```

Minute portion of the reminder time.

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** minute

<!--Device-ReminderRequestAlarm-minute: number--><!--Device-ReminderRequestAlarm-minute: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

