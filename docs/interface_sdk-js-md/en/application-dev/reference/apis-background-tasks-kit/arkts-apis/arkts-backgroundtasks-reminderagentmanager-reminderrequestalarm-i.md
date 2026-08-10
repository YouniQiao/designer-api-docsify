# ReminderRequestAlarm

ReminderRequestAlarm extends ReminderRequest

闹钟实例对象，用于设置提醒的时间。

**Inheritance/Implementation:** ReminderRequestAlarm extends [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface ReminderRequestAlarm extends ReminderRequest--><!--Device-reminderAgentManager-interface ReminderRequestAlarm extends ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## daysOfWeek

```TypeScript
daysOfWeek?: Array<int>
```

指明每周哪几天需要重复提醒。范围为周一到周日，对应数字为1到7，默认为空。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ReminderRequestAlarm-daysOfWeek?: Array<int>--><!--Device-ReminderRequestAlarm-daysOfWeek?: Array<int>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## hour

```TypeScript
hour: int
```

指明提醒的目标时刻，范围：[0, 23]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ReminderRequestAlarm-hour: int--><!--Device-ReminderRequestAlarm-hour: int-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## minute

```TypeScript
minute: int
```

指明提醒的目标分钟，范围：[0, 59]。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ReminderRequestAlarm-minute: int--><!--Device-ReminderRequestAlarm-minute: int-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

