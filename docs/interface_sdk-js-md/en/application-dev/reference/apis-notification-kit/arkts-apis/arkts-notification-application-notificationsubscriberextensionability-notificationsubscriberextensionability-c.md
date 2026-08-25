# NotificationSubscriberExtensionAbility

NotificationSubscriberExtensionAbility is the base class for notification subscriber extension abilities, providing notification subscription-related functionality. Third-party wearable apps (such as companion applications for watches)implement callback logic by inheriting this class, receiving notification information when notifications are published on the local device and forwarding them to the wearable device via Bluetooth, and receiving callbacks for notification cancellation when local notifications are cancelled and forwarding them to the wearable device to delete the corresponding notifications.Use this module when your wearable application needs to obtain local notifications and sync them to a paired wearable device. This module is used together with the notificationExtensionSubscription module. This module is responsible for receiving and processing notification data in callbacks, while the notificationExtensionSubscription module is responsible for management operations such as authorization, subscription, and unsubscription.

**Since:** 22

**System capability:** SystemCapability.Notification.Notification

## Modules to Import

```TypeScript
import { NotificationSubscriberExtensionAbility } from 'kits/@kit.NotificationKit';
```

## onCancelMessages

```TypeScript
onCancelMessages(hashCodes: Array<string>): void
```

Called when notifications are canceled.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hashCodes | Array & lt;string & gt; | Yes |

## onDestroy

```TypeScript
onDestroy(): void
```

Called when the notification subscription extension is destroyed.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Notification.Notification

## onReceiveMessage

```TypeScript
onReceiveMessage(notificationInfo: NotificationInfo): void
```

Called when a notification is received.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| notificationInfo | [NotificationInfo](arkts-notification-notificationinfo-i.md) | Yes |

## context

```TypeScript
context: NotificationSubscriberExtensionContext
```

Context for the NotificationSubscriberExtensionAbility.

**Type:** [NotificationSubscriberExtensionContext](arkts-notification-application-notificationsubscriberextensioncontext-notificationsubscriberextensioncontext-c.md)

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Notification.Notification
