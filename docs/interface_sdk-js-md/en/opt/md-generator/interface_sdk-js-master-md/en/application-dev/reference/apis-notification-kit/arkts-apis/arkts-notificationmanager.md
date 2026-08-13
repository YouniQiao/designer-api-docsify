# @ohos.notificationManager

This module provides notification management capabilities, allowing applications to manage the complete lifecycle of notifications. This includes operations such as publishing, updating, and canceling notifications, creating and querying notification slots, querying and requesting authorization status for notification capabilities, setting application badges, and querying stored notifications in the notification center. **APIs used in combination**: The APIs of this module follow the following workflow of notifications: Authorization → Publishing → Cancellation → Channel Management. The APIs are designed to be used in combination with one another. 1. **Authorization query and request process**: Before publishing a notification, first query the authorization status of the notification capability through **isNotificationEnabled**. If the notification capability is not authorized, guide the user to enable the notification permission through **requestEnableNotification**. 2. **Notification publish and update process**: Publish a notification via the **publish** method, with the notification content specified through **NotificationRequest**. If a newly published notification has the same ID and tag as an existing one, the existing notification will be automatically updated. If the ID or tag differs, a new notification will be created instead. 3. **Notification cancellation process**: Cancel a notification with a specified ID through **cancel**, cancel all notifications of this application through **cancelAll**, and cancel notifications under a specified group through **cancelGroup**. 4. **Notification slot management process**: Create a notification slot through **addSlot**, query notification slot configurations through **getSlot** / **getSlots**, and delete notification slots through **removeSlot** / **removeAllSlots**. It is recommended to create the corresponding type of notification slot before publishing a notification. In addition to using **addSlot** to create a notification slot, you can also carry the **notificationSlotType** field in the NotificationRequest when publishing a notification. If a slot of the corresponding type does not exist, it will be automatically created. 5. **Badge management process**: Set the badge number through **setBadgeNumber**, or when publishing a notification through the **publish** API, carry the number of badges to be incremented in the **badgeNumber** field of NotificationRequest. 6. **Stored notification query process**: Obtain the number of stored notifications for this application in the notification center through **getActiveNotificationCount**, and obtain the details of stored notifications for this application in the notification center through **getActiveNotifications**.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace notificationManager--><!--Device-unnamed-declare namespace notificationManager-End-->

**System capability:** SystemCapability.Notification.Notification

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSlot](arkts-notification-notificationmanager-addslot-f.md#addSlot) |
| [addSlot](arkts-notification-notificationmanager-addslot-f.md#addSlot) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md#cancel) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md#cancel) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md#cancel) |
| [cancelAll](arkts-notification-notificationmanager-cancelall-f.md#cancelAll) |
| [cancelAll](arkts-notification-notificationmanager-cancelall-f.md#cancelAll) |
| [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md#cancelGroup) |
| [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md#cancelGroup) |
| [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md#getActiveNotificationCount) |
| [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md#getActiveNotificationCount) |
| [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md#getActiveNotifications) |
| [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md#getActiveNotifications) |
| [getBadgeNumber](arkts-notification-notificationmanager-getbadgenumber-f.md#getBadgeNumber) |
| [getNotificationParameters](arkts-notification-notificationmanager-getnotificationparameters-f.md#getNotificationParameters) |
| [getNotificationParameters](arkts-notification-notificationmanager-getnotificationparameters-f.md#getNotificationParameters) |
| [getNotificationSetting](arkts-notification-notificationmanager-getnotificationsetting-f.md#getNotificationSetting) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getSlot) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getSlot) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getSlot) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getSlot) |
| [getSlots](arkts-notification-notificationmanager-getslots-f.md#getSlots) |
| [getSlots](arkts-notification-notificationmanager-getslots-f.md#getSlots) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md#isDistributedEnabled) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md#isDistributedEnabled) |
| [isGeofenceEnabled](arkts-notification-notificationmanager-isgeofenceenabled-f.md#isGeofenceEnabled) |
| [isNotificationEnabledSync](arkts-notification-notificationmanager-isnotificationenabledsync-f.md#isNotificationEnabledSync) |
| [isSupportTemplate](arkts-notification-notificationmanager-issupporttemplate-f.md#isSupportTemplate) |
| [isSupportTemplate](arkts-notification-notificationmanager-issupporttemplate-f.md#isSupportTemplate) |
| [openNotificationSettings](arkts-notification-notificationmanager-opennotificationsettings-f.md#openNotificationSettings) |
| [openNotificationSettingsWithResult](arkts-notification-notificationmanager-opennotificationsettingswithresult-f.md#openNotificationSettingsWithResult) |
| [publish](arkts-notification-notificationmanager-publish-f.md#publish) |
| [publish](arkts-notification-notificationmanager-publish-f.md#publish) |
| [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md#removeAllSlots) |
| [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md#removeAllSlots) |
| [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeSlot) |
| [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeSlot) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestEnableNotification) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestEnableNotification) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestEnableNotification) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestEnableNotification) |
| [setBadgeNumber](arkts-notification-notificationmanager-setbadgenumber-f.md#setBadgeNumber) |
| [setBadgeNumber](arkts-notification-notificationmanager-setbadgenumber-f.md#setBadgeNumber) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md#addDoNotDisturbProfile-(System-API)) |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md#addDoNotDisturbProfile-(System-API)) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md#addSlot-(System-API)) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md#addSlot-(System-API)) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md#addSlots-(System-API)) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md#addSlots-(System-API)) |
| [cancel](arkts-notification-notificationmanager-cancel-f-sys.md#cancel-(System-API)) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelAsBundle-(System-API)) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelAsBundle-(System-API)) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelAsBundle-(System-API)) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md#disableNotificationFeature-(System-API)) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md#disableNotificationFeature-(System-API)) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displayBadge-(System-API)) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displayBadge-(System-API)) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getActiveNotificationByFilter-(System-API)) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getActiveNotificationByFilter-(System-API)) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getActiveNotificationByFilter-(System-API)) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getActiveNotificationByFilter-(System-API)) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md#getAllActiveNotifications-(System-API)) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md#getAllActiveNotifications-(System-API)) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md#getAllNotificationEnabledBundles-(System-API)) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md#getAllNotificationEnabledBundles-(System-API)) |
| [getBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-getbadgedisplaystatusbybundles-f-sys.md#getBadgeDisplayStatusByBundles-(System-API)) |
| [getBundlePriorityConfig](arkts-notification-notificationmanager-getbundlepriorityconfig-f-sys.md#getBundlePriorityConfig-(System-API)) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md#getDeviceRemindType-(System-API)) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md#getDeviceRemindType-(System-API)) |
| [getDistributedDeviceList](arkts-notification-notificationmanager-getdistributeddevicelist-f-sys.md#getDistributedDeviceList-(System-API)) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getDoNotDisturbDate-(System-API)) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getDoNotDisturbDate-(System-API)) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getDoNotDisturbDate-(System-API)) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getDoNotDisturbDate-(System-API)) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md#getDoNotDisturbProfile-(System-API)) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md#getDoNotDisturbProfile-(System-API)) |
| [getNotificationStatisticsByBundle](arkts-notification-notificationmanager-getnotificationstatisticsbybundle-f-sys.md#getNotificationStatisticsByBundle-(System-API)) |
| [getNotificationSwitch](arkts-notification-notificationmanager-getnotificationswitch-f-sys.md#getNotificationSwitch-(System-API)) |
| [getPriorityEnabledByBundles](arkts-notification-notificationmanager-getpriorityenabledbybundles-f-sys.md#getPriorityEnabledByBundles-(System-API)) |
| [getPriorityStrategyByBundles](arkts-notification-notificationmanager-getprioritystrategybybundles-f-sys.md#getPriorityStrategyByBundles-(System-API)) |
| [getReminderInfoByBundles](arkts-notification-notificationmanager-getreminderinfobybundles-f-sys.md#getReminderInfoByBundles-(System-API)) |
| [getRingtoneInfoByBundle](arkts-notification-notificationmanager-getringtoneinfobybundle-f-sys.md#getRingtoneInfoByBundle-(System-API)) |
| [getSlotByBundle](arkts-notification-notificationmanager-getslotbybundle-f-sys.md#getSlotByBundle-(System-API)) |
| [getSlotByBundle](arkts-notification-notificationmanager-getslotbybundle-f-sys.md#getSlotByBundle-(System-API)) |
| [getSlotFlagsByBundle](arkts-notification-notificationmanager-getslotflagsbybundle-f-sys.md#getSlotFlagsByBundle-(System-API)) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md#getSlotNumByBundle-(System-API)) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md#getSlotNumByBundle-(System-API)) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md#getSlotsByBundle-(System-API)) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md#getSlotsByBundle-(System-API)) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md#getSyncNotificationEnabledWithoutApp-(System-API)) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md#getSyncNotificationEnabledWithoutApp-(System-API)) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isBadgeDisplayed-(System-API)) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isBadgeDisplayed-(System-API)) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f-sys.md#isDistributedEnabled-(System-API)) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isDistributedEnabledByBundle-(System-API)) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isDistributedEnabledByBundle-(System-API)) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isDistributedEnabledByBundle-(System-API)) |
| [isDistributedEnabledBySlot](arkts-notification-notificationmanager-isdistributedenabledbyslot-f-sys.md#isDistributedEnabledBySlot-(System-API)) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled-(System-API)) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled-(System-API)) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled-(System-API)) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled-(System-API)) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled-(System-API)) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled-(System-API)) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md#isNotificationSlotEnabled-(System-API)) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md#isNotificationSlotEnabled-(System-API)) |
| [isNotificationSlotEnabledByBundles](arkts-notification-notificationmanager-isnotificationslotenabledbybundles-f-sys.md#isNotificationSlotEnabledByBundles-(System-API)) |
| [isPriorityEnabled](arkts-notification-notificationmanager-ispriorityenabled-f-sys.md#isPriorityEnabled-(System-API)) |
| [isPriorityEnabledByBundle](arkts-notification-notificationmanager-ispriorityenabledbybundle-f-sys.md#isPriorityEnabledByBundle-(System-API)) |
| [isPriorityIntelligentEnabled](arkts-notification-notificationmanager-ispriorityintelligentenabled-f-sys.md#isPriorityIntelligentEnabled-(System-API)) |
| [isSilentReminderEnabled](arkts-notification-notificationmanager-issilentreminderenabled-f-sys.md#isSilentReminderEnabled-(System-API)) |
| [isSmartReminderEnabled](arkts-notification-notificationmanager-issmartreminderenabled-f-sys.md#isSmartReminderEnabled-(System-API)) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md#isSupportDoNotDisturbMode-(System-API)) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md#isSupportDoNotDisturbMode-(System-API)) |
| [offBadgeNumberQuery](arkts-notification-notificationmanager-offbadgenumberquery-f-sys.md#offBadgeNumberQuery-(System-API)) |
| [offCheckNotification](arkts-notification-notificationmanager-offchecknotification-f-sys.md#offCheckNotification-(System-API)) |
| [off_checkNotification](arkts-notification-notificationmanager-offchecknotification-f-sys.md) |
| [onBadgeNumberQuery](arkts-notification-notificationmanager-onbadgenumberquery-f-sys.md#onBadgeNumberQuery-(System-API)) |
| [onCheckNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md#onCheckNotification-(System-API)) |
| [onCheckNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md#onCheckNotification-(System-API)) |
| [on_checkNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md) |
| [on_checkNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md#publish-(System-API)) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md#publish-(System-API)) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishAsBundle-(System-API)) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishAsBundle-(System-API)) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishAsBundle-(System-API)) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md#removeDoNotDisturbProfile-(System-API)) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md#removeDoNotDisturbProfile-(System-API)) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md#removeGroupByBundle-(System-API)) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md#removeGroupByBundle-(System-API)) |
| [setAdditionalConfig](arkts-notification-notificationmanager-setadditionalconfig-f-sys.md#setAdditionalConfig-(System-API)) |
| [setBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-setbadgedisplaystatusbybundles-f-sys.md#setBadgeDisplayStatusByBundles-(System-API)) |
| [setBadgeNumberByBundle](arkts-notification-notificationmanager-setbadgenumberbybundle-f-sys.md#setBadgeNumberByBundle-(System-API)) |
| [setBundlePriorityConfig](arkts-notification-notificationmanager-setbundlepriorityconfig-f-sys.md#setBundlePriorityConfig-(System-API)) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setDistributedEnable-(System-API)) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setDistributedEnable-(System-API)) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setDistributedEnableByBundle-(System-API)) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setDistributedEnableByBundle-(System-API)) |
| [setDistributedEnableByBundles](arkts-notification-notificationmanager-setdistributedenablebybundles-f-sys.md#setDistributedEnableByBundles-(System-API)) |
| [setDistributedEnabled](arkts-notification-notificationmanager-setdistributedenabled-f-sys.md#setDistributedEnabled-(System-API)) |
| [setDistributedEnabledByBundle](arkts-notification-notificationmanager-setdistributedenabledbybundle-f-sys.md#setDistributedEnabledByBundle-(System-API)) |
| [setDistributedEnabledBySlot](arkts-notification-notificationmanager-setdistributedenabledbyslot-f-sys.md#setDistributedEnabledBySlot-(System-API)) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setDoNotDisturbDate-(System-API)) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setDoNotDisturbDate-(System-API)) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setDoNotDisturbDate-(System-API)) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setDoNotDisturbDate-(System-API)) |
| [setGeofenceEnabled](arkts-notification-notificationmanager-setgeofenceenabled-f-sys.md#setGeofenceEnabled-(System-API)) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md#setNotificationEnable-(System-API)) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md#setNotificationEnable-(System-API)) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setNotificationEnableSlot-(System-API)) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setNotificationEnableSlot-(System-API)) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setNotificationEnableSlot-(System-API)) |
| [setNotificationSwitch](arkts-notification-notificationmanager-setnotificationswitch-f-sys.md#setNotificationSwitch-(System-API)) |
| [setPriorityEnabled](arkts-notification-notificationmanager-setpriorityenabled-f-sys.md#setPriorityEnabled-(System-API)) |
| [setPriorityEnabledByBundle](arkts-notification-notificationmanager-setpriorityenabledbybundle-f-sys.md#setPriorityEnabledByBundle-(System-API)) |
| [setPriorityEnabledByBundles](arkts-notification-notificationmanager-setpriorityenabledbybundles-f-sys.md#setPriorityEnabledByBundles-(System-API)) |
| [setPriorityIntelligentEnabled](arkts-notification-notificationmanager-setpriorityintelligentenabled-f-sys.md#setPriorityIntelligentEnabled-(System-API)) |
| [setPriorityStrategyByBundles](arkts-notification-notificationmanager-setprioritystrategybybundles-f-sys.md#setPriorityStrategyByBundles-(System-API)) |
| [setReminderInfoByBundles](arkts-notification-notificationmanager-setreminderinfobybundles-f-sys.md#setReminderInfoByBundles-(System-API)) |
| [setRingtoneInfoByBundle](arkts-notification-notificationmanager-setringtoneinfobybundle-f-sys.md#setRingtoneInfoByBundle-(System-API)) |
| [setSilentReminderEnabled](arkts-notification-notificationmanager-setsilentreminderenabled-f-sys.md#setSilentReminderEnabled-(System-API)) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md#setSlotByBundle-(System-API)) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md#setSlotByBundle-(System-API)) |
| [setSlotFlagsByBundle](arkts-notification-notificationmanager-setslotflagsbybundle-f-sys.md#setSlotFlagsByBundle-(System-API)) |
| [setSmartReminderEnabled](arkts-notification-notificationmanager-setsmartreminderenabled-f-sys.md#setSmartReminderEnabled-(System-API)) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md#setSyncNotificationEnabledWithoutApp-(System-API)) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md#setSyncNotificationEnabledWithoutApp-(System-API)) |
| [setTargetDeviceStatus](arkts-notification-notificationmanager-settargetdevicestatus-f-sys.md#setTargetDeviceStatus-(System-API)) |
| [snoozeNotification](arkts-notification-notificationmanager-snoozenotification-f-sys.md#snoozeNotification-(System-API)) |
| [subscribeSystemLiveView](arkts-notification-notificationmanager-subscribesystemliveview-f-sys.md#subscribeSystemLiveView-(System-API)) |
| [triggerSystemLiveView](arkts-notification-notificationmanager-triggersystemliveview-f-sys.md#triggerSystemLiveView-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NotificationSetting](arkts-notification-notificationmanager-notificationsetting-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BundleNotificationStatistics](arkts-notification-notificationmanager-bundlenotificationstatistics-i-sys.md) |
| [ButtonOptions](arkts-notification-notificationmanager-buttonoptions-i-sys.md) |
| [DistributedBundleEnableInfo](arkts-notification-notificationmanager-distributedbundleenableinfo-i-sys.md) |
| [DoNotDisturbDate](arkts-notification-notificationmanager-donotdisturbdate-i-sys.md) |
| [DoNotDisturbProfile](arkts-notification-notificationmanager-donotdisturbprofile-i-sys.md) |
| [NotificationCheckInfo](arkts-notification-notificationmanager-notificationcheckinfo-i-sys.md) |
| [NotificationCheckResult](arkts-notification-notificationmanager-notificationcheckresult-i-sys.md) |
| [NotificationReminderInfo](arkts-notification-notificationmanager-notificationreminderinfo-i-sys.md) |
| [RingtoneInfo](arkts-notification-notificationmanager-ringtoneinfo-i-sys.md) |
| [SystemLiveViewSubscriber](arkts-notification-notificationmanager-systemliveviewsubscriber-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ContentType](arkts-notification-notificationmanager-contenttype-e.md) |
| [PriorityNotificationType](arkts-notification-notificationmanager-prioritynotificationtype-e.md) |
| [SlotLevel](arkts-notification-notificationmanager-slotlevel-e.md) |
| [SlotType](arkts-notification-notificationmanager-slottype-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeviceRemindType](arkts-notification-notificationmanager-deviceremindtype-e-sys.md) |
| [DoNotDisturbType](arkts-notification-notificationmanager-donotdisturbtype-e-sys.md) |
| [NotificationControlFlagStatus](arkts-notification-notificationmanager-notificationcontrolflagstatus-e-sys.md) |
| [PriorityEnableStatus](arkts-notification-notificationmanager-priorityenablestatus-e-sys.md) |
| [PriorityNotificationType](arkts-notification-notificationmanager-prioritynotificationtype-e-sys.md) |
| [PriorityStrategyStatus](arkts-notification-notificationmanager-prioritystrategystatus-e-sys.md) |
| [RingtoneType](arkts-notification-notificationmanager-ringtonetype-e-sys.md) |
| [SlotType](arkts-notification-notificationmanager-slottype-e-sys.md) |
| [SourceType](arkts-notification-notificationmanager-sourcetype-e-sys.md) |
| [SwitchState](arkts-notification-notificationmanager-switchstate-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BundleOption](arkts-notification-notificationmanager-bundleoption-t.md) |
| [DistributedOptions](arkts-notification-notificationmanager-distributedoptions-t.md) |
| [NotificationActionButton](arkts-notification-notificationmanager-notificationactionbutton-t.md) |
| [NotificationBasicContent](arkts-notification-notificationmanager-notificationbasiccontent-t.md) |
| [NotificationButton](arkts-notification-notificationmanager-notificationbutton-t.md) |
| [NotificationCapsule](arkts-notification-notificationmanager-notificationcapsule-t.md) |
| [NotificationContent](arkts-notification-notificationmanager-notificationcontent-t.md) |
| [NotificationLongTextContent](arkts-notification-notificationmanager-notificationlongtextcontent-t.md) |
| [NotificationMultiLineContent](arkts-notification-notificationmanager-notificationmultilinecontent-t.md) |
| [NotificationParameters](arkts-notification-notificationmanager-notificationparameters-t.md) |
| [NotificationPictureContent](arkts-notification-notificationmanager-notificationpicturecontent-t.md) |
| [NotificationProgress](arkts-notification-notificationmanager-notificationprogress-t.md) |
| [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) |
| [NotificationSlot](arkts-notification-notificationmanager-notificationslot-t.md) |
| [NotificationSystemLiveViewContent](arkts-notification-notificationmanager-notificationsystemliveviewcontent-t.md) |
| [NotificationTemplate](arkts-notification-notificationmanager-notificationtemplate-t.md) |
| [NotificationTime](arkts-notification-notificationmanager-notificationtime-t.md) |
| [NotificationUserInput](arkts-notification-notificationmanager-notificationuserinput-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CoordinateSystemType](arkts-notification-notificationmanager-coordinatesystemtype-t-sys.md) |
| [Geofence](arkts-notification-notificationmanager-geofence-t-sys.md) |
| [GroupInfo](arkts-notification-notificationmanager-groupinfo-t-sys.md) |
| [LiveViewStatus](arkts-notification-notificationmanager-liveviewstatus-t-sys.md) |
| [LiveViewTypes](arkts-notification-notificationmanager-liveviewtypes-t-sys.md) |
| [MonitorEvent](arkts-notification-notificationmanager-monitorevent-t-sys.md) |
| [NotificationCheckRequest](arkts-notification-notificationmanager-notificationcheckrequest-t-sys.md) |
| [NotificationFilter](arkts-notification-notificationmanager-notificationfilter-t-sys.md) |
| [NotificationFlagStatus](arkts-notification-notificationmanager-notificationflagstatus-t-sys.md) |
| [NotificationFlags](arkts-notification-notificationmanager-notificationflags-t-sys.md) |
| [NotificationIconButton](arkts-notification-notificationmanager-notificationiconbutton-t-sys.md) |
| [NotificationLiveViewContent](arkts-notification-notificationmanager-notificationliveviewcontent-t-sys.md) |
| [NotificationSorting](arkts-notification-notificationmanager-notificationsorting-t-sys.md) |
| [Trigger](arkts-notification-notificationmanager-trigger-t-sys.md) |
| [TriggerType](arkts-notification-notificationmanager-triggertype-t-sys.md) |
| [UnifiedGroupInfo](arkts-notification-notificationmanager-unifiedgroupinfo-t-sys.md) |
<!--DelEnd-->
