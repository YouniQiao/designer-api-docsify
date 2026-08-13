# @ohos.notification

The **Notification** module provides notification management capabilities, covering notifications, notification slots , notification subscription, notification enabled status, and notification badge status.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [notificationManager](arkts-notificationmanager.md#@ohos.notificationManager)

<!--Device-unnamed-declare namespace notification--><!--Device-unnamed-declare namespace notification-End-->

**System capability:** SystemCapability.Notification.Notification

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSlot](arkts-notification-notification-addslot-depr-f.md#addSlot) |
| [addSlot](arkts-notification-notification-addslot-depr-f.md#addSlot) |
| [cancel](arkts-notification-notification-cancel-depr-f.md#cancel) |
| [cancel](arkts-notification-notification-cancel-depr-f.md#cancel) |
| [cancel](arkts-notification-notification-cancel-depr-f.md#cancel) |
| [cancelAll](arkts-notification-notification-cancelall-depr-f.md#cancelAll) |
| [cancelAll](arkts-notification-notification-cancelall-depr-f.md#cancelAll) |
| [cancelGroup](arkts-notification-notification-cancelgroup-depr-f.md#cancelGroup) |
| [cancelGroup](arkts-notification-notification-cancelgroup-depr-f.md#cancelGroup) |
| [getActiveNotificationCount](arkts-notification-notification-getactivenotificationcount-depr-f.md#getActiveNotificationCount) |
| [getActiveNotificationCount](arkts-notification-notification-getactivenotificationcount-depr-f.md#getActiveNotificationCount) |
| [getActiveNotifications](arkts-notification-notification-getactivenotifications-depr-f.md#getActiveNotifications) |
| [getActiveNotifications](arkts-notification-notification-getactivenotifications-depr-f.md#getActiveNotifications) |
| [getSlot](arkts-notification-notification-getslot-depr-f.md#getSlot) |
| [getSlot](arkts-notification-notification-getslot-depr-f.md#getSlot) |
| [getSlots](arkts-notification-notification-getslots-depr-f.md#getSlots) |
| [getSlots](arkts-notification-notification-getslots-depr-f.md#getSlots) |
| [isDistributedEnabled](arkts-notification-notification-isdistributedenabled-depr-f.md#isDistributedEnabled) |
| [isDistributedEnabled](arkts-notification-notification-isdistributedenabled-depr-f.md#isDistributedEnabled) |
| [isSupportTemplate](arkts-notification-notification-issupporttemplate-depr-f.md#isSupportTemplate) |
| [isSupportTemplate](arkts-notification-notification-issupporttemplate-depr-f.md#isSupportTemplate) |
| [publish](arkts-notification-notification-publish-depr-f.md#publish) |
| [publish](arkts-notification-notification-publish-depr-f.md#publish) |
| [removeAllSlots](arkts-notification-notification-removeallslots-depr-f.md#removeAllSlots) |
| [removeAllSlots](arkts-notification-notification-removeallslots-depr-f.md#removeAllSlots) |
| [removeSlot](arkts-notification-notification-removeslot-depr-f.md#removeSlot) |
| [removeSlot](arkts-notification-notification-removeslot-depr-f.md#removeSlot) |
| [requestEnableNotification](arkts-notification-notification-requestenablenotification-depr-f.md#requestEnableNotification) |
| [requestEnableNotification](arkts-notification-notification-requestenablenotification-depr-f.md#requestEnableNotification) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSlot](arkts-notification-notification-addslot-depr-f-sys.md#addSlot) |
| [addSlot](arkts-notification-notification-addslot-depr-f-sys.md#addSlot) |
| [addSlots](arkts-notification-notification-addslots-depr-f-sys.md#addSlots) |
| [addSlots](arkts-notification-notification-addslots-depr-f-sys.md#addSlots) |
| [displayBadge](arkts-notification-notification-displaybadge-depr-f-sys.md#displayBadge) |
| [displayBadge](arkts-notification-notification-displaybadge-depr-f-sys.md#displayBadge) |
| [enableDistributed](arkts-notification-notification-enabledistributed-depr-f-sys.md#enableDistributed) |
| [enableDistributed](arkts-notification-notification-enabledistributed-depr-f-sys.md#enableDistributed) |
| [enableDistributedByBundle](arkts-notification-notification-enabledistributedbybundle-depr-f-sys.md#enableDistributedByBundle) |
| [enableDistributedByBundle](arkts-notification-notification-enabledistributedbybundle-depr-f-sys.md#enableDistributedByBundle) |
| [enableNotification](arkts-notification-notification-enablenotification-depr-f-sys.md#enableNotification) |
| [enableNotification](arkts-notification-notification-enablenotification-depr-f-sys.md#enableNotification) |
| [getAllActiveNotifications](arkts-notification-notification-getallactivenotifications-depr-f-sys.md#getAllActiveNotifications) |
| [getAllActiveNotifications](arkts-notification-notification-getallactivenotifications-depr-f-sys.md#getAllActiveNotifications) |
| [getDeviceRemindType](arkts-notification-notification-getdeviceremindtype-depr-f-sys.md#getDeviceRemindType) |
| [getDeviceRemindType](arkts-notification-notification-getdeviceremindtype-depr-f-sys.md#getDeviceRemindType) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getDoNotDisturbDate) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getDoNotDisturbDate) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getDoNotDisturbDate) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getDoNotDisturbDate) |
| [getSlotNumByBundle](arkts-notification-notification-getslotnumbybundle-depr-f-sys.md#getSlotNumByBundle) |
| [getSlotNumByBundle](arkts-notification-notification-getslotnumbybundle-depr-f-sys.md#getSlotNumByBundle) |
| [getSlotsByBundle](arkts-notification-notification-getslotsbybundle-depr-f-sys.md#getSlotsByBundle) |
| [getSlotsByBundle](arkts-notification-notification-getslotsbybundle-depr-f-sys.md#getSlotsByBundle) |
| [isBadgeDisplayed](arkts-notification-notification-isbadgedisplayed-depr-f-sys.md#isBadgeDisplayed) |
| [isBadgeDisplayed](arkts-notification-notification-isbadgedisplayed-depr-f-sys.md#isBadgeDisplayed) |
| [isDistributedEnabledByBundle](arkts-notification-notification-isdistributedenabledbybundle-depr-f-sys.md#isDistributedEnabledByBundle) |
| [isDistributedEnabledByBundle](arkts-notification-notification-isdistributedenabledbybundle-depr-f-sys.md#isDistributedEnabledByBundle) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isNotificationEnabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isNotificationEnabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isNotificationEnabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isNotificationEnabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isNotificationEnabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isNotificationEnabled) |
| [publish](arkts-notification-notification-publish-depr-f-sys.md#publish) |
| [publish](arkts-notification-notification-publish-depr-f-sys.md#publish) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeAll) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeAll) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeAll) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeAll) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeAll) |
| [removeGroupByBundle](arkts-notification-notification-removegroupbybundle-depr-f-sys.md#removeGroupByBundle) |
| [removeGroupByBundle](arkts-notification-notification-removegroupbybundle-depr-f-sys.md#removeGroupByBundle) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setDoNotDisturbDate) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setDoNotDisturbDate) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setDoNotDisturbDate) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setDoNotDisturbDate) |
| [setSlotByBundle](arkts-notification-notification-setslotbybundle-depr-f-sys.md#setSlotByBundle) |
| [setSlotByBundle](arkts-notification-notification-setslotbybundle-depr-f-sys.md#setSlotByBundle) |
| [subscribe](arkts-notification-notification-subscribe-depr-f-sys.md#subscribe) |
| [subscribe](arkts-notification-notification-subscribe-depr-f-sys.md#subscribe) |
| [subscribe](arkts-notification-notification-subscribe-depr-f-sys.md#subscribe) |
| [supportDoNotDisturbMode](arkts-notification-notification-supportdonotdisturbmode-depr-f-sys.md#supportDoNotDisturbMode) |
| [supportDoNotDisturbMode](arkts-notification-notification-supportdonotdisturbmode-depr-f-sys.md#supportDoNotDisturbMode) |
| [unsubscribe](arkts-notification-notification-unsubscribe-depr-f-sys.md#unsubscribe) |
| [unsubscribe](arkts-notification-notification-unsubscribe-depr-f-sys.md#unsubscribe) |
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
