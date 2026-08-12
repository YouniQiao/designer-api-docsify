# @ohos.notification

The **Notification** module provides notification management capabilities, covering notifications, notification slots, notification subscription, notification enabled status, and notification badge status.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [notificationManager](arkts-notificationmanager.md#notificationManager)

<!--Device-unnamed-declare namespace notification--><!--Device-unnamed-declare namespace notification-End-->

**System capability:** SystemCapability.Notification.Notification

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSlot](arkts-notification-notification-addslot-depr-f.md#addslot-2) |
| [addSlot](arkts-notification-notification-addslot-depr-f.md#addslot-3) |
| [cancel](arkts-notification-notification-cancel-depr-f.md#cancel) |
| [cancel](arkts-notification-notification-cancel-depr-f.md#cancel-1) |
| [cancel](arkts-notification-notification-cancel-depr-f.md#cancel-2) |
| [cancelAll](arkts-notification-notification-cancelall-depr-f.md#cancelall) |
| [cancelAll](arkts-notification-notification-cancelall-depr-f.md#cancelall-1) |
| [cancelGroup](arkts-notification-notification-cancelgroup-depr-f.md#cancelgroup) |
| [cancelGroup](arkts-notification-notification-cancelgroup-depr-f.md#cancelgroup-1) |
| [getActiveNotificationCount](arkts-notification-notification-getactivenotificationcount-depr-f.md#getactivenotificationcount) |
| [getActiveNotificationCount](arkts-notification-notification-getactivenotificationcount-depr-f.md#getactivenotificationcount-1) |
| [getActiveNotifications](arkts-notification-notification-getactivenotifications-depr-f.md#getactivenotifications) |
| [getActiveNotifications](arkts-notification-notification-getactivenotifications-depr-f.md#getactivenotifications-1) |
| [getSlot](arkts-notification-notification-getslot-depr-f.md#getslot) |
| [getSlot](arkts-notification-notification-getslot-depr-f.md#getslot-1) |
| [getSlots](arkts-notification-notification-getslots-depr-f.md#getslots) |
| [getSlots](arkts-notification-notification-getslots-depr-f.md#getslots-1) |
| [isDistributedEnabled](arkts-notification-notification-isdistributedenabled-depr-f.md#isdistributedenabled) |
| [isDistributedEnabled](arkts-notification-notification-isdistributedenabled-depr-f.md#isdistributedenabled-1) |
| [isSupportTemplate](arkts-notification-notification-issupporttemplate-depr-f.md#issupporttemplate) |
| [isSupportTemplate](arkts-notification-notification-issupporttemplate-depr-f.md#issupporttemplate-1) |
| [publish](arkts-notification-notification-publish-depr-f.md#publish) |
| [publish](arkts-notification-notification-publish-depr-f.md#publish-1) |
| [removeAllSlots](arkts-notification-notification-removeallslots-depr-f.md#removeallslots) |
| [removeAllSlots](arkts-notification-notification-removeallslots-depr-f.md#removeallslots-1) |
| [removeSlot](arkts-notification-notification-removeslot-depr-f.md#removeslot) |
| [removeSlot](arkts-notification-notification-removeslot-depr-f.md#removeslot-1) |
| [requestEnableNotification](arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification) |
| [requestEnableNotification](arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification-1) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSlot](arkts-notification-notification-addslot-depr-f-sys.md#addslot) |
| [addSlot](arkts-notification-notification-addslot-depr-f-sys.md#addslot-1) |
| [addSlots](arkts-notification-notification-addslots-depr-f-sys.md#addslots) |
| [addSlots](arkts-notification-notification-addslots-depr-f-sys.md#addslots-1) |
| [displayBadge](arkts-notification-notification-displaybadge-depr-f-sys.md#displaybadge) |
| [displayBadge](arkts-notification-notification-displaybadge-depr-f-sys.md#displaybadge-1) |
| [enableDistributed](arkts-notification-notification-enabledistributed-depr-f-sys.md#enabledistributed) |
| [enableDistributed](arkts-notification-notification-enabledistributed-depr-f-sys.md#enabledistributed-1) |
| [enableDistributedByBundle](arkts-notification-notification-enabledistributedbybundle-depr-f-sys.md#enabledistributedbybundle) |
| [enableDistributedByBundle](arkts-notification-notification-enabledistributedbybundle-depr-f-sys.md#enabledistributedbybundle-1) |
| [enableNotification](arkts-notification-notification-enablenotification-depr-f-sys.md#enablenotification) |
| [enableNotification](arkts-notification-notification-enablenotification-depr-f-sys.md#enablenotification-1) |
| [getAllActiveNotifications](arkts-notification-notification-getallactivenotifications-depr-f-sys.md#getallactivenotifications) |
| [getAllActiveNotifications](arkts-notification-notification-getallactivenotifications-depr-f-sys.md#getallactivenotifications-1) |
| [getDeviceRemindType](arkts-notification-notification-getdeviceremindtype-depr-f-sys.md#getdeviceremindtype) |
| [getDeviceRemindType](arkts-notification-notification-getdeviceremindtype-depr-f-sys.md#getdeviceremindtype-1) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getdonotdisturbdate) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getdonotdisturbdate-1) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getdonotdisturbdate-2) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getdonotdisturbdate-3) |
| [getSlotNumByBundle](arkts-notification-notification-getslotnumbybundle-depr-f-sys.md#getslotnumbybundle) |
| [getSlotNumByBundle](arkts-notification-notification-getslotnumbybundle-depr-f-sys.md#getslotnumbybundle-1) |
| [getSlotsByBundle](arkts-notification-notification-getslotsbybundle-depr-f-sys.md#getslotsbybundle) |
| [getSlotsByBundle](arkts-notification-notification-getslotsbybundle-depr-f-sys.md#getslotsbybundle-1) |
| [isBadgeDisplayed](arkts-notification-notification-isbadgedisplayed-depr-f-sys.md#isbadgedisplayed) |
| [isBadgeDisplayed](arkts-notification-notification-isbadgedisplayed-depr-f-sys.md#isbadgedisplayed-1) |
| [isDistributedEnabledByBundle](arkts-notification-notification-isdistributedenabledbybundle-depr-f-sys.md#isdistributedenabledbybundle) |
| [isDistributedEnabledByBundle](arkts-notification-notification-isdistributedenabledbybundle-depr-f-sys.md#isdistributedenabledbybundle-1) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled-1) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled-2) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled-3) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled-4) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled-5) |
| [publish](arkts-notification-notification-publish-depr-f-sys.md#publish-2) |
| [publish](arkts-notification-notification-publish-depr-f-sys.md#publish-3) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove-1) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove-2) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove-3) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall-1) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall-2) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall-3) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall-4) |
| [removeGroupByBundle](arkts-notification-notification-removegroupbybundle-depr-f-sys.md#removegroupbybundle) |
| [removeGroupByBundle](arkts-notification-notification-removegroupbybundle-depr-f-sys.md#removegroupbybundle-1) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setdonotdisturbdate) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setdonotdisturbdate-1) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setdonotdisturbdate-2) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setdonotdisturbdate-3) |
| [setSlotByBundle](arkts-notification-notification-setslotbybundle-depr-f-sys.md#setslotbybundle) |
| [setSlotByBundle](arkts-notification-notification-setslotbybundle-depr-f-sys.md#setslotbybundle-1) |
| [subscribe](arkts-notification-notification-subscribe-depr-f-sys.md#subscribe) |
| [subscribe](arkts-notification-notification-subscribe-depr-f-sys.md#subscribe-1) |
| [subscribe](arkts-notification-notification-subscribe-depr-f-sys.md#subscribe-2) |
| [supportDoNotDisturbMode](arkts-notification-notification-supportdonotdisturbmode-depr-f-sys.md#supportdonotdisturbmode) |
| [supportDoNotDisturbMode](arkts-notification-notification-supportdonotdisturbmode-depr-f-sys.md#supportdonotdisturbmode-1) |
| [unsubscribe](arkts-notification-notification-unsubscribe-depr-f-sys.md#unsubscribe) |
| [unsubscribe](arkts-notification-notification-unsubscribe-depr-f-sys.md#unsubscribe-1) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BundleOption](arkts-notification-notification-bundleoption-depr-i.md) |
| [NotificationKey](arkts-notification-notification-notificationkey-depr-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DoNotDisturbDate](arkts-notification-notification-donotdisturbdate-depr-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ContentType](arkts-notification-notification-contenttype-depr-e.md) |
| [SlotLevel](arkts-notification-notification-slotlevel-depr-e.md) |
| [SlotType](arkts-notification-notification-slottype-depr-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeviceRemindType](arkts-notification-notification-deviceremindtype-depr-e-sys.md) |
| [DoNotDisturbType](arkts-notification-notification-donotdisturbtype-depr-e-sys.md) |
| [RemoveReason](arkts-notification-notification-removereason-depr-e-sys.md) |
| [SourceType](arkts-notification-notification-sourcetype-depr-e-sys.md) |
<!--DelEnd-->
