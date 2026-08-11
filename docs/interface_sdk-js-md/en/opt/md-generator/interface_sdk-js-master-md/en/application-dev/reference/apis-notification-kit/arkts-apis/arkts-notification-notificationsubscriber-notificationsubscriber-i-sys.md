# NotificationSubscriber (System API)

Provides callback methods for subscribers to receive and cancel notifications.

**Since:** 7

<!--Device-unnamed-export interface NotificationSubscriber--><!--Device-unnamed-export interface NotificationSubscriber-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onBadgeChanged

```TypeScript
onBadgeChanged?:(data: BadgeNumberCallbackData) => void
```

Listens for changes of the application badge number.

**Since:** 10

<!--Device-NotificationSubscriber-onBadgeChanged?:(data: BadgeNumberCallbackData) => void--><!--Device-NotificationSubscriber-onBadgeChanged?:(data: BadgeNumberCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [BadgeNumberCallbackData](arkts-notification-notificationsubscribe-badgenumbercallbackdata-t-sys.md) | Yes |

## onBatchCancel

```TypeScript
onBatchCancel?: (data: Array<SubscribeCallbackData>) => void
```

Called for batch deletion.

**Since:** 11

<!--Device-NotificationSubscriber-onBatchCancel?: (data: Array<SubscribeCallbackData>) => void--><!--Device-NotificationSubscriber-onBatchCancel?: (data: Array<SubscribeCallbackData>) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Array&lt;SubscribeCallbackData&gt; | Yes |

## onCancel

```TypeScript
onCancel?:(data: SubscribeCallbackData) => void
```

Called when a notification is canceled.

**Since:** 7

<!--Device-NotificationSubscriber-onCancel?:(data: SubscribeCallbackData) => void--><!--Device-NotificationSubscriber-onCancel?:(data: SubscribeCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [SubscribeCallbackData](arkts-notification-notificationsubscribe-subscribecallbackdata-t-sys.md) | Yes |

## onConnect

```TypeScript
onConnect?:() => void
```

Called when subscription is complete.

**Since:** 7

<!--Device-NotificationSubscriber-onConnect?:() => void--><!--Device-NotificationSubscriber-onConnect?:() => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onConsume

```TypeScript
onConsume?:(data: SubscribeCallbackData) => void
```

Called when a new notification is received.

**Since:** 7

<!--Device-NotificationSubscriber-onConsume?:(data: SubscribeCallbackData) => void--><!--Device-NotificationSubscriber-onConsume?:(data: SubscribeCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [SubscribeCallbackData](arkts-notification-notificationsubscribe-subscribecallbackdata-t-sys.md) | Yes |

## onDestroy

```TypeScript
onDestroy?:() => void
```

Called when the service is disconnected.

**Since:** 7

<!--Device-NotificationSubscriber-onDestroy?:() => void--><!--Device-NotificationSubscriber-onDestroy?:() => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onDisconnect

```TypeScript
onDisconnect?:() => void
```

Called when unsubscription is complete.

**Since:** 7

<!--Device-NotificationSubscriber-onDisconnect?:() => void--><!--Device-NotificationSubscriber-onDisconnect?:() => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onDoNotDisturbChanged

```TypeScript
onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void
```

Called when the DND time settings are changed.

**Since:** 11

<!--Device-NotificationSubscriber-onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void--><!--Device-NotificationSubscriber-onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | notificationManager.DoNotDisturbDate | Yes |

## onDoNotDisturbDateChange

```TypeScript
onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void
```

Called when the DND time settings are changed.

**Since:** 8

**Deprecated since:** 11

**Substitutes:** [NotificationSubscriber#onDoNotDisturbChanged](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md#ondonotdisturbchanged)

<!--Device-NotificationSubscriber-onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void--><!--Device-NotificationSubscriber-onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | notification.DoNotDisturbDate | Yes |

## onEnabledNotificationChanged

```TypeScript
onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void
```

Listens for the notification enabled state changes.

**Since:** 8

<!--Device-NotificationSubscriber-onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void--><!--Device-NotificationSubscriber-onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackData | [EnabledNotificationCallbackData](arkts-notification-notificationsubscriber-enablednotificationcallbackdata-i-sys.md) | Yes |

## onEnabledPriorityByBundleChanged

```TypeScript
onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void
```

Called when the enabling state of the application priority notification changes.

**Since:** 23

<!--Device-NotificationSubscriber-onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void--><!--Device-NotificationSubscriber-onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackData | [EnabledPriorityNotificationByBundleCallbackData](arkts-notification-notificationsubscriber-enabledprioritynotificationbybundlecallbackdata-i-sys.md) | Yes |

## onEnabledPriorityChanged

```TypeScript
onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void
```

Called when the enabling state of the priority notification changes.

**Since:** 23

<!--Device-NotificationSubscriber-onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void--><!--Device-NotificationSubscriber-onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackData | [EnabledPriorityNotificationCallbackData](arkts-notification-notificationsubscribe-enabledprioritynotificationcallbackdata-t-sys.md) | Yes |

## onEnabledSilentReminderChanged

```TypeScript
onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback
```

Returns the changes of the enabling state of the application's silent reminder.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscriber-onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback--><!--Device-NotificationSubscriber-onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onNotificationSwitchChanged

```TypeScript
onNotificationSwitchChanged?: NotificationSwitchChangedCallback
```

Returns the changes of the notification switch status set by  
[notificationManager.setNotificationSwitch](arkts-notification-notificationmanager-setnotificationswitch-f-sys.md#setnotificationswitch).

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscriber-onNotificationSwitchChanged?: NotificationSwitchChangedCallback--><!--Device-NotificationSubscriber-onNotificationSwitchChanged?: NotificationSwitchChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onSystemUpdate

```TypeScript
onSystemUpdate?: SystemUpdateCallback
```

Returns notification information containing the system property value.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscriber-onSystemUpdate?: SystemUpdateCallback--><!--Device-NotificationSubscriber-onSystemUpdate?: SystemUpdateCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onUpdate

```TypeScript
onUpdate?:(data: NotificationSortingMap) => void
```

Called when notification sorting is updated. Not supported currently.

**Since:** 7

<!--Device-NotificationSubscriber-onUpdate?:(data: NotificationSortingMap) => void--><!--Device-NotificationSubscriber-onUpdate?:(data: NotificationSortingMap) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [NotificationSortingMap](arkts-notification-notificationsortingmap-notificationsortingmap-i-sys.md) | Yes |

## onBadgeEnabledChanged

```TypeScript
onBadgeEnabledChanged?: BadgeEnabledChangedCallback
```

Returns the changes of the enabling state of the application's badge.

**Type:** [BadgeEnabledChangedCallback](arkts-notification-notificationsubscriber-badgeenabledchangedcallback-i-sys.md)

**Since:** 12

<!--Device-NotificationSubscriber-onBadgeEnabledChanged?: BadgeEnabledChangedCallback--><!--Device-NotificationSubscriber-onBadgeEnabledChanged?: BadgeEnabledChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.
