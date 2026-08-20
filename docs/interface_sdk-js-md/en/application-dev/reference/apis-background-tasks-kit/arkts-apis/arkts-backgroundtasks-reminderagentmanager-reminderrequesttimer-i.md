# ReminderRequestTimer

ReminderRequestTimer extends ReminderRequest

Defines a reminder for a scheduled timer.

**Inheritance/Implementation:** ReminderRequestTimer extends [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md)

**Since:** 23

<!--Device-reminderAgentManager-interface ReminderRequestTimer--><!--Device-reminderAgentManager-interface ReminderRequestTimer-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## repeatCount

```TypeScript
repeatCount?: int
```

Number of repetitions. The default value is **0**, indicating infinite repetitions. This parameter must be used together with **repeatInterval**.

The value range is [0, +∞). If the value is out of range, error code 401 is returned.

**Type:** int

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReminderRequestTimer-repeatCount?: int--><!--Device-ReminderRequestTimer-repeatCount?: int-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatInterval

```TypeScript
repeatInterval?: long
```

Repeat interval. There is no default value. If no value is set, there is no repeat interval. This parameter must be used together with **repeatCount**.

The value range is [86400, +∞), in seconds. If the value is out of range, error code 401 is returned.

**Type:** long

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReminderRequestTimer-repeatInterval?: long--><!--Device-ReminderRequestTimer-repeatInterval?: long-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## triggerTimeInSeconds

```TypeScript
triggerTimeInSeconds: long
```

Number of seconds in the countdown timer.

Unit: s

**Type:** long

**Since:** 23

<!--Device-ReminderRequestTimer-triggerTimeInSeconds: long--><!--Device-ReminderRequestTimer-triggerTimeInSeconds: long-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

