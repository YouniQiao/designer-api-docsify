# WantAgent

跳转目标的ability信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface WantAgent--><!--Device-reminderAgentManager-interface WantAgent-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## abilityName

```TypeScript
abilityName: string
```

指明跳转目标的ability名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WantAgent-abilityName: string--><!--Device-WantAgent-abilityName: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## parameters

```TypeScript
parameters?: Record<string, Object>
```

需要传递到目标的参数。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-WantAgent-parameters?: Record<string, Object>--><!--Device-WantAgent-parameters?: Record<string, Object>-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## pkgName

```TypeScript
pkgName: string
```

指明跳转目标的包名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WantAgent-pkgName: string--><!--Device-WantAgent-pkgName: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## uri

```TypeScript
uri?: string
```

指明跳转目标的uri信息。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-WantAgent-uri?: string--><!--Device-WantAgent-uri?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

