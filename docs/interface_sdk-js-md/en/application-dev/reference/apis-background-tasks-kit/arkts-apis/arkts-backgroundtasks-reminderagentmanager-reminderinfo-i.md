# ReminderInfo

代理提醒信息，包含 ReminderRequest 和 ReminderId。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-reminderAgentManager-interface ReminderInfo--><!--Device-reminderAgentManager-interface ReminderInfo-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## reminderId

```TypeScript
reminderId: int
```

发布提醒后返回的id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ReminderInfo-reminderId: int--><!--Device-ReminderInfo-reminderId: int-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## reminderReq

```TypeScript
reminderReq: ReminderRequest
```

代理提醒对象。

**Type:** [ReminderRequest](arkts-backgroundtasks-reminderagentmanager-reminderrequest-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ReminderInfo-reminderReq: ReminderRequest--><!--Device-ReminderInfo-reminderReq: ReminderRequest-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

