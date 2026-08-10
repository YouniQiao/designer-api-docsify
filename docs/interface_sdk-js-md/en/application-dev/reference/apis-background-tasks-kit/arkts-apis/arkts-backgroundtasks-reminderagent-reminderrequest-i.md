# ReminderRequest

提醒实例对象，用于设置提醒类型、响铃时长等具体信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [@ohos.reminderAgentManager:reminderAgentManager.ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md)

<!--Device-reminderAgent-interface ReminderRequest--><!--Device-reminderAgent-interface ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgent } from 'kits/@kit.BackgroundTasksKit';
```

## actionButton

```TypeScript
actionButton?: [ActionButton?, ActionButton?]
```

弹出的提醒通知栏中显示的按钮（参数可选，支持0/1/2个按钮）。

**Type:** [ActionButton?, ActionButton?]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.actionButton](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#actionbutton)

<!--Device-ReminderRequest-actionButton?: [ActionButton?, ActionButton?]--><!--Device-ReminderRequest-actionButton?: [ActionButton?, ActionButton?]-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## content

```TypeScript
content?: string
```

指明提醒内容。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.content](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#content)

<!--Device-ReminderRequest-content?: string--><!--Device-ReminderRequest-content?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## expiredContent

```TypeScript
expiredContent?: string
```

指明提醒过期后需要显示的内容。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.expiredContent](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#expiredcontent)

<!--Device-ReminderRequest-expiredContent?: string--><!--Device-ReminderRequest-expiredContent?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## maxScreenWantAgent

```TypeScript
maxScreenWantAgent?: MaxScreenWantAgent
```

提醒到达时跳转的目标包。如果设备正在使用中，则弹出一个通知框。

**Type:** [MaxScreenWantAgent](arkts-backgroundtasks-reminderagentmanager-maxscreenwantagent-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.maxScreenWantAgent](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#maxscreenwantagent)

<!--Device-ReminderRequest-maxScreenWantAgent?: MaxScreenWantAgent--><!--Device-ReminderRequest-maxScreenWantAgent?: MaxScreenWantAgent-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## notificationId

```TypeScript
notificationId?: number
```

指明提醒使用的通知的id号，相同id号的提醒会覆盖。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.notificationId](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#notificationid)

<!--Device-ReminderRequest-notificationId?: number--><!--Device-ReminderRequest-notificationId?: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## reminderType

```TypeScript
reminderType: ReminderType
```

指明提醒类型。

**Type:** [ReminderType](arkts-backgroundtasks-reminderagent-remindertype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.reminderType](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#remindertype)

<!--Device-ReminderRequest-reminderType: ReminderType--><!--Device-ReminderRequest-reminderType: ReminderType-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## ringDuration

```TypeScript
ringDuration?: number
```

指明响铃时长（单位：秒），默认1秒。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.ringDuration](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#ringduration)

<!--Device-ReminderRequest-ringDuration?: number--><!--Device-ReminderRequest-ringDuration?: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## slotType

```TypeScript
slotType?: notification.SlotType
```

指明提醒的slot类型。

**Type:** notification.SlotType

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.slotType](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#slottype)

<!--Device-ReminderRequest-slotType?: notification.SlotType--><!--Device-ReminderRequest-slotType?: notification.SlotType-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## snoozeContent

```TypeScript
snoozeContent?: string
```

指明延迟提醒时需要显示的内容。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.snoozeContent](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#snoozecontent)

<!--Device-ReminderRequest-snoozeContent?: string--><!--Device-ReminderRequest-snoozeContent?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## snoozeTimes

```TypeScript
snoozeTimes?: number
```

指明延迟提醒次数，默认0次。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.snoozeTimes](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#snoozetimes)

<!--Device-ReminderRequest-snoozeTimes?: number--><!--Device-ReminderRequest-snoozeTimes?: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## timeInterval

```TypeScript
timeInterval?: number
```

执行延迟提醒间隔（单位：秒），默认0秒。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.timeInterval](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#timeinterval)

<!--Device-ReminderRequest-timeInterval?: number--><!--Device-ReminderRequest-timeInterval?: number-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## title

```TypeScript
title?: string
```

指明提醒标题。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.title](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#title)

<!--Device-ReminderRequest-title?: string--><!--Device-ReminderRequest-title?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## wantAgent

```TypeScript
wantAgent?: WantAgent
```

点击通知后需要跳转的目标ability信息。

**Type:** [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [reminderAgentManager.ReminderRequest.wantAgent](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md#wantagent)

<!--Device-ReminderRequest-wantAgent?: WantAgent--><!--Device-ReminderRequest-wantAgent?: WantAgent-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

