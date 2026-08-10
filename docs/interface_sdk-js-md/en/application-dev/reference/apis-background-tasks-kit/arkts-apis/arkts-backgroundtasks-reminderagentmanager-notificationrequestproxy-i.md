# NotificationRequestProxy

通知请求信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-reminderAgentManager-interface NotificationRequestProxy--><!--Device-reminderAgentManager-interface NotificationRequestProxy-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## Modules to Import

```TypeScript
import { reminderAgentManager } from 'kits/@kit.BackgroundTasksKit';
```

## appMessageId

```TypeScript
appMessageId?: string
```

应用发送通知携带的唯一标识字段，用于通知去重，默认为空。具体请参考  
[NotificationRequest.appMessageId](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationrequest-i.md/arkts-notification-notificationrequest-notificationrequest-i.md)。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationRequestProxy-appMessageId?: string--><!--Device-NotificationRequestProxy-appMessageId?: string-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

## isAlertOnce

```TypeScript
isAlertOnce?: boolean
```

发布或更新该通知时，是否只进行一次通知提醒，默认为false。具体请参考  
[NotificationRequest.isAlertOnce](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-notificationrequest-i.md/arkts-notification-notificationrequest-notificationrequest-i.md)。

- true：仅首次发布通知时进行提醒，后续更新该通知时，提醒方式变更为[LEVEL_LOW](../../apis-notification-kit/arkts-apis/arkts-notification-notificationmanager-slotlevel-e.md/arkts-notification-notificationmanager-slotlevel-e.md).  
- false：每次均按照配置的通知提醒方式进行提醒。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationRequestProxy-isAlertOnce?: boolean--><!--Device-NotificationRequestProxy-isAlertOnce?: boolean-End-->

**System capability:** SystemCapability.Notification.ReminderAgent

