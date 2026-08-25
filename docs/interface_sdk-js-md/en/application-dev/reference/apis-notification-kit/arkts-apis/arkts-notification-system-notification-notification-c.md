# Notification

Manages notifications.

**Since:** 3

**ArkTS mode:** Supports only ArkTS-Dyn, since version 3.

**Deprecated since:** 7

**Substitutes:** [notification/notification](arkts-notification.md)

**System capability:** SystemCapability.Notification.Notification

## Modules to Import

```TypeScript
import { Notification, ActionResult, ShowNotificationOptions } from '@kit.NotificationKit';
```

## show

```TypeScript
static show(options?: ShowNotificationOptions): void
```

Displays the notification.

**Since:** 3

**ArkTS mode:** Supports only ArkTS-Dyn, since version 3.

**Deprecated since:** 7

**Substitutes:** [notification/notification](arkts-notification.md)

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ShowNotificationOptions](arkts-notification-system-notification-shownotificationoptions-i.md) | No |

**Examples**

```TypeScript
let notificationObj: notification = {
  show() {
    notification.show({
      contentTitle: 'title info',
      contentText: 'text',
      clickAction: {
        bundleName: 'com.example.testapp',
        abilityName: 'notificationDemo',
        uri: '/path/to/notification'
      }
    });
  }
}
```
