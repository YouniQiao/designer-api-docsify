# @ohos.notificationManager

This module provides notification management capabilities, allowing applications to manage the complete lifecycle of notifications. This includes operations such as publishing, updating, and canceling notifications, creating and querying notification slots, querying and requesting authorization status for notification capabilities, setting application badges, and querying stored notifications in the notification center.  
**APIs used in combination**:The APIs of this module follow the following workflow of notifications: Authorization → Publishing → Cancellation → Channel Management. The APIs are designed to be used in combination with one another.
1. **Authorization query and request process**: Before publishing a notification, first query the authorization
status of the notification capability through **isNotificationEnabled**. If the notification capability is not authorized, guide the user to enable the notification permission through **requestEnableNotification**.
2. **Notification publish and update process**: Publish a notification via the **publish** method, with the
notification content specified through **NotificationRequest**. If a newly published notification has the same ID and tag as an existing one, the existing notification will be automatically updated. If the ID or tag differs, a new notification will be created instead.
3. **Notification cancellation process**: Cancel a notification with a specified ID through **cancel**, cancel all
notifications of this application through **cancelAll**, and cancel notifications under a specified group through **cancelGroup**.
4. **Notification slot management process**: Create a notification slot through **addSlot**, query notification slot
configurations through **getSlot** / **getSlots**, and delete notification slots through **removeSlot** / **removeAllSlots**. It is recommended to create the corresponding type of notification slot before publishing a notification. In addition to using **addSlot** to create a notification slot, you can also carry the **notificationSlotType** field in the NotificationRequest when publishing a notification. If a slot of the corresponding type does not exist, it will be automatically created.
5. **Badge management process**: Set the badge number through **setBadgeNumber**, or when publishing a notification
through the **publish** API, carry the number of badges to be incremented in the **badgeNumber** field of NotificationRequest.
6. **Stored notification query process**: Obtain the number of stored notifications for this application in the
notification center through **getActiveNotificationCount**, and obtain the details of stored notifications for this application in the notification center through **getActiveNotifications**.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Notification.Notification

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addSlot](arkts-notification-notificationmanager-addslot-f.md) |
| [addSlot](arkts-notification-notificationmanager-addslot-f.md) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md) |
| [cancelAll](arkts-notification-notificationmanager-cancelall-f.md) |
| [cancelAll](arkts-notification-notificationmanager-cancelall-f.md) |
| [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md) |
| [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md) |
| [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md) |
| [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md) |
| [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md) |
| [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md) |
| [getBadgeNumber](arkts-notification-notificationmanager-getbadgenumber-f.md) |
| [getNotificationParameters](arkts-notification-notificationmanager-getnotificationparameters-f.md) |
| [getNotificationParameters](arkts-notification-notificationmanager-getnotificationparameters-f.md) |
| [getNotificationSetting](arkts-notification-notificationmanager-getnotificationsetting-f.md) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md) |
| [getSlots](arkts-notification-notificationmanager-getslots-f.md) |
| [getSlots](arkts-notification-notificationmanager-getslots-f.md) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md) |
| [isGeofenceEnabled](arkts-notification-notificationmanager-isgeofenceenabled-f.md) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md) |
| [isNotificationEnabledSync](arkts-notification-notificationmanager-isnotificationenabledsync-f.md) |
| [isSupportTemplate](arkts-notification-notificationmanager-issupporttemplate-f.md) |
| [isSupportTemplate](arkts-notification-notificationmanager-issupporttemplate-f.md) |
| [openNotificationSettings](arkts-notification-notificationmanager-opennotificationsettings-f.md) |
| [openNotificationSettingsWithResult](arkts-notification-notificationmanager-opennotificationsettingswithresult-f.md) |
| [publish](arkts-notification-notificationmanager-publish-f.md) |
| [publish](arkts-notification-notificationmanager-publish-f.md) |
| [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md) |
| [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md) |
| [removeSlot](arkts-notification-notificationmanager-removeslot-f.md) |
| [removeSlot](arkts-notification-notificationmanager-removeslot-f.md) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md) |
| [setBadgeNumber](arkts-notification-notificationmanager-setbadgenumber-f.md) |
| [setBadgeNumber](arkts-notification-notificationmanager-setbadgenumber-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md) |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md) |
| [cancel](arkts-notification-notificationmanager-cancel-f-sys.md) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md) |
| [getBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-getbadgedisplaystatusbybundles-f-sys.md) |
| [getBundlePriorityConfig](arkts-notification-notificationmanager-getbundlepriorityconfig-f-sys.md) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md) |
| [getDistributedDeviceList](arkts-notification-notificationmanager-getdistributeddevicelist-f-sys.md) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md) |
| [getNotificationStatisticsByBundle](arkts-notification-notificationmanager-getnotificationstatisticsbybundle-f-sys.md) |
| [getNotificationSwitch](arkts-notification-notificationmanager-getnotificationswitch-f-sys.md) |
| [getPriorityEnabledByBundles](arkts-notification-notificationmanager-getpriorityenabledbybundles-f-sys.md) |
| [getPriorityStrategyByBundles](arkts-notification-notificationmanager-getprioritystrategybybundles-f-sys.md) |
| [getReminderInfoByBundles](arkts-notification-notificationmanager-getreminderinfobybundles-f-sys.md) |
| [getRingtoneInfoByBundle](arkts-notification-notificationmanager-getringtoneinfobybundle-f-sys.md) |
| [getSlotByBundle](arkts-notification-notificationmanager-getslotbybundle-f-sys.md) |
| [getSlotByBundle](arkts-notification-notificationmanager-getslotbybundle-f-sys.md) |
| [getSlotFlagsByBundle](arkts-notification-notificationmanager-getslotflagsbybundle-f-sys.md) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f-sys.md) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md) |
| [isDistributedEnabledBySlot](arkts-notification-notificationmanager-isdistributedenabledbyslot-f-sys.md) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md) |
| [isNotificationSlotEnabledByBundles](arkts-notification-notificationmanager-isnotificationslotenabledbybundles-f-sys.md) |
| [isPriorityEnabled](arkts-notification-notificationmanager-ispriorityenabled-f-sys.md) |
| [isPriorityEnabledByBundle](arkts-notification-notificationmanager-ispriorityenabledbybundle-f-sys.md) |
| [isPriorityIntelligentEnabled](arkts-notification-notificationmanager-ispriorityintelligentenabled-f-sys.md) |
| [isSilentReminderEnabled](arkts-notification-notificationmanager-issilentreminderenabled-f-sys.md) |
| [isSmartReminderEnabled](arkts-notification-notificationmanager-issmartreminderenabled-f-sys.md) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md) |
| [off](arkts-notification-notificationmanager-off-f-sys.md#offchecknotification) |
| [offBadgeNumberQuery](arkts-notification-notificationmanager-offbadgenumberquery-f-sys.md) |
| [offCheckNotification](arkts-notification-notificationmanager-offchecknotification-f-sys.md) |
| [on](arkts-notification-notificationmanager-on-f-sys.md#onchecknotification) |
| [on](arkts-notification-notificationmanager-on-f-sys.md#onchecknotification) |
| [onBadgeNumberQuery](arkts-notification-notificationmanager-onbadgenumberquery-f-sys.md) |
| [onCheckNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md) |
| [onCheckNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md) |
| [setAdditionalConfig](arkts-notification-notificationmanager-setadditionalconfig-f-sys.md) |
| [setBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-setbadgedisplaystatusbybundles-f-sys.md) |
| [setBadgeNumberByBundle](arkts-notification-notificationmanager-setbadgenumberbybundle-f-sys.md) |
| [setBundlePriorityConfig](arkts-notification-notificationmanager-setbundlepriorityconfig-f-sys.md) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md) |
| [setDistributedEnableByBundles](arkts-notification-notificationmanager-setdistributedenablebybundles-f-sys.md) |
| [setDistributedEnabled](arkts-notification-notificationmanager-setdistributedenabled-f-sys.md) |
| [setDistributedEnabledByBundle](arkts-notification-notificationmanager-setdistributedenabledbybundle-f-sys.md) |
| [setDistributedEnabledBySlot](arkts-notification-notificationmanager-setdistributedenabledbyslot-f-sys.md) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md) |
| [setGeofenceEnabled](arkts-notification-notificationmanager-setgeofenceenabled-f-sys.md) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md) |
| [setNotificationSwitch](arkts-notification-notificationmanager-setnotificationswitch-f-sys.md) |
| [setPriorityEnabled](arkts-notification-notificationmanager-setpriorityenabled-f-sys.md) |
| [setPriorityEnabledByBundle](arkts-notification-notificationmanager-setpriorityenabledbybundle-f-sys.md) |
| [setPriorityEnabledByBundles](arkts-notification-notificationmanager-setpriorityenabledbybundles-f-sys.md) |
| [setPriorityIntelligentEnabled](arkts-notification-notificationmanager-setpriorityintelligentenabled-f-sys.md) |
| [setPriorityStrategyByBundles](arkts-notification-notificationmanager-setprioritystrategybybundles-f-sys.md) |
| [setReminderInfoByBundles](arkts-notification-notificationmanager-setreminderinfobybundles-f-sys.md) |
| [setRingtoneInfoByBundle](arkts-notification-notificationmanager-setringtoneinfobybundle-f-sys.md) |
| [setSilentReminderEnabled](arkts-notification-notificationmanager-setsilentreminderenabled-f-sys.md) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md) |
| [setSlotFlagsByBundle](arkts-notification-notificationmanager-setslotflagsbybundle-f-sys.md) |
| [setSmartReminderEnabled](arkts-notification-notificationmanager-setsmartreminderenabled-f-sys.md) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md) |
| [setTargetDeviceStatus](arkts-notification-notificationmanager-settargetdevicestatus-f-sys.md) |
| [snoozeNotification](arkts-notification-notificationmanager-snoozenotification-f-sys.md) |
| [subscribeSystemLiveView](arkts-notification-notificationmanager-subscribesystemliveview-f-sys.md) |
| [triggerSystemLiveView](arkts-notification-notificationmanager-triggersystemliveview-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NotificationSetting](arkts-notification-notificationmanager-notificationsetting-i.md) |

<!--Del-->
### Interfaces(System API)

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
### Enums(System API)

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
### Types(System API)

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
| [NotificationFlags](arkts-notification-notificationmanager-notificationflags-t-sys.md) |
| [NotificationFlagStatus](arkts-notification-notificationmanager-notificationflagstatus-t-sys.md) |
| [NotificationIconButton](arkts-notification-notificationmanager-notificationiconbutton-t-sys.md) |
| [NotificationLiveViewContent](arkts-notification-notificationmanager-notificationliveviewcontent-t-sys.md) |
| [NotificationSorting](arkts-notification-notificationmanager-notificationsorting-t-sys.md) |
| [Trigger](arkts-notification-notificationmanager-trigger-t-sys.md) |
| [TriggerType](arkts-notification-notificationmanager-triggertype-t-sys.md) |
| [UnifiedGroupInfo](arkts-notification-notificationmanager-unifiedgroupinfo-t-sys.md) |
<!--DelEnd-->
