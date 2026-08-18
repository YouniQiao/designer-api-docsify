# @ohos.notificationManager

This module provides notification management capabilities, allowing applications to manage the complete lifecycle of notifications. This includes operations such as publishing, updating, and canceling notifications, creating and querying notification slots, querying and requesting authorization status for notification capabilities, setting application badges, and querying stored notifications in the notification center. **APIs used in combination**: The APIs of this module follow the following workflow of notifications: Authorization → Publishing → Cancellation → Channel Management. The APIs are designed to be used in combination with one another. 1. **Authorization query and request process**: Before publishing a notification, first query the authorization status of the notification capability through **isNotificationEnabled**. If the notification capability is not authorized, guide the user to enable the notification permission through **requestEnableNotification**. 2. **Notification publish and update process**: Publish a notification via the **publish** method, with the notification content specified through **NotificationRequest**. If a newly published notification has the same ID and tag as an existing one, the existing notification will be automatically updated. If the ID or tag differs, a new notification will be created instead. 3. **Notification cancellation process**: Cancel a notification with a specified ID through **cancel**, cancel all notifications of this application through **cancelAll**, and cancel notifications under a specified group through **cancelGroup**. 4. **Notification slot management process**: Create a notification slot through **addSlot**, query notification slot configurations through **getSlot** / **getSlots**, and delete notification slots through **removeSlot** / **removeAllSlots**. It is recommended to create the corresponding type of notification slot before publishing a notification. In addition to using **addSlot** to create a notification slot, you can also carry the **notificationSlotType** field in the NotificationRequest when publishing a notification. If a slot of the corresponding type does not exist, it will be automatically created. 5. **Badge management process**: Set the badge number through **setBadgeNumber**, or when publishing a notification through the **publish** API, carry the number of badges to be incremented in the **badgeNumber** field of NotificationRequest. 6. **Stored notification query process**: Obtain the number of stored notifications for this application in the notification center through **getActiveNotificationCount**, and obtain the details of stored notifications for this application in the notification center through **getActiveNotifications**.

**Since:** 23

<!--Device-unnamed-declare namespace notificationManager--><!--Device-unnamed-declare namespace notificationManager-End-->

**System capability:** SystemCapability.Notification.Notification

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSlot](arkts-notification-notificationmanager-addslot-f.md#addslot) |
| [addSlot](arkts-notification-notificationmanager-addslot-f.md#addslot) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md#cancel) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md#cancel) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md#cancel) |
| [cancelAll](arkts-notification-notificationmanager-cancelall-f.md#cancelall) |
| [cancelAll](arkts-notification-notificationmanager-cancelall-f.md#cancelall) |
| [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md#cancelgroup) |
| [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md#cancelgroup) |
| [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md#getactivenotificationcount) |
| [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md#getactivenotificationcount) |
| [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md#getactivenotifications) |
| [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md#getactivenotifications) |
| [getBadgeNumber](arkts-notification-notificationmanager-getbadgenumber-f.md#getbadgenumber) |
| [getNotificationParameters](arkts-notification-notificationmanager-getnotificationparameters-f.md#getnotificationparameters) |
| [getNotificationParameters](arkts-notification-notificationmanager-getnotificationparameters-f.md#getnotificationparameters) |
| [getNotificationSetting](arkts-notification-notificationmanager-getnotificationsetting-f.md#getnotificationsetting) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getslot) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getslot) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getslot) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getslot) |
| [getSlots](arkts-notification-notificationmanager-getslots-f.md#getslots) |
| [getSlots](arkts-notification-notificationmanager-getslots-f.md#getslots) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md#isdistributedenabled) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md#isdistributedenabled) |
| [isGeofenceEnabled](arkts-notification-notificationmanager-isgeofenceenabled-f.md#isgeofenceenabled) |
| [isNotificationEnabledSync](arkts-notification-notificationmanager-isnotificationenabledsync-f.md#isnotificationenabledsync) |
| [isSupportTemplate](arkts-notification-notificationmanager-issupporttemplate-f.md#issupporttemplate) |
| [isSupportTemplate](arkts-notification-notificationmanager-issupporttemplate-f.md#issupporttemplate) |
| [openNotificationSettings](arkts-notification-notificationmanager-opennotificationsettings-f.md#opennotificationsettings) |
| [openNotificationSettingsWithResult](arkts-notification-notificationmanager-opennotificationsettingswithresult-f.md#opennotificationsettingswithresult) |
| [publish](arkts-notification-notificationmanager-publish-f.md#publish) |
| [publish](arkts-notification-notificationmanager-publish-f.md#publish) |
| [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md#removeallslots) |
| [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md#removeallslots) |
| [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeslot) |
| [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeslot) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestenablenotification) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestenablenotification) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestenablenotification) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestenablenotification) |
| [setBadgeNumber](arkts-notification-notificationmanager-setbadgenumber-f.md#setbadgenumber) |
| [setBadgeNumber](arkts-notification-notificationmanager-setbadgenumber-f.md#setbadgenumber) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md#adddonotdisturbprofile-system-api) |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md#adddonotdisturbprofile-system-api) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md#addslot-system-api) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md#addslot-system-api) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md#addslots-system-api) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md#addslots-system-api) |
| [cancel](arkts-notification-notificationmanager-cancel-f-sys.md#cancel-system-api) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelasbundle-system-api) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelasbundle-system-api) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelasbundle-system-api) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md#disablenotificationfeature-system-api) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md#disablenotificationfeature-system-api) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displaybadge-system-api) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displaybadge-system-api) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getactivenotificationbyfilter-system-api) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getactivenotificationbyfilter-system-api) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getactivenotificationbyfilter-system-api) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getactivenotificationbyfilter-system-api) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md#getallactivenotifications-system-api) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md#getallactivenotifications-system-api) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md#getallnotificationenabledbundles-system-api) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md#getallnotificationenabledbundles-system-api) |
| [getBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-getbadgedisplaystatusbybundles-f-sys.md#getbadgedisplaystatusbybundles-system-api) |
| [getBundlePriorityConfig](arkts-notification-notificationmanager-getbundlepriorityconfig-f-sys.md#getbundlepriorityconfig-system-api) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md#getdeviceremindtype-system-api) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md#getdeviceremindtype-system-api) |
| [getDistributedDeviceList](arkts-notification-notificationmanager-getdistributeddevicelist-f-sys.md#getdistributeddevicelist-system-api) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-system-api) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-system-api) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-system-api) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-system-api) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md#getdonotdisturbprofile-system-api) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md#getdonotdisturbprofile-system-api) |
| [getNotificationStatisticsByBundle](arkts-notification-notificationmanager-getnotificationstatisticsbybundle-f-sys.md#getnotificationstatisticsbybundle-system-api) |
| [getNotificationSwitch](arkts-notification-notificationmanager-getnotificationswitch-f-sys.md#getnotificationswitch-system-api) |
| [getPriorityEnabledByBundles](arkts-notification-notificationmanager-getpriorityenabledbybundles-f-sys.md#getpriorityenabledbybundles-system-api) |
| [getPriorityStrategyByBundles](arkts-notification-notificationmanager-getprioritystrategybybundles-f-sys.md#getprioritystrategybybundles-system-api) |
| [getReminderInfoByBundles](arkts-notification-notificationmanager-getreminderinfobybundles-f-sys.md#getreminderinfobybundles-system-api) |
| [getRingtoneInfoByBundle](arkts-notification-notificationmanager-getringtoneinfobybundle-f-sys.md#getringtoneinfobybundle-system-api) |
| [getSlotByBundle](arkts-notification-notificationmanager-getslotbybundle-f-sys.md#getslotbybundle-system-api) |
| [getSlotByBundle](arkts-notification-notificationmanager-getslotbybundle-f-sys.md#getslotbybundle-system-api) |
| [getSlotFlagsByBundle](arkts-notification-notificationmanager-getslotflagsbybundle-f-sys.md#getslotflagsbybundle-system-api) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md#getslotnumbybundle-system-api) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md#getslotnumbybundle-system-api) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md#getslotsbybundle-system-api) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md#getslotsbybundle-system-api) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md#getsyncnotificationenabledwithoutapp-system-api) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md#getsyncnotificationenabledwithoutapp-system-api) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isbadgedisplayed-system-api) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isbadgedisplayed-system-api) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f-sys.md#isdistributedenabled-system-api) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isdistributedenabledbybundle-system-api) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isdistributedenabledbybundle-system-api) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isdistributedenabledbybundle-system-api) |
| [isDistributedEnabledBySlot](arkts-notification-notificationmanager-isdistributedenabledbyslot-f-sys.md#isdistributedenabledbyslot-system-api) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled-system-api) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled-system-api) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled-system-api) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled-system-api) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled-system-api) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled-system-api) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md#isnotificationslotenabled-system-api) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md#isnotificationslotenabled-system-api) |
| [isNotificationSlotEnabledByBundles](arkts-notification-notificationmanager-isnotificationslotenabledbybundles-f-sys.md#isnotificationslotenabledbybundles-system-api) |
| [isPriorityEnabled](arkts-notification-notificationmanager-ispriorityenabled-f-sys.md#ispriorityenabled-system-api) |
| [isPriorityEnabledByBundle](arkts-notification-notificationmanager-ispriorityenabledbybundle-f-sys.md#ispriorityenabledbybundle-system-api) |
| [isPriorityIntelligentEnabled](arkts-notification-notificationmanager-ispriorityintelligentenabled-f-sys.md#ispriorityintelligentenabled-system-api) |
| [isSilentReminderEnabled](arkts-notification-notificationmanager-issilentreminderenabled-f-sys.md#issilentreminderenabled-system-api) |
| [isSmartReminderEnabled](arkts-notification-notificationmanager-issmartreminderenabled-f-sys.md#issmartreminderenabled-system-api) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md#issupportdonotdisturbmode-system-api) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md#issupportdonotdisturbmode-system-api) |
| [offBadgeNumberQuery](arkts-notification-notificationmanager-offbadgenumberquery-f-sys.md#offbadgenumberquery-system-api) |
| [offCheckNotification](arkts-notification-notificationmanager-offchecknotification-f-sys.md#offchecknotification) |
| [off_checkNotification](arkts-notification-notificationmanager-offchecknotification-f-sys.md#offchecknotification) |
| [onBadgeNumberQuery](arkts-notification-notificationmanager-onbadgenumberquery-f-sys.md#onbadgenumberquery-system-api) |
| [onCheckNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md#onchecknotification) |
| [onCheckNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md#onchecknotification-system-api) |
| [on_checkNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md#onchecknotification) |
| [on_checkNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md#onchecknotification-system-api) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md#publish-system-api) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md#publish-system-api) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishasbundle-system-api) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishasbundle-system-api) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishasbundle-system-api) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md#removedonotdisturbprofile-system-api) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md#removedonotdisturbprofile-system-api) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md#removegroupbybundle-system-api) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md#removegroupbybundle-system-api) |
| [setAdditionalConfig](arkts-notification-notificationmanager-setadditionalconfig-f-sys.md#setadditionalconfig-system-api) |
| [setBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-setbadgedisplaystatusbybundles-f-sys.md#setbadgedisplaystatusbybundles-system-api) |
| [setBadgeNumberByBundle](arkts-notification-notificationmanager-setbadgenumberbybundle-f-sys.md#setbadgenumberbybundle-system-api) |
| [setBundlePriorityConfig](arkts-notification-notificationmanager-setbundlepriorityconfig-f-sys.md#setbundlepriorityconfig-system-api) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setdistributedenable-system-api) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setdistributedenable-system-api) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setdistributedenablebybundle-system-api) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setdistributedenablebybundle-system-api) |
| [setDistributedEnableByBundles](arkts-notification-notificationmanager-setdistributedenablebybundles-f-sys.md#setdistributedenablebybundles-system-api) |
| [setDistributedEnabled](arkts-notification-notificationmanager-setdistributedenabled-f-sys.md#setdistributedenabled-system-api) |
| [setDistributedEnabledByBundle](arkts-notification-notificationmanager-setdistributedenabledbybundle-f-sys.md#setdistributedenabledbybundle-system-api) |
| [setDistributedEnabledBySlot](arkts-notification-notificationmanager-setdistributedenabledbyslot-f-sys.md#setdistributedenabledbyslot-system-api) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-system-api) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-system-api) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-system-api) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-system-api) |
| [setGeofenceEnabled](arkts-notification-notificationmanager-setgeofenceenabled-f-sys.md#setgeofenceenabled-system-api) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md#setnotificationenable-system-api) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md#setnotificationenable-system-api) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setnotificationenableslot-system-api) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setnotificationenableslot-system-api) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setnotificationenableslot-system-api) |
| [setNotificationSwitch](arkts-notification-notificationmanager-setnotificationswitch-f-sys.md#setnotificationswitch-system-api) |
| [setPriorityEnabled](arkts-notification-notificationmanager-setpriorityenabled-f-sys.md#setpriorityenabled-system-api) |
| [setPriorityEnabledByBundle](arkts-notification-notificationmanager-setpriorityenabledbybundle-f-sys.md#setpriorityenabledbybundle-system-api) |
| [setPriorityEnabledByBundles](arkts-notification-notificationmanager-setpriorityenabledbybundles-f-sys.md#setpriorityenabledbybundles-system-api) |
| [setPriorityIntelligentEnabled](arkts-notification-notificationmanager-setpriorityintelligentenabled-f-sys.md#setpriorityintelligentenabled-system-api) |
| [setPriorityStrategyByBundles](arkts-notification-notificationmanager-setprioritystrategybybundles-f-sys.md#setprioritystrategybybundles-system-api) |
| [setReminderInfoByBundles](arkts-notification-notificationmanager-setreminderinfobybundles-f-sys.md#setreminderinfobybundles-system-api) |
| [setRingtoneInfoByBundle](arkts-notification-notificationmanager-setringtoneinfobybundle-f-sys.md#setringtoneinfobybundle-system-api) |
| [setSilentReminderEnabled](arkts-notification-notificationmanager-setsilentreminderenabled-f-sys.md#setsilentreminderenabled-system-api) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md#setslotbybundle-system-api) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md#setslotbybundle-system-api) |
| [setSlotFlagsByBundle](arkts-notification-notificationmanager-setslotflagsbybundle-f-sys.md#setslotflagsbybundle-system-api) |
| [setSmartReminderEnabled](arkts-notification-notificationmanager-setsmartreminderenabled-f-sys.md#setsmartreminderenabled-system-api) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md#setsyncnotificationenabledwithoutapp-system-api) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md#setsyncnotificationenabledwithoutapp-system-api) |
| [setTargetDeviceStatus](arkts-notification-notificationmanager-settargetdevicestatus-f-sys.md#settargetdevicestatus-system-api) |
| [snoozeNotification](arkts-notification-notificationmanager-snoozenotification-f-sys.md#snoozenotification-system-api) |
| [subscribeSystemLiveView](arkts-notification-notificationmanager-subscribesystemliveview-f-sys.md#subscribesystemliveview-system-api) |
| [triggerSystemLiveView](arkts-notification-notificationmanager-triggersystemliveview-f-sys.md#triggersystemliveview-system-api) |
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
