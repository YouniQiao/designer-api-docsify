# NotificationSubscriber (System API)

Provides callback methods for subscribers to receive and cancel notifications.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface NotificationSubscriber--><!--Device-unnamed-export interface NotificationSubscriber-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onBadgeChanged

```TypeScript
onBadgeChanged?:(data: BadgeNumberCallbackData) => void
```

Listens for changes of the application badge number.

**Type:** (data: BadgeNumberCallbackData) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onBadgeChanged?:(data: BadgeNumberCallbackData) => void--><!--Device-NotificationSubscriber-onBadgeChanged?:(data: BadgeNumberCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onBadgeEnabledChanged

```TypeScript
onBadgeEnabledChanged?: BadgeEnabledChangedCallback
```

Returns the changes of the enabling state of the application's badge.

**Type:** [BadgeEnabledChangedCallback](arkts-notification-notificationsubscriber-badgeenabledchangedcallback-i-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onBadgeEnabledChanged?: BadgeEnabledChangedCallback--><!--Device-NotificationSubscriber-onBadgeEnabledChanged?: BadgeEnabledChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onBatchCancel

```TypeScript
onBatchCancel?: (data: Array<SubscribeCallbackData>) => void
```

Called for batch deletion.

**Type:** (data: Array&lt;[SubscribeCallbackData](arkts-notification-notificationsubscriber-subscribecallbackdata-i-sys.md)&gt;) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onBatchCancel?: (data: Array<SubscribeCallbackData>) => void--><!--Device-NotificationSubscriber-onBatchCancel?: (data: Array<SubscribeCallbackData>) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onCancel

```TypeScript
onCancel?:(data: SubscribeCallbackData) => void
```

Called when a notification is canceled.

**Type:** (data: SubscribeCallbackData) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onCancel?:(data: SubscribeCallbackData) => void--><!--Device-NotificationSubscriber-onCancel?:(data: SubscribeCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onConnect

```TypeScript
onConnect?:() => void
```

Called when subscription is complete.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onConnect?:() => void--><!--Device-NotificationSubscriber-onConnect?:() => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onConsume

```TypeScript
onConsume?:(data: SubscribeCallbackData) => void
```

Called when a new notification is received.

**Type:** (data: SubscribeCallbackData) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onConsume?:(data: SubscribeCallbackData) => void--><!--Device-NotificationSubscriber-onConsume?:(data: SubscribeCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onDestroy

```TypeScript
onDestroy?:() => void
```

Called when the service is disconnected.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onDestroy?:() => void--><!--Device-NotificationSubscriber-onDestroy?:() => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onDisconnect

```TypeScript
onDisconnect?:() => void
```

Called when unsubscription is complete.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onDisconnect?:() => void--><!--Device-NotificationSubscriber-onDisconnect?:() => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onDoNotDisturbChanged

```TypeScript
onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void
```

Called when the DND time settings are changed.

**Type:** (mode: notificationManager.DoNotDisturbDate) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void--><!--Device-NotificationSubscriber-onDoNotDisturbChanged?: (mode: notificationManager.DoNotDisturbDate) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onDoNotDisturbDateChange

```TypeScript
onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void
```

Called when the DND time settings are changed.

**Type:** (mode: notification.DoNotDisturbDate) =&gt; void

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 11

**Substitutes:** [onDoNotDisturbChanged](#onDoNotDisturbChanged)

<!--Device-NotificationSubscriber-onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void--><!--Device-NotificationSubscriber-onDoNotDisturbDateChange?: (mode: notification.DoNotDisturbDate) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onEnabledNotificationChanged

```TypeScript
onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void
```

Listens for the notification enabled state changes.

**Type:** (callbackData: EnabledNotificationCallbackData) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void--><!--Device-NotificationSubscriber-onEnabledNotificationChanged?:(callbackData: EnabledNotificationCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onEnabledPriorityByBundleChanged

```TypeScript
onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void
```

Called when the enabling state of the application priority notification changes.

**Type:** (callbackData: EnabledPriorityNotificationByBundleCallbackData) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void--><!--Device-NotificationSubscriber-onEnabledPriorityByBundleChanged?: (callbackData: EnabledPriorityNotificationByBundleCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onEnabledPriorityChanged

```TypeScript
onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void
```

Called when the enabling state of the priority notification changes.

**Type:** (callbackData: EnabledPriorityNotificationCallbackData) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void--><!--Device-NotificationSubscriber-onEnabledPriorityChanged?: (callbackData: EnabledPriorityNotificationCallbackData) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onEnabledSilentReminderChanged

```TypeScript
onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback
```

Returns the changes of the enabling state of the application's silent reminder.

**Type:** [EnabledSilentReminderChangedCallback](arkts-notification-enabledsilentreminderchangedcallback-t-sys.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscriber-onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback--><!--Device-NotificationSubscriber-onEnabledSilentReminderChanged?: EnabledSilentReminderChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onNotificationSwitchChanged

```TypeScript
onNotificationSwitchChanged?: NotificationSwitchChangedCallback
```

Returns the changes of the notification switch status set by [notificationManager.setNotificationSwitch](arkts-notification-notificationmanager-setnotificationswitch-f-sys.md#setNotificationSwitch-(System-API)).

**Type:** [NotificationSwitchChangedCallback](arkts-notification-notificationswitchchangedcallback-t-sys.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscriber-onNotificationSwitchChanged?: NotificationSwitchChangedCallback--><!--Device-NotificationSubscriber-onNotificationSwitchChanged?: NotificationSwitchChangedCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onSystemUpdate

```TypeScript
onSystemUpdate?: SystemUpdateCallback
```

Returns notification information containing the system property value.

**Type:** [SystemUpdateCallback](arkts-notification-systemupdatecallback-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationSubscriber-onSystemUpdate?: SystemUpdateCallback--><!--Device-NotificationSubscriber-onSystemUpdate?: SystemUpdateCallback-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## onUpdate

```TypeScript
onUpdate?:(data: NotificationSortingMap) => void
```

Called when notification sorting is updated. Not supported currently.

**Type:** (data: NotificationSortingMap) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationSubscriber-onUpdate?:(data: NotificationSortingMap) => void--><!--Device-NotificationSubscriber-onUpdate?:(data: NotificationSortingMap) => void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

