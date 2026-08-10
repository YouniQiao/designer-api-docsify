# ActionButton

弹出的提醒中按钮的类型和标题。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface ActionButton--><!--Device-reminderAgentManager-interface ActionButton-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## dataShareUpdate

```TypeScript
dataShareUpdate?: DataShareUpdate
```

点击按钮将更新应用数据库。

**Type:** [DataShareUpdate](arkts-backgroundtasks-reminderagentmanager-datashareupdate-i-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ActionButton-dataShareUpdate?: DataShareUpdate--><!--Device-ActionButton-dataShareUpdate?: DataShareUpdate-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**System API:** This is a system API.

## wantAgent

```TypeScript
wantAgent?: WantAgent
```

点击按钮跳转的ability信息。

**Type:** [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ActionButton-wantAgent?: WantAgent--><!--Device-ActionButton-wantAgent?: WantAgent-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

**System API:** This is a system API.

