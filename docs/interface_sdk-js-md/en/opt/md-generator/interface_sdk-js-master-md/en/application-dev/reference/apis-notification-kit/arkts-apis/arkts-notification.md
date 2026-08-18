# @ohos.notification

The **Notification** module provides notification management capabilities, covering notifications, notification slots , notification subscription, notification enabled status, and notification badge status.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [notificationManager](arkts-notificationmanager.md#ohosnotificationmanager)

<!--Device-unnamed-declare namespace notification--><!--Device-unnamed-declare namespace notification-End-->

**System capability:** SystemCapability.Notification.Notification

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSlot](arkts-notification-notification-addslot-depr-f.md#addslot) |
| [addSlot](arkts-notification-notification-addslot-depr-f.md#addslot) |
| [cancel](arkts-notification-notification-cancel-depr-f.md#cancel) |
| [cancel](arkts-notification-notification-cancel-depr-f.md#cancel) |
| [cancel](arkts-notification-notification-cancel-depr-f.md#cancel) |
| [cancelAll](arkts-notification-notification-cancelall-depr-f.md#cancelall) |
| [cancelAll](arkts-notification-notification-cancelall-depr-f.md#cancelall) |
| [cancelGroup](arkts-notification-notification-cancelgroup-depr-f.md#cancelgroup) |
| [cancelGroup](arkts-notification-notification-cancelgroup-depr-f.md#cancelgroup) |
| [getActiveNotificationCount](arkts-notification-notification-getactivenotificationcount-depr-f.md#getactivenotificationcount) |
| [getActiveNotificationCount](arkts-notification-notification-getactivenotificationcount-depr-f.md#getactivenotificationcount) |
| [getActiveNotifications](arkts-notification-notification-getactivenotifications-depr-f.md#getactivenotifications) |
| [getActiveNotifications](arkts-notification-notification-getactivenotifications-depr-f.md#getactivenotifications) |
| [getSlot](arkts-notification-notification-getslot-depr-f.md#getslot) |
| [getSlot](arkts-notification-notification-getslot-depr-f.md#getslot) |
| [getSlots](arkts-notification-notification-getslots-depr-f.md#getslots) |
| [getSlots](arkts-notification-notification-getslots-depr-f.md#getslots) |
| [isDistributedEnabled](arkts-notification-notification-isdistributedenabled-depr-f.md#isdistributedenabled) |
| [isDistributedEnabled](arkts-notification-notification-isdistributedenabled-depr-f.md#isdistributedenabled) |
| [isSupportTemplate](arkts-notification-notification-issupporttemplate-depr-f.md#issupporttemplate) |
| [isSupportTemplate](arkts-notification-notification-issupporttemplate-depr-f.md#issupporttemplate) |
| [publish](arkts-notification-notification-publish-depr-f.md#publish) |
| [publish](arkts-notification-notification-publish-depr-f.md#publish) |
| [removeAllSlots](arkts-notification-notification-removeallslots-depr-f.md#removeallslots) |
| [removeAllSlots](arkts-notification-notification-removeallslots-depr-f.md#removeallslots) |
| [removeSlot](arkts-notification-notification-removeslot-depr-f.md#removeslot) |
| [removeSlot](arkts-notification-notification-removeslot-depr-f.md#removeslot) |
| [requestEnableNotification](arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification) |
| [requestEnableNotification](arkts-notification-notification-requestenablenotification-depr-f.md#requestenablenotification) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSlot](arkts-notification-notification-addslot-depr-f-sys.md#addslot) |
| [addSlot](arkts-notification-notification-addslot-depr-f-sys.md#addslot) |
| [addSlots](arkts-notification-notification-addslots-depr-f-sys.md#addslots) |
| [addSlots](arkts-notification-notification-addslots-depr-f-sys.md#addslots) |
| [displayBadge](arkts-notification-notification-displaybadge-depr-f-sys.md#displaybadge) |
| [displayBadge](arkts-notification-notification-displaybadge-depr-f-sys.md#displaybadge) |
| [enableDistributed](arkts-notification-notification-enabledistributed-depr-f-sys.md#enabledistributed) |
| [enableDistributed](arkts-notification-notification-enabledistributed-depr-f-sys.md#enabledistributed) |
| [enableDistributedByBundle](arkts-notification-notification-enabledistributedbybundle-depr-f-sys.md#enabledistributedbybundle) |
| [enableDistributedByBundle](arkts-notification-notification-enabledistributedbybundle-depr-f-sys.md#enabledistributedbybundle) |
| [enableNotification](arkts-notification-notification-enablenotification-depr-f-sys.md#enablenotification) |
| [enableNotification](arkts-notification-notification-enablenotification-depr-f-sys.md#enablenotification) |
| [getAllActiveNotifications](arkts-notification-notification-getallactivenotifications-depr-f-sys.md#getallactivenotifications) |
| [getAllActiveNotifications](arkts-notification-notification-getallactivenotifications-depr-f-sys.md#getallactivenotifications) |
| [getDeviceRemindType](arkts-notification-notification-getdeviceremindtype-depr-f-sys.md#getdeviceremindtype) |
| [getDeviceRemindType](arkts-notification-notification-getdeviceremindtype-depr-f-sys.md#getdeviceremindtype) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getdonotdisturbdate) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getdonotdisturbdate) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getdonotdisturbdate) |
| [getDoNotDisturbDate](arkts-notification-notification-getdonotdisturbdate-depr-f-sys.md#getdonotdisturbdate) |
| [getSlotNumByBundle](arkts-notification-notification-getslotnumbybundle-depr-f-sys.md#getslotnumbybundle) |
| [getSlotNumByBundle](arkts-notification-notification-getslotnumbybundle-depr-f-sys.md#getslotnumbybundle) |
| [getSlotsByBundle](arkts-notification-notification-getslotsbybundle-depr-f-sys.md#getslotsbybundle) |
| [getSlotsByBundle](arkts-notification-notification-getslotsbybundle-depr-f-sys.md#getslotsbybundle) |
| [isBadgeDisplayed](arkts-notification-notification-isbadgedisplayed-depr-f-sys.md#isbadgedisplayed) |
| [isBadgeDisplayed](arkts-notification-notification-isbadgedisplayed-depr-f-sys.md#isbadgedisplayed) |
| [isDistributedEnabledByBundle](arkts-notification-notification-isdistributedenabledbybundle-depr-f-sys.md#isdistributedenabledbybundle) |
| [isDistributedEnabledByBundle](arkts-notification-notification-isdistributedenabledbybundle-depr-f-sys.md#isdistributedenabledbybundle) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled) |
| [isNotificationEnabled](arkts-notification-notification-isnotificationenabled-depr-f-sys.md#isnotificationenabled) |
| [publish](arkts-notification-notification-publish-depr-f-sys.md#publish) |
| [publish](arkts-notification-notification-publish-depr-f-sys.md#publish) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove) |
| [remove](arkts-notification-notification-remove-depr-f-sys.md#remove) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall) |
| [removeAll](arkts-notification-notification-removeall-depr-f-sys.md#removeall) |
| [removeGroupByBundle](arkts-notification-notification-removegroupbybundle-depr-f-sys.md#removegroupbybundle) |
| [removeGroupByBundle](arkts-notification-notification-removegroupbybundle-depr-f-sys.md#removegroupbybundle) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setdonotdisturbdate) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setdonotdisturbdate) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setdonotdisturbdate) |
| [setDoNotDisturbDate](arkts-notification-notification-setdonotdisturbdate-depr-f-sys.md#setdonotdisturbdate) |
| [setSlotByBundle](arkts-notification-notification-setslotbybundle-depr-f-sys.md#setslotbybundle) |
| [setSlotByBundle](arkts-notification-notification-setslotbybundle-depr-f-sys.md#setslotbybundle) |
| [subscribe](arkts-notification-notification-subscribe-depr-f-sys.md#subscribe) |
| [subscribe](arkts-notification-notification-subscribe-depr-f-sys.md#subscribe) |
| [subscribe](arkts-notification-notification-subscribe-depr-f-sys.md#subscribe) |
| [supportDoNotDisturbMode](arkts-notification-notification-supportdonotdisturbmode-depr-f-sys.md#supportdonotdisturbmode) |
| [supportDoNotDisturbMode](arkts-notification-notification-supportdonotdisturbmode-depr-f-sys.md#supportdonotdisturbmode) |
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
