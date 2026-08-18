# ReminderRequest

Defines the reminder to publish.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md)

<!--Device-reminderAgent-interface ReminderRequest--><!--Device-reminderAgent-interface ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgent } from '@kit.BackgroundTasksKit';
import { reminderAgentManager } from '@kit.BackgroundTasksKit';
```

## actionButton

```TypeScript
actionButton?: [ActionButton?, ActionButton?]
```

Button displayed in the reminder notification. (The parameter is optional. Up to two buttons are supported.)

**Type:** [ActionButton?, ActionButton?]

**Since:** 7

**Deprecated since:** 9

**Substitutes:** actionButton

<!--Device-ReminderRequest-actionButton?: [ActionButton?, ActionButton?]--><!--Device-ReminderRequest-actionButton?: [ActionButton?, ActionButton?]-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## content

```TypeScript
content?: string
```

Reminder content.

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** content

<!--Device-ReminderRequest-content?: string--><!--Device-ReminderRequest-content?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## expiredContent

```TypeScript
expiredContent?: string
```

Content to be displayed after the reminder expires.

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** expiredContent

<!--Device-ReminderRequest-expiredContent?: string--><!--Device-ReminderRequest-expiredContent?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## maxScreenWantAgent

```TypeScript
maxScreenWantAgent?: MaxScreenWantAgent
```

Information about the ability that is automatically started when the reminder arrives. If the device is in use, a notification will be displayed.

**Type:** MaxScreenWantAgent

**Since:** 7

**Deprecated since:** 9

**Substitutes:** maxScreenWantAgent

<!--Device-ReminderRequest-maxScreenWantAgent?: MaxScreenWantAgent--><!--Device-ReminderRequest-maxScreenWantAgent?: MaxScreenWantAgent-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## notificationId

```TypeScript
notificationId?: number
```

Notification ID used by the reminder. If there are reminders with the same notification ID, the later one will overwrite the earlier one.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** notificationId

<!--Device-ReminderRequest-notificationId?: number--><!--Device-ReminderRequest-notificationId?: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## reminderType

```TypeScript
reminderType: ReminderType
```

Type of the reminder.

**Type:** ReminderType

**Since:** 7

**Deprecated since:** 9

**Substitutes:** reminderType

<!--Device-ReminderRequest-reminderType: ReminderType--><!--Device-ReminderRequest-reminderType: ReminderType-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## ringDuration

```TypeScript
ringDuration?: number
```

Ringing duration, in seconds. The default value is **1**. Unit: s.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ringDuration

<!--Device-ReminderRequest-ringDuration?: number--><!--Device-ReminderRequest-ringDuration?: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## slotType

```TypeScript
slotType?: notification.SlotType
```

Type of the slot used by the reminder.

**Type:** notification.SlotType

**Since:** 7

**Deprecated since:** 9

**Substitutes:** slotType

<!--Device-ReminderRequest-slotType?: notification.SlotType--><!--Device-ReminderRequest-slotType?: notification.SlotType-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## snoozeContent

```TypeScript
snoozeContent?: string
```

Content to be displayed when the reminder is snoozing.

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** snoozeContent

<!--Device-ReminderRequest-snoozeContent?: string--><!--Device-ReminderRequest-snoozeContent?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## snoozeTimes

```TypeScript
snoozeTimes?: number
```

Number of reminder snooze times. The default value is **0**.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** snoozeTimes

<!--Device-ReminderRequest-snoozeTimes?: number--><!--Device-ReminderRequest-snoozeTimes?: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## timeInterval

```TypeScript
timeInterval?: number
```

Reminder snooze interval, in seconds. The default value is **0**. Unit: s.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** timeInterval

<!--Device-ReminderRequest-timeInterval?: number--><!--Device-ReminderRequest-timeInterval?: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## title

```TypeScript
title?: string
```

Reminder title.

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** title

<!--Device-ReminderRequest-title?: string--><!--Device-ReminderRequest-title?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## wantAgent

```TypeScript
wantAgent?: WantAgent
```

Information about the ability that is redirected to when the notification is clicked.

**Type:** WantAgent

**Since:** 7

**Deprecated since:** 9

**Substitutes:** wantAgent

<!--Device-ReminderRequest-wantAgent?: WantAgent--><!--Device-ReminderRequest-wantAgent?: WantAgent-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

