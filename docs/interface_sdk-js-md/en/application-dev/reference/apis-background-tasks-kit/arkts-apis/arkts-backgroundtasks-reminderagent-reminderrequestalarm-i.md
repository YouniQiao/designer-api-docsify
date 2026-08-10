# ReminderRequestAlarm

闹钟实例对象，用于设置提醒的时间。

**Inheritance/Implementation:** ReminderRequestAlarm extends [ReminderRequest](arkts-backgroundtasks-reminderagent-reminderrequest-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.reminderAgentManager:reminderAgentManager.ReminderRequestAlarm](arkts-backgroundtasks-reminderagentmanager-reminderrequestalarm-i.md)

<!--Device-reminderAgent-interface ReminderRequestAlarm extends ReminderRequest--><!--Device-reminderAgent-interface ReminderRequestAlarm extends ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## daysOfWeek

```TypeScript
daysOfWeek?: Array<number>
```

指明每周哪几天需要重复提醒。范围为周一到周末，对应数字为1到7。

**Type:** Array&lt;number&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequestAlarm.daysOfWeek](arkts-backgroundtasks-reminderagentmanager-reminderrequestalarm-i.md#daysofweek)

<!--Device-ReminderRequestAlarm-daysOfWeek?: Array<number>--><!--Device-ReminderRequestAlarm-daysOfWeek?: Array<number>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## hour

```TypeScript
hour: number
```

指明提醒的目标时刻。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequestAlarm.hour](arkts-backgroundtasks-reminderagentmanager-reminderrequestalarm-i.md#hour)

<!--Device-ReminderRequestAlarm-hour: number--><!--Device-ReminderRequestAlarm-hour: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## minute

```TypeScript
minute: number
```

指明提醒的目标分钟。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequestAlarm.minute](arkts-backgroundtasks-reminderagentmanager-reminderrequestalarm-i.md#minute)

<!--Device-ReminderRequestAlarm-minute: number--><!--Device-ReminderRequestAlarm-minute: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

