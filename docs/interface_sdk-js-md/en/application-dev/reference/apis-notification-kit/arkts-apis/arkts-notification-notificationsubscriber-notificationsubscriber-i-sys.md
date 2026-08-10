# NotificationSubscriber (System API)

提供订阅者接收到新通知、取消通知等的回调方法。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationSubscriber--><!--Device-unnamed-export interface NotificationSubscriber-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onBadgeChanged

```TypeScript
onBadgeChanged?:(data: BadgeNumberCallbackData) => void
```

回调返回监听到的应用角标数量变化。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onBadgeChanged?:(data: BadgeNumberCallbackData) => void--><!--Device-NotificationSubscriber-onBadgeChanged?:(data: BadgeNumberCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [BadgeNumberCallbackData](arkts-notification-notificationsubscribe-badgenumbercallbackdata-t-sys.md) | Yes |  |

## onBatchCancel

```TypeScript
onBatchCancel?: (data: Array<SubscribeCallbackData>) => void
```

批量删除的通知信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onBatchCancel?: (data: Array<SubscribeCallbackData>) => void--><!--Device-NotificationSubscriber-onBatchCancel?: (data: Array<SubscribeCallbackData>) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Array&lt;SubscribeCallbackData&gt; | Yes |  |

## onCancel

```TypeScript
onCancel?:(data: SubscribeCallbackData) => void
```

需要取消的通知信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onCancel?:(data: SubscribeCallbackData) => void--><!--Device-NotificationSubscriber-onCancel?:(data: SubscribeCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [SubscribeCallbackData](arkts-notification-notificationsubscribe-subscribecallbackdata-t-sys.md) | Yes |  |

## onConnect

```TypeScript
onConnect?:() => void
```

订阅完成的回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onConnect?:() => void--><!--Device-NotificationSubscriber-onConnect?:() => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onConsume

```TypeScript
onConsume?:(data: SubscribeCallbackData) => void
```

新接收到的通知信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onConsume?:(data: SubscribeCallbackData) => void--><!--Device-NotificationSubscriber-onConsume?:(data: SubscribeCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [SubscribeCallbackData](arkts-notification-notificationsubscribe-subscribecallbackdata-t-sys.md) | Yes |  |

## onDestroy

```TypeScript
onDestroy?:() => void
```

服务失联的回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onDestroy?:() => void--><!--Device-NotificationSubscriber-onDestroy?:() => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onDisconnect

```TypeScript
onDisconnect?:() => void
```

取消订阅的回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onDisconnect?:() => void--><!--Device-NotificationSubscriber-onDisconnect?:() => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onDoNotDisturbChanged

```TypeScript
onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void
```

回调返回免打扰时间选项变更。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void--><!--Device-NotificationSubscriber-onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | notificationManager.DoNotDisturbDate | Yes |  |

## onDoNotDisturbDateChange

```TypeScript
onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void
```

回调返回免打扰时间选项变更。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 11

**Substitutes:** [NotificationSubscriber#onDoNotDisturbChanged](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md#ondonotdisturbchanged)

<!--Device-NotificationSubscriber-onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void--><!--Device-NotificationSubscriber-onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | notification.DoNotDisturbDate | Yes |  |

## onEnabledNotificationChanged

```TypeScript
onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void
```

回调返回监听到的应用信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void--><!--Device-NotificationSubscriber-onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackData | [EnabledNotificationCallbackData](arkts-notification-notificationsubscribe-enablednotificationcallbackdata-t-sys.md) | Yes |  |

## onEnabledPriorityByBundleChanged

```TypeScript
onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void
```

返回应用通知优先级开关状态。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-NotificationSubscriber-onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void--><!--Device-NotificationSubscriber-onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackData | [EnabledPriorityNotificationByBundleCallbackData](arkts-notification-notificationsubscriber-enabledprioritynotificationbybundlecallbackdata-i-sys.md) | Yes |  |

## onEnabledPriorityChanged

```TypeScript
onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void
```

返回通知优先级总开关状态。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-NotificationSubscriber-onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void--><!--Device-NotificationSubscriber-onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackData | [EnabledPriorityNotificationCallbackData](arkts-notification-notificationsubscribe-enabledprioritynotificationcallbackdata-t-sys.md) | Yes |  |

## onEnabledSilentReminderChanged

```TypeScript
onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback
```

返回应用通知静默提醒的使能状态变化。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscriber-onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback--><!--Device-NotificationSubscriber-onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onNotificationSwitchChanged

```TypeScript
onNotificationSwitchChanged?: NotificationSwitchChangedCallback
```

返回由[notificationManager.setNotificationSwitch](arkts-notification-notificationmanager-setnotificationswitch-f-sys.md#setnotificationswitch)接口设置的通知开关状态变化。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscriber-onNotificationSwitchChanged?: NotificationSwitchChangedCallback--><!--Device-NotificationSubscriber-onNotificationSwitchChanged?: NotificationSwitchChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onSystemUpdate

```TypeScript
onSystemUpdate?: SystemUpdateCallback
```

返回携带系统属性值的通知信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscriber-onSystemUpdate?: SystemUpdateCallback--><!--Device-NotificationSubscriber-onSystemUpdate?: SystemUpdateCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onUpdate

```TypeScript
onUpdate?:(data: NotificationSortingMap) => void
```

最新的通知排序列表。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onUpdate?:(data: NotificationSortingMap) => void--><!--Device-NotificationSubscriber-onUpdate?:(data: NotificationSortingMap) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [NotificationSortingMap](arkts-notification-notificationsortingmap-notificationsortingmap-i-sys.md) | Yes |  |

## onBadgeEnabledChanged

```TypeScript
onBadgeEnabledChanged?: BadgeEnabledChangedCallback
```

返回应用角标的使能状态变化。

**Type:** [BadgeEnabledChangedCallback](arkts-notification-notificationsubscriber-badgeenabledchangedcallback-i-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NotificationSubscriber-onBadgeEnabledChanged?: BadgeEnabledChangedCallback--><!--Device-NotificationSubscriber-onBadgeEnabledChanged?: BadgeEnabledChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

