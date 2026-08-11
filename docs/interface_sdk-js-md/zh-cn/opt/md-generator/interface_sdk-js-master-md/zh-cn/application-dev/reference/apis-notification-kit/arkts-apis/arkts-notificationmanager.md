# @ohos.notificationManager

本模块提供通知管理的能力，应用可使用本模块完成通知的完整生命周期管理。其中涉及通知的发布、更新与取消，通知渠道的创建与查询、通知能力授权状态的查询与申请、应用角标的设置、通知中心存量通知的查询等操作。

**API组合使用关系说明**：

本模块的接口围绕通知的"授权→发布→取消→渠道管理"的完整流程展开，各接口间存在明确的组合使用关系：

1. **授权查询与申请流程**：发布通知前，先通过isNotificationEnabled查询通知能力的授权状态。如果通知能力未授权，通过requestEnableNotification引导用户开启通知权限。

2. **通知发布与更新流程**：通过publish发布通知，通知内容通过NotificationRequest指定。如果新发布通知与已有通知的ID和标签相同，将自动更新已有通知。如果新发布通知与已有通知的ID或标签不相同，将创建新的通知。

3. **通知取消流程**：通过cancel取消指定ID的通知，通过cancelAll取消本应用所有通知，通过cancelGroup取消指定分组下的通知。

4. **通知渠道管理流程**：通过addSlot创建通知渠道，通过getSlot/getSlots查询通知渠道配置，通过removeSlot/removeAllSlots删除通知渠道。建议在发布通知前先创建对应类型的通知渠道。除了可以使用addSlot创建通知渠道，还可以在发布通知的NotificationRequest中携带notificationSlotType字段，如果对应类型的渠道不存在，会自动创建。

5. **角标管理流程**：通过setBadgeNumber设置角标数字，或者通过publish接口发布通知时，在NotificationRequest的badgeNumber字段里携带需要增加的角标数量。

6. **存量通知查询流程**：通过getActiveNotificationCount获取通知中心本应用存量通知数量，通过getActiveNotifications获取通知中心本应用存量通知详情。

**起始版本：** 9

<!--Device-unnamed-declare namespace notificationManager--><!--Device-unnamed-declare namespace notificationManager-End-->

**系统能力：** SystemCapability.Notification.Notification

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addSlot](arkts-notification-notificationmanager-addslot-f.md#addslot-2) |
| [addSlot](arkts-notification-notificationmanager-addslot-f.md#addslot-3) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md#cancel) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md#cancel-1) |
| [cancel](arkts-notification-notificationmanager-cancel-f.md#cancel-2) |
| [cancelAll](arkts-notification-notificationmanager-cancelall-f.md#cancelall) |
| [cancelAll](arkts-notification-notificationmanager-cancelall-f.md#cancelall-1) |
| [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md#cancelgroup) |
| [cancelGroup](arkts-notification-notificationmanager-cancelgroup-f.md#cancelgroup-1) |
| [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md#getactivenotificationcount) |
| [getActiveNotificationCount](arkts-notification-notificationmanager-getactivenotificationcount-f.md#getactivenotificationcount-1) |
| [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md#getactivenotifications) |
| [getActiveNotifications](arkts-notification-notificationmanager-getactivenotifications-f.md#getactivenotifications-1) |
| [getBadgeNumber](arkts-notification-notificationmanager-getbadgenumber-f.md#getbadgenumber) |
| [getNotificationParameters](arkts-notification-notificationmanager-getnotificationparameters-f.md#getnotificationparameters) |
| [getNotificationSetting](arkts-notification-notificationmanager-getnotificationsetting-f.md#getnotificationsetting) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getslot) |
| [getSlot](arkts-notification-notificationmanager-getslot-f.md#getslot-1) |
| [getSlots](arkts-notification-notificationmanager-getslots-f.md#getslots) |
| [getSlots](arkts-notification-notificationmanager-getslots-f.md#getslots-1) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md#isdistributedenabled) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f.md#isdistributedenabled-1) |
| [isGeofenceEnabled](arkts-notification-notificationmanager-isgeofenceenabled-f.md#isgeofenceenabled) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md#isnotificationenabled-2) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md#isnotificationenabled-3) |
| [isNotificationEnabledSync](arkts-notification-notificationmanager-isnotificationenabledsync-f.md#isnotificationenabledsync) |
| [isSupportTemplate](arkts-notification-notificationmanager-issupporttemplate-f.md#issupporttemplate) |
| [isSupportTemplate](arkts-notification-notificationmanager-issupporttemplate-f.md#issupporttemplate-1) |
| [openNotificationSettings](arkts-notification-notificationmanager-opennotificationsettings-f.md#opennotificationsettings) |
| [openNotificationSettingsWithResult](arkts-notification-notificationmanager-opennotificationsettingswithresult-f.md#opennotificationsettingswithresult) |
| [publish](arkts-notification-notificationmanager-publish-f.md#publish) |
| [publish](arkts-notification-notificationmanager-publish-f.md#publish-1) |
| [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md#removeallslots) |
| [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md#removeallslots-1) |
| [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeslot) |
| [removeSlot](arkts-notification-notificationmanager-removeslot-f.md#removeslot-1) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestenablenotification) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestenablenotification-1) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestenablenotification-2) |
| [requestEnableNotification](arkts-notification-notificationmanager-requestenablenotification-f.md#requestenablenotification-3) |
| [setBadgeNumber](arkts-notification-notificationmanager-setbadgenumber-f.md#setbadgenumber) |
| [setBadgeNumber](arkts-notification-notificationmanager-setbadgenumber-f.md#setbadgenumber-1) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md#adddonotdisturbprofile) |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md#adddonotdisturbprofile-1) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md#addslot) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md#addslot-1) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md#addslots) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md#addslots-1) |
| [cancel](arkts-notification-notificationmanager-cancel-f-sys.md#cancel-3) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelasbundle) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelasbundle-1) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelasbundle-2) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md#disablenotificationfeature) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md#disablenotificationfeature-1) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displaybadge) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displaybadge-1) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getactivenotificationbyfilter) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getactivenotificationbyfilter-1) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md#getallactivenotifications) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md#getallactivenotifications-1) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md#getallnotificationenabledbundles) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md#getallnotificationenabledbundles-1) |
| [getBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-getbadgedisplaystatusbybundles-f-sys.md#getbadgedisplaystatusbybundles) |
| [getBundlePriorityConfig](arkts-notification-notificationmanager-getbundlepriorityconfig-f-sys.md#getbundlepriorityconfig) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md#getdeviceremindtype) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md#getdeviceremindtype-1) |
| [getDistributedDeviceList](arkts-notification-notificationmanager-getdistributeddevicelist-f-sys.md#getdistributeddevicelist) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-1) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-2) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getdonotdisturbdate-3) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md#getdonotdisturbprofile) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md#getdonotdisturbprofile-1) |
| [getNotificationStatisticsByBundle](arkts-notification-notificationmanager-getnotificationstatisticsbybundle-f-sys.md#getnotificationstatisticsbybundle) |
| [getNotificationSwitch](arkts-notification-notificationmanager-getnotificationswitch-f-sys.md#getnotificationswitch) |
| [getPriorityEnabledByBundles](arkts-notification-notificationmanager-getpriorityenabledbybundles-f-sys.md#getpriorityenabledbybundles) |
| [getPriorityStrategyByBundles](arkts-notification-notificationmanager-getprioritystrategybybundles-f-sys.md#getprioritystrategybybundles) |
| [getReminderInfoByBundles](arkts-notification-notificationmanager-getreminderinfobybundles-f-sys.md#getreminderinfobybundles) |
| [getRingtoneInfoByBundle](arkts-notification-notificationmanager-getringtoneinfobybundle-f-sys.md#getringtoneinfobybundle) |
| [getSlotByBundle](arkts-notification-notificationmanager-getslotbybundle-f-sys.md#getslotbybundle) |
| [getSlotFlagsByBundle](arkts-notification-notificationmanager-getslotflagsbybundle-f-sys.md#getslotflagsbybundle) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md#getslotnumbybundle) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md#getslotnumbybundle-1) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md#getslotsbybundle) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md#getslotsbybundle-1) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md#getsyncnotificationenabledwithoutapp) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md#getsyncnotificationenabledwithoutapp-1) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isbadgedisplayed) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isbadgedisplayed-1) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f-sys.md#isdistributedenabled-2) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isdistributedenabledbybundle) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isdistributedenabledbybundle-1) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isdistributedenabledbybundle-2) |
| [isDistributedEnabledBySlot](arkts-notification-notificationmanager-isdistributedenabledbyslot-f-sys.md#isdistributedenabledbyslot) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled-1) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled-4) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isnotificationenabled-5) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md#isnotificationslotenabled) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md#isnotificationslotenabled-1) |
| [isNotificationSlotEnabledByBundles](arkts-notification-notificationmanager-isnotificationslotenabledbybundles-f-sys.md#isnotificationslotenabledbybundles) |
| [isPriorityEnabled](arkts-notification-notificationmanager-ispriorityenabled-f-sys.md#ispriorityenabled) |
| [isPriorityEnabledByBundle](arkts-notification-notificationmanager-ispriorityenabledbybundle-f-sys.md#ispriorityenabledbybundle) |
| [isPriorityIntelligentEnabled](arkts-notification-notificationmanager-ispriorityintelligentenabled-f-sys.md#ispriorityintelligentenabled) |
| [isSilentReminderEnabled](arkts-notification-notificationmanager-issilentreminderenabled-f-sys.md#issilentreminderenabled) |
| [isSmartReminderEnabled](arkts-notification-notificationmanager-issmartreminderenabled-f-sys.md#issmartreminderenabled) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md#issupportdonotdisturbmode) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md#issupportdonotdisturbmode-1) |
| [off](arkts-notification-notificationmanager-off-f-sys.md#off) |
| [offBadgeNumberQuery](arkts-notification-notificationmanager-offbadgenumberquery-f-sys.md#offbadgenumberquery) |
| [on](arkts-notification-notificationmanager-on-f-sys.md#on) |
| [on](arkts-notification-notificationmanager-on-f-sys.md#on-1) |
| [onBadgeNumberQuery](arkts-notification-notificationmanager-onbadgenumberquery-f-sys.md#onbadgenumberquery) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md#publish-2) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md#publish-3) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishasbundle) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishasbundle-1) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishasbundle-2) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md#removedonotdisturbprofile) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md#removedonotdisturbprofile-1) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md#removegroupbybundle) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md#removegroupbybundle-1) |
| [setAdditionalConfig](arkts-notification-notificationmanager-setadditionalconfig-f-sys.md#setadditionalconfig) |
| [setBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-setbadgedisplaystatusbybundles-f-sys.md#setbadgedisplaystatusbybundles) |
| [setBadgeNumberByBundle](arkts-notification-notificationmanager-setbadgenumberbybundle-f-sys.md#setbadgenumberbybundle) |
| [setBundlePriorityConfig](arkts-notification-notificationmanager-setbundlepriorityconfig-f-sys.md#setbundlepriorityconfig) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setdistributedenable) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setdistributedenable-1) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setdistributedenablebybundle) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setdistributedenablebybundle-1) |
| [setDistributedEnableByBundles](arkts-notification-notificationmanager-setdistributedenablebybundles-f-sys.md#setdistributedenablebybundles) |
| [setDistributedEnabled](arkts-notification-notificationmanager-setdistributedenabled-f-sys.md#setdistributedenabled) |
| [setDistributedEnabledByBundle](arkts-notification-notificationmanager-setdistributedenabledbybundle-f-sys.md#setdistributedenabledbybundle) |
| [setDistributedEnabledBySlot](arkts-notification-notificationmanager-setdistributedenabledbyslot-f-sys.md#setdistributedenabledbyslot) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setdonotdisturbdate) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-1) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-2) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setdonotdisturbdate-3) |
| [setGeofenceEnabled](arkts-notification-notificationmanager-setgeofenceenabled-f-sys.md#setgeofenceenabled) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md#setnotificationenable) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md#setnotificationenable-1) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setnotificationenableslot) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setnotificationenableslot-1) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setnotificationenableslot-2) |
| [setNotificationSwitch](arkts-notification-notificationmanager-setnotificationswitch-f-sys.md#setnotificationswitch) |
| [setPriorityEnabled](arkts-notification-notificationmanager-setpriorityenabled-f-sys.md#setpriorityenabled) |
| [setPriorityEnabledByBundle](arkts-notification-notificationmanager-setpriorityenabledbybundle-f-sys.md#setpriorityenabledbybundle) |
| [setPriorityEnabledByBundles](arkts-notification-notificationmanager-setpriorityenabledbybundles-f-sys.md#setpriorityenabledbybundles) |
| [setPriorityIntelligentEnabled](arkts-notification-notificationmanager-setpriorityintelligentenabled-f-sys.md#setpriorityintelligentenabled) |
| [setPriorityStrategyByBundles](arkts-notification-notificationmanager-setprioritystrategybybundles-f-sys.md#setprioritystrategybybundles) |
| [setReminderInfoByBundles](arkts-notification-notificationmanager-setreminderinfobybundles-f-sys.md#setreminderinfobybundles) |
| [setRingtoneInfoByBundle](arkts-notification-notificationmanager-setringtoneinfobybundle-f-sys.md#setringtoneinfobybundle) |
| [setSilentReminderEnabled](arkts-notification-notificationmanager-setsilentreminderenabled-f-sys.md#setsilentreminderenabled) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md#setslotbybundle) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md#setslotbybundle-1) |
| [setSlotFlagsByBundle](arkts-notification-notificationmanager-setslotflagsbybundle-f-sys.md#setslotflagsbybundle) |
| [setSmartReminderEnabled](arkts-notification-notificationmanager-setsmartreminderenabled-f-sys.md#setsmartreminderenabled) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md#setsyncnotificationenabledwithoutapp) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md#setsyncnotificationenabledwithoutapp-1) |
| [setTargetDeviceStatus](arkts-notification-notificationmanager-settargetdevicestatus-f-sys.md#settargetdevicestatus) |
| [snoozeNotification](arkts-notification-notificationmanager-snoozenotification-f-sys.md#snoozenotification) |
| [subscribeSystemLiveView](arkts-notification-notificationmanager-subscribesystemliveview-f-sys.md#subscribesystemliveview) |
| [triggerSystemLiveView](arkts-notification-notificationmanager-triggersystemliveview-f-sys.md#triggersystemliveview) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [NotificationSetting](arkts-notification-notificationmanager-notificationsetting-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
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

### 枚举

| 名称 |
| --- |
| [ContentType](arkts-notification-notificationmanager-contenttype-e.md) |
| [PriorityNotificationType](arkts-notification-notificationmanager-prioritynotificationtype-e.md) |
| [SlotLevel](arkts-notification-notificationmanager-slotlevel-e.md) |
| [SlotType](arkts-notification-notificationmanager-slottype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
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

### 类型

| 名称 |
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
### 类型（系统接口）

| 名称 |
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
