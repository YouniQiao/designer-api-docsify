# NotificationExtensionSubscriptionInfo

The **NotificationExtensionSubscriptionInfo** module describes the information about notification extension subscription.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationExtensionSubscriptionInfo--><!--Device-unnamed-export interface NotificationExtensionSubscriptionInfo-End-->

**System capability:** SystemCapability.Notification.Notification

## addr

```TypeScript
addr: string
```

Unique identifier of the device. When **type** is set to **SubscribeType.BLUETOOTH**, the corresponding Bluetooth device address is specified. Example: "11:22:33:AA:BB:FF".

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationExtensionSubscriptionInfo-addr: string--><!--Device-NotificationExtensionSubscriptionInfo-addr: string-End-->

**System capability:** SystemCapability.Notification.Notification

## type

```TypeScript
type: notificationExtensionSubscription.SubscribeType
```

Subscription type, specifying the subscription method for notification extension. Currently, only  
**SubscribeType.BLUETOOTH** is supported, indicating subscription to notifications via Bluetooth.

**Type:** notificationExtensionSubscription.SubscribeType

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationExtensionSubscriptionInfo-type: notificationExtensionSubscription.SubscribeType--><!--Device-NotificationExtensionSubscriptionInfo-type: notificationExtensionSubscription.SubscribeType-End-->

**System capability:** SystemCapability.Notification.Notification

