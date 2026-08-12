# ReminderRequestTimer

Defines a reminder for a scheduled timer.

**Inheritance/Implementation:** ReminderRequestTimer extends [ReminderRequest](arkts-backgroundtasks-reminderagent-reminderrequest-i.md#ReminderRequest)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [ReminderRequestTimer](arkts-backgroundtasks-reminderagentmanager-reminderrequesttimer-i.md#ReminderRequestTimer)

<!--Device-reminderAgent-interface ReminderRequestTimer extends ReminderRequest--><!--Device-reminderAgent-interface ReminderRequestTimer extends ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgent } from '@kit.BackgroundTasksKit';
```

## triggerTimeInSeconds

```TypeScript
triggerTimeInSeconds: number
```

Number of seconds in the countdown timer.Unit: s.

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [triggerTimeInSeconds](reminderAgentManager.ReminderRequestTimer.triggerTimeInSeconds)

<!--Device-ReminderRequestTimer-triggerTimeInSeconds: number--><!--Device-ReminderRequestTimer-triggerTimeInSeconds: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

