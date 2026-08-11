# ReminderRequestCalendar

ReminderRequestCalendar extends ReminderRequest

Defines a reminder for a calendar event.

**Inheritance/Implementation:** ReminderRequestCalendar extends [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface ReminderRequestCalendar extends ReminderRequest--><!--Device-reminderAgentManager-interface ReminderRequestCalendar extends ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## rruleWantAgent

```TypeScript
rruleWantAgent?: WantAgent
```

Custom reminder, which specifies the ServiceExtensionAbility to start.

**Type:** [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ReminderRequestCalendar-rruleWantAgent?: WantAgent--><!--Device-ReminderRequestCalendar-rruleWantAgent?: WantAgent-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**System API:** This is a system API.

