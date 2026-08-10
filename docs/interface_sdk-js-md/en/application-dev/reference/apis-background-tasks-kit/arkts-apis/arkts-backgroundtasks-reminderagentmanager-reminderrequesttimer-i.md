# ReminderRequestTimer

ReminderRequestTimer extends ReminderRequest

倒计时实例对象，用于设置提醒的时间。

**Inheritance/Implementation:** ReminderRequestTimer extends [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface ReminderRequestTimer extends ReminderRequest--><!--Device-reminderAgentManager-interface ReminderRequestTimer extends ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## repeatCount

```TypeScript
repeatCount?: int
```

重复次数，默认值为0，无限次重复。需和repeatInterval一起使用。

范围：[0, +∞)。超出范围返回错误码401。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReminderRequestTimer-repeatCount?: int--><!--Device-ReminderRequestTimer-repeatCount?: int-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## repeatInterval

```TypeScript
repeatInterval?: long
```

重复周期，无默认值，未赋值时，无重复周期。需和repeatCount一起使用。

单位：s，范围：[86400, +∞)。超出范围返回错误码401。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReminderRequestTimer-repeatInterval?: long--><!--Device-ReminderRequestTimer-repeatInterval?: long-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## triggerTimeInSeconds

```TypeScript
triggerTimeInSeconds: long
```

指明倒计时的秒数。

单位：s

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ReminderRequestTimer-triggerTimeInSeconds: long--><!--Device-ReminderRequestTimer-triggerTimeInSeconds: long-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

