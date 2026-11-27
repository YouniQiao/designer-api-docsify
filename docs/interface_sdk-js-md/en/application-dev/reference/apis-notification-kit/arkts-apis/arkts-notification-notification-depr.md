# @ohos.notification(Notification)

The **Notification** module provides notification management capabilities, covering notifications, notification slots, notification subscription, notification enabled status, and notification badge status.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [notificationManager](arkts-notification-notificationmanager.md)

<!--Device-unnamed-declare namespace notification--><!--Device-unnamed-declare namespace notification-End-->

**System capability:** SystemCapability.Notification.Notification

## Modules to Import

```TypeScript
import { notification } from '@ohos.notification';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addSlot](arkts-notification-notification-depr-addslot-f.md#addslot-3) | Adds a notification slot of a specified type. This API uses an asynchronous callback to return the result. |
| [addSlot](arkts-notification-notification-depr-addslot-f.md#addslot-4) | Adds a notification slot of a specified type. This API uses a promise to return the result. |
| [cancel](arkts-notification-notification-depr-cancel-f.md#cancel-1) | Cancels a notification with the specified ID. This API uses an asynchronous callback to return the result. |
| [cancel](arkts-notification-notification-depr-cancel-f.md#cancel-2) | Cancels a notification with the specified ID and label. This API uses an asynchronous callback to return the result. |
| [cancel](arkts-notification-notification-depr-cancel-f.md#cancel-3) | Cancels a notification with the specified ID and optional label. This API uses a promise to return the result. |
| [cancelAll](arkts-notification-notification-depr-cancelall-f.md#cancelall-1) | Cancels all notifications. This API uses an asynchronous callback to return the result. |
| [cancelAll](arkts-notification-notification-depr-cancelall-f.md#cancelall-2) | Cancels all notifications. This API uses a promise to return the result. |
| [cancelGroup](arkts-notification-notification-depr-cancelgroup-f.md#cancelgroup-1) | Cancels notifications under a notification group of this application. This API uses an asynchronous callback to return the result. |
| [cancelGroup](arkts-notification-notification-depr-cancelgroup-f.md#cancelgroup-2) | Cancels notifications under a notification group of this application. This API uses a promise to return the result. |
| [getActiveNotificationCount](arkts-notification-notification-depr-getactivenotificationcount-f.md#getactivenotificationcount-1) | Obtains the number of active notifications of this application. This API uses an asynchronous callback to return the result. |
| [getActiveNotificationCount](arkts-notification-notification-depr-getactivenotificationcount-f.md#getactivenotificationcount-2) | Obtains the number of active notifications of this application. This API uses a promise to return the result. |
| [getActiveNotifications](arkts-notification-notification-depr-getactivenotifications-f.md#getactivenotifications-1) | Obtains active notifications of this application. This API uses an asynchronous callback to return the result. |
| [getActiveNotifications](arkts-notification-notification-depr-getactivenotifications-f.md#getactivenotifications-2) | Obtains active notifications of this application. This API uses a promise to return the result. |
| [getSlot](arkts-notification-notification-depr-getslot-f.md#getslot-1) | Obtains a notification slot of a specified type. This API uses an asynchronous callback to return the result. |
| [getSlot](arkts-notification-notification-depr-getslot-f.md#getslot-2) | Obtains a notification slot of a specified type. This API uses a promise to return the result. |
| [getSlots](arkts-notification-notification-depr-getslots-f.md#getslots-1) | Obtains all notification slots. This API uses an asynchronous callback to return the result. |
| [getSlots](arkts-notification-notification-depr-getslots-f.md#getslots-2) | Obtains all notification slots of this application. This API uses a promise to return the result. |
| [isDistributedEnabled](arkts-notification-notification-depr-isdistributedenabled-f.md#isdistributedenabled-1) | Checks whether the device supports [distributed notification](../../../notification/notification-glossary.md#distributed-notification). This API uses a callback to return the result. |
| [isDistributedEnabled](arkts-notification-notification-depr-isdistributedenabled-f.md#isdistributedenabled-2) | Checks whether the device supports [distributed notification](../../../notification/notification-glossary.md#distributed-notification). This API uses a promise to return the result. |
| [isSupportTemplate](arkts-notification-notification-depr-issupporttemplate-f.md#issupporttemplate-1) | Before publishing a notification using [NotificationTemplate](arkts-notification-notificationtemplate-i.md), you can call this API to check whether the corresponding notification template is supported. This API uses an asynchronous callback to return the result. |
| [isSupportTemplate](arkts-notification-notification-depr-issupporttemplate-f.md#issupporttemplate-2) | Checks whether a specified template is supported before using [NotificationTemplate](arkts-notification-notificationtemplate-i.md) to publish a notification. This API uses a promise to return the result. |
| [publish](arkts-notification-notification-depr-publish-f.md#publish-1) | Publishes a notification. This API uses an asynchronous callback to return the result. |
| [publish](arkts-notification-notification-depr-publish-f.md#publish-2) | Publishes a notification. This API uses a promise to return the result. |
| [removeAllSlots](arkts-notification-notification-depr-removeallslots-f.md#removeallslots-1) | Removes all notification slots. This API uses an asynchronous callback to return the result. |
| [removeAllSlots](arkts-notification-notification-depr-removeallslots-f.md#removeallslots-2) | Removes all notification slots. This API uses a promise to return the result. |
| [removeSlot](arkts-notification-notification-depr-removeslot-f.md#removeslot-1) | Removes a notification slot of a specified type. This API uses an asynchronous callback to return the result. |
| [removeSlot](arkts-notification-notification-depr-removeslot-f.md#removeslot-2) | Removes a notification slot of a specified type. This API uses a promise to return the result. |
| [requestEnableNotification](arkts-notification-notification-depr-requestenablenotification-f.md#requestenablenotification-1) | Requests notification to be enabled for this application. This API uses an asynchronous callback to return the result. |
| [requestEnableNotification](arkts-notification-notification-depr-requestenablenotification-f.md#requestenablenotification-2) | Requests notification to be enabled for this application. This API uses a promise to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [addSlot](arkts-notification-notification-depr-addslot-f-sys.md#addslot-1) | Adds a notification slot. This API uses an asynchronous callback to return the result. |
| [addSlot](arkts-notification-notification-depr-addslot-f-sys.md#addslot-2) | Adds a notification slot. This API uses a promise to return the result. |
| [addSlots](arkts-notification-notification-depr-addslots-f-sys.md#addslots-1) | Adds an array of notification slots. This API uses an asynchronous callback to return the result. |
| [addSlots](arkts-notification-notification-depr-addslots-f-sys.md#addslots-2) | Adds an array of notification slots. This API uses a promise to return the result. |
| [displayBadge](arkts-notification-notification-depr-displaybadge-f-sys.md#displaybadge-1) | Sets whether to enable the notification badge for a specified application. This API uses an asynchronous callback to return the result. |
| [displayBadge](arkts-notification-notification-depr-displaybadge-f-sys.md#displaybadge-2) | Sets whether to enable the notification badge for a specified application. This API uses a promise to return the result. |
| [enableDistributed](arkts-notification-notification-depr-enabledistributed-f-sys.md#enabledistributed-1) | Sets whether the device supports [distributed notifications](../../../notification/notification-glossary.md#distributed-notification). This API uses a callback to return the result. |
| [enableDistributed](arkts-notification-notification-depr-enabledistributed-f-sys.md#enabledistributed-2) | Sets whether the device supports [distributed notifications](../../../notification/notification-glossary.md#distributed-notification). This API uses a promise to return the result. |
| [enableDistributedByBundle](arkts-notification-notification-depr-enabledistributedbybundle-f-sys.md#enabledistributedbybundle-1) | Sets whether the specified application supports [distributed notifications](../../../notification/notification-glossary.md#distributed-notification). This API uses a callback to return the result. |
| [enableDistributedByBundle](arkts-notification-notification-depr-enabledistributedbybundle-f-sys.md#enabledistributedbybundle-2) | Sets whether the specified application supports [distributed notifications](../../../notification/notification-glossary.md#distributed-notification). This API uses a promise to return the result. |
| [enableNotification](arkts-notification-notification-depr-enablenotification-f-sys.md#enablenotification-1) | Sets whether to enable notification for a specified application. This API uses an asynchronous callback to return the result. |
| [enableNotification](arkts-notification-notification-depr-enablenotification-f-sys.md#enablenotification-2) | Sets whether to enable notification for a specified application. This API uses a promise to return the result. |
| [getAllActiveNotifications](arkts-notification-notification-depr-getallactivenotifications-f-sys.md#getallactivenotifications-1) | Obtains all active notifications. This API uses an asynchronous callback to return the result. |
| [getAllActiveNotifications](arkts-notification-notification-depr-getallactivenotifications-f-sys.md#getallactivenotifications-2) | Obtains all active notifications. This API uses a promise to return the result. |
| [getDeviceRemindType](arkts-notification-notification-depr-getdeviceremindtype-f-sys.md#getdeviceremindtype-1) | Obtains the notification reminder type. This API uses an asynchronous callback to return the result. |
| [getDeviceRemindType](arkts-notification-notification-depr-getdeviceremindtype-f-sys.md#getdeviceremindtype-2) | Obtains the notification reminder type. This API uses a promise to return the result. |
| [getDoNotDisturbDate](arkts-notification-notification-depr-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-1) | Obtains the DND time. This API uses an asynchronous callback to return the result. |
| [getDoNotDisturbDate](arkts-notification-notification-depr-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-2) | Obtains the DND time. This API uses a promise to return the result. |
| [getDoNotDisturbDate](arkts-notification-notification-depr-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-3) | Obtains the DND time of a specified user. This API uses an asynchronous callback to return the result. |
| [getDoNotDisturbDate](arkts-notification-notification-depr-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-4) | Obtains the DND time of a specified user. This API uses a promise to return the result. |
| [getSlotNumByBundle](arkts-notification-notification-depr-getslotnumbybundle-f-sys.md#getslotnumbybundle-1) | Obtains the number of notification slots of a specified application. This API uses an asynchronous callback to return the result. |
| [getSlotNumByBundle](arkts-notification-notification-depr-getslotnumbybundle-f-sys.md#getslotnumbybundle-2) | Obtains the number of notification slots of a specified application. This API uses a promise to return the result. |
| [getSlotsByBundle](arkts-notification-notification-depr-getslotsbybundle-f-sys.md#getslotsbybundle-1) | Obtains the notification slots of a specified application. This API uses an asynchronous callback to return the result. |
| [getSlotsByBundle](arkts-notification-notification-depr-getslotsbybundle-f-sys.md#getslotsbybundle-2) | Obtains the notification slots of a specified application. This API uses a promise to return the result. |
| [isBadgeDisplayed](arkts-notification-notification-depr-isbadgedisplayed-f-sys.md#isbadgedisplayed-1) | Checks whether the notification badge is enabled for a specified application. This API uses an asynchronous callback to return the result. |
| [isBadgeDisplayed](arkts-notification-notification-depr-isbadgedisplayed-f-sys.md#isbadgedisplayed-2) | Checks whether the notification badge is enabled for a specified application. This API uses a promise to return the result. |
| [isDistributedEnabledByBundle](arkts-notification-notification-depr-isdistributedenabledbybundle-f-sys.md#isdistributedenabledbybundle-1) | Obtains whether the application supports [distributed notifications](../../../notification/notification-glossary.md#distributed-notification) based on the application's bundle. This API uses a callback to return the result. |
| [isDistributedEnabledByBundle](arkts-notification-notification-depr-isdistributedenabledbybundle-f-sys.md#isdistributedenabledbybundle-2) | Queries whether the specified application supports [distributed notifications](../../../notification/notification-glossary.md#distributed-notification). This API uses a promise to return the result. |
| [isNotificationEnabled](arkts-notification-notification-depr-isnotificationenabled-f-sys.md#isnotificationenabled-1) | Checks whether notification is enabled for a specified application. This API uses an asynchronous callback to return the result. |
| [isNotificationEnabled](arkts-notification-notification-depr-isnotificationenabled-f-sys.md#isnotificationenabled-2) | Checks whether notification is enabled for a specified application. This API uses a promise to return the result. |
| [isNotificationEnabled](arkts-notification-notification-depr-isnotificationenabled-f-sys.md#isnotificationenabled-3) | Checks whether notification is enabled for this application. This API uses an asynchronous callback to return the result. |
| [isNotificationEnabled](arkts-notification-notification-depr-isnotificationenabled-f-sys.md#isnotificationenabled-4) | Checks whether notification is enabled for this application. This API uses a promise to return the result. |
| [isNotificationEnabled](arkts-notification-notification-depr-isnotificationenabled-f-sys.md#isnotificationenabled-5) | Checks whether notification is enabled for a specified user. This API uses an asynchronous callback to return the result. |
| [isNotificationEnabled](arkts-notification-notification-depr-isnotificationenabled-f-sys.md#isnotificationenabled-6) | Checks whether notification is enabled for a specified user. This API uses a promise to return the result. |
| [publish](arkts-notification-notification-depr-publish-f-sys.md#publish-3) | Publishes a notification to a specified user. This API uses an asynchronous callback to return the result. |
| [publish](arkts-notification-notification-depr-publish-f-sys.md#publish-4) | Publishes a notification to a specified user. This API uses a promise to return the result. |
| [remove](arkts-notification-notification-depr-remove-f-sys.md#remove-1) | Removes a notification for a specified bundle. This API uses an asynchronous callback to return the result. |
| [remove](arkts-notification-notification-depr-remove-f-sys.md#remove-2) | Removes a notification for a specified bundle. This API uses a promise to return the result. |
| [remove](arkts-notification-notification-depr-remove-f-sys.md#remove-3) | Removes a notification for a specified bundle. This API uses an asynchronous callback to return the result. |
| [remove](arkts-notification-notification-depr-remove-f-sys.md#remove-4) | Removes a notification for a specified bundle. This API uses a promise to return the result. |
| [removeAll](arkts-notification-notification-depr-removeall-f-sys.md#removeall-1) | Removes all notifications for a specified application. This API uses an asynchronous callback to return the result. |
| [removeAll](arkts-notification-notification-depr-removeall-f-sys.md#removeall-2) | Removes all notifications. This API uses an asynchronous callback to return the result. |
| [removeAll](arkts-notification-notification-depr-removeall-f-sys.md#removeall-3) | Removes all notifications for a specified user. This API uses an asynchronous callback to return the result. |
| [removeAll](arkts-notification-notification-depr-removeall-f-sys.md#removeall-4) | Removes all notifications for a specified user. This API uses a promise to return the result. |
| [removeAll](arkts-notification-notification-depr-removeall-f-sys.md#removeall-5) | Removes all notifications for a specified application. This API uses a promise to return the result. |
| [removeGroupByBundle](arkts-notification-notification-depr-removegroupbybundle-f-sys.md#removegroupbybundle-1) | Removes notifications under a notification group of a specified application. This API uses an asynchronous callback to return the result. |
| [removeGroupByBundle](arkts-notification-notification-depr-removegroupbybundle-f-sys.md#removegroupbybundle-2) | Removes notifications under a notification group of a specified application. This API uses a promise to return the result. |
| [setDoNotDisturbDate](arkts-notification-notification-depr-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-1) | Sets the DND time. This API uses an asynchronous callback to return the result. |
| [setDoNotDisturbDate](arkts-notification-notification-depr-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-2) | Sets the DND time. This API uses a promise to return the result. |
| [setDoNotDisturbDate](arkts-notification-notification-depr-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-3) | Sets the DND time for a specified user. This API uses an asynchronous callback to return the result. |
| [setDoNotDisturbDate](arkts-notification-notification-depr-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-4) | Sets the DND time for a specified user. This API uses a promise to return the result. |
| [setSlotByBundle](arkts-notification-notification-depr-setslotbybundle-f-sys.md#setslotbybundle-1) | Sets the notification slot for a specified application. This API uses an asynchronous callback to return the result. |
| [setSlotByBundle](arkts-notification-notification-depr-setslotbybundle-f-sys.md#setslotbybundle-2) | Sets the notification slot for a specified application. This API uses a promise to return the result. |
| [subscribe](arkts-notification-notification-depr-subscribe-f-sys.md#subscribe-1) | Subscribes to notifications of all applications under this user. This API uses an asynchronous callback to return the result. |
| [subscribe](arkts-notification-notification-depr-subscribe-f-sys.md#subscribe-2) | Subscribes to a notification with the subscription information specified. This API uses an asynchronous callback to return the result. |
| [subscribe](arkts-notification-notification-depr-subscribe-f-sys.md#subscribe-3) | Subscribes to a notification with the subscription information specified. This API uses a promise to return the result. |
| [supportDoNotDisturbMode](arkts-notification-notification-depr-supportdonotdisturbmode-f-sys.md#supportdonotdisturbmode-1) | Checks whether DND mode is supported. This API uses an asynchronous callback to return the result. |
| [supportDoNotDisturbMode](arkts-notification-notification-depr-supportdonotdisturbmode-f-sys.md#supportdonotdisturbmode-2) | Checks whether DND mode is supported. This API uses a promise to return the result. |
| [unsubscribe](arkts-notification-notification-depr-unsubscribe-f-sys.md#unsubscribe-1) | Unsubscribes from notifications. This API uses a callback to return the result. |
| [unsubscribe](arkts-notification-notification-depr-unsubscribe-f-sys.md#unsubscribe-2) | Unsubscribes from a notification. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BundleOption](arkts-notification-notification-depr-bundleoption-i.md) | Describes the **BundleOption** information |
| [NotificationKey](arkts-notification-notification-depr-notificationkey-i.md) | Notification key. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [DoNotDisturbDate](arkts-notification-notification-depr-donotdisturbdate-i-sys.md) | Defines the DND time. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ContentType](arkts-notification-notification-depr-contenttype-e.md) | Enumerates the notification content types. |
| [SlotLevel](arkts-notification-notification-depr-slotlevel-e.md) | Enumerates the notification level. |
| [SlotType](arkts-notification-notification-depr-slottype-e.md) | Enumerates the notification slot types. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [DeviceRemindType](arkts-notification-notification-depr-deviceremindtype-e-sys.md) | Defines the notification reminder type. |
| [DoNotDisturbType](arkts-notification-notification-depr-donotdisturbtype-e-sys.md) | Defines the DND time type. |
| [RemoveReason](arkts-notification-notification-depr-removereason-e-sys.md) | Reason for removing the notification. |
| [SourceType](arkts-notification-notification-depr-sourcetype-e-sys.md) | Defines the notification source type. |
<!--DelEnd-->
