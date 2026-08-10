# MaxScreenWantAgent

通知中心弹出提醒时，全屏显示自动拉起目标的ability信息。该接口为预留接口，暂不支持使用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface MaxScreenWantAgent--><!--Device-reminderAgentManager-interface MaxScreenWantAgent-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## abilityName

```TypeScript
abilityName: string
```

指明提醒到达时自动拉起的目标ability名（如果设备在使用中，则只弹出通知横幅框）。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MaxScreenWantAgent-abilityName: string--><!--Device-MaxScreenWantAgent-abilityName: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## pkgName

```TypeScript
pkgName: string
```

指明提醒到达时自动拉起的目标包名（如果设备在使用中，则只弹出通知横幅框）。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-MaxScreenWantAgent-pkgName: string--><!--Device-MaxScreenWantAgent-pkgName: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

