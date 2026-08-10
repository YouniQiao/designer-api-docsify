# NotificationExtensionSubscriptionInfo

用于描述通知扩展订阅的信息。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationExtensionSubscriptionInfo--><!--Device-unnamed-export interface NotificationExtensionSubscriptionInfo-End-->

**System capability:** SystemCapability.Notification.Notification

## addr

```TypeScript
addr: string
```

表示设备的唯一标识符。当type为`SubscribeType.BLUETOOTH`时，指定对应的蓝牙设备地址。例如："11:22:33:AA:BB:FF"。

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationExtensionSubscriptionInfo-addr: string--><!--Device-NotificationExtensionSubscriptionInfo-addr: string-End-->

**System capability:** SystemCapability.Notification.Notification

## type

```TypeScript
type: notificationExtensionSubscription.SubscribeType
```

订阅的类型，指定通知扩展的订阅方式。当前仅支持`SubscribeType.BLUETOOTH`，表示通过蓝牙订阅通知。

**Type:** notificationExtensionSubscription.SubscribeType

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-NotificationExtensionSubscriptionInfo-type: notificationExtensionSubscription.SubscribeType--><!--Device-NotificationExtensionSubscriptionInfo-type: notificationExtensionSubscription.SubscribeType-End-->

**System capability:** SystemCapability.Notification.Notification

