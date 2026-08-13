# @ohos.notificationManager

本模块提供通知管理的能力，应用可使用本模块完成通知的完整生命周期管理。其中涉及通知的发布、更新与取消，通知渠道的创建与查询、通知能力授权状态的查询与申请、应用角标的设置、通知中心存量通知的查询等操作。 **API组合使用关系说明**： 本模块的接口围绕通知的"授权→发布→取消→渠道管理"的完整流程展开，各接口间存在明确的组合使用关系： 1. **授权查询与申请流程**：发布通知前，先通过isNotificationEnabled查询通知能力的授权状态。如果通知能力未授权，通过requestEnableNotification引导用户开启通知权限。 2. **通知发布与更新流程**：通过publish发布通知，通知内容通过NotificationRequest指定。如果新发布通知与已有通知的ID和标签相同，将自动更新已有通知。如果新发布通知与已有通知的ID或标签不相同，将创建新的通知。 3. **通知取消流程**：通过cancel取消指定ID的通知，通过cancelAll取消本应用所有通知，通过cancelGroup取消指定分组下的通知。 4. **通知渠道管理流程**：通过addSlot创建通知渠道，通过getSlot/getSlots查询通知渠道配置， 通过removeSlot/removeAllSlots删除通知渠道。建议在发布通知前先创建对应类型的通知渠道。 除了可以使用addSlot创建通知渠道，还可以在发布通知的NotificationRequest中携带notificationSlotType字段， 如果对应类型的渠道不存在，会自动创建。 5. **角标管理流程**：通过setBadgeNumber设置角标数字，或者通过publish接口发布通知时，在NotificationRequest的badgeNumber字段里携带需要增加的角标数量。 6. **存量通知查询流程**：通过getActiveNotificationCount获取通知中心本应用存量通知数量，通过getActiveNotifications获取通知中心本应用存量通知详情。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace notificationManager--><!--Device-unnamed-declare namespace notificationManager-End-->

**系统能力：** SystemCapability.Notification.Notification

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md#addDoNotDisturbProfile（系统接口）) |
| [addDoNotDisturbProfile](arkts-notification-notificationmanager-adddonotdisturbprofile-f-sys.md#addDoNotDisturbProfile（系统接口）) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md#addSlot（系统接口）) |
| [addSlot](arkts-notification-notificationmanager-addslot-f-sys.md#addSlot（系统接口）) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md#addSlots（系统接口）) |
| [addSlots](arkts-notification-notificationmanager-addslots-f-sys.md#addSlots（系统接口）) |
| [cancel](arkts-notification-notificationmanager-cancel-f-sys.md#cancel（系统接口）) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelAsBundle（系统接口）) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelAsBundle（系统接口）) |
| [cancelAsBundle](arkts-notification-notificationmanager-cancelasbundle-f-sys.md#cancelAsBundle（系统接口）) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md#disableNotificationFeature（系统接口）) |
| [disableNotificationFeature](arkts-notification-notificationmanager-disablenotificationfeature-f-sys.md#disableNotificationFeature（系统接口）) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displayBadge（系统接口）) |
| [displayBadge](arkts-notification-notificationmanager-displaybadge-f-sys.md#displayBadge（系统接口）) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getActiveNotificationByFilter（系统接口）) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getActiveNotificationByFilter（系统接口）) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getActiveNotificationByFilter（系统接口）) |
| [getActiveNotificationByFilter](arkts-notification-notificationmanager-getactivenotificationbyfilter-f-sys.md#getActiveNotificationByFilter（系统接口）) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md#getAllActiveNotifications（系统接口）) |
| [getAllActiveNotifications](arkts-notification-notificationmanager-getallactivenotifications-f-sys.md#getAllActiveNotifications（系统接口）) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md#getAllNotificationEnabledBundles（系统接口）) |
| [getAllNotificationEnabledBundles](arkts-notification-notificationmanager-getallnotificationenabledbundles-f-sys.md#getAllNotificationEnabledBundles（系统接口）) |
| [getBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-getbadgedisplaystatusbybundles-f-sys.md#getBadgeDisplayStatusByBundles（系统接口）) |
| [getBundlePriorityConfig](arkts-notification-notificationmanager-getbundlepriorityconfig-f-sys.md#getBundlePriorityConfig（系统接口）) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md#getDeviceRemindType（系统接口）) |
| [getDeviceRemindType](arkts-notification-notificationmanager-getdeviceremindtype-f-sys.md#getDeviceRemindType（系统接口）) |
| [getDistributedDeviceList](arkts-notification-notificationmanager-getdistributeddevicelist-f-sys.md#getDistributedDeviceList（系统接口）) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getDoNotDisturbDate（系统接口）) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getDoNotDisturbDate（系统接口）) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getDoNotDisturbDate（系统接口）) |
| [getDoNotDisturbDate](arkts-notification-notificationmanager-getdonotdisturbdate-f-sys.md#getDoNotDisturbDate（系统接口）) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md#getDoNotDisturbProfile（系统接口）) |
| [getDoNotDisturbProfile](arkts-notification-notificationmanager-getdonotdisturbprofile-f-sys.md#getDoNotDisturbProfile（系统接口）) |
| [getNotificationStatisticsByBundle](arkts-notification-notificationmanager-getnotificationstatisticsbybundle-f-sys.md#getNotificationStatisticsByBundle（系统接口）) |
| [getNotificationSwitch](arkts-notification-notificationmanager-getnotificationswitch-f-sys.md#getNotificationSwitch（系统接口）) |
| [getPriorityEnabledByBundles](arkts-notification-notificationmanager-getpriorityenabledbybundles-f-sys.md#getPriorityEnabledByBundles（系统接口）) |
| [getPriorityStrategyByBundles](arkts-notification-notificationmanager-getprioritystrategybybundles-f-sys.md#getPriorityStrategyByBundles（系统接口）) |
| [getReminderInfoByBundles](arkts-notification-notificationmanager-getreminderinfobybundles-f-sys.md#getReminderInfoByBundles（系统接口）) |
| [getRingtoneInfoByBundle](arkts-notification-notificationmanager-getringtoneinfobybundle-f-sys.md#getRingtoneInfoByBundle（系统接口）) |
| [getSlotByBundle](arkts-notification-notificationmanager-getslotbybundle-f-sys.md#getSlotByBundle（系统接口）) |
| [getSlotByBundle](arkts-notification-notificationmanager-getslotbybundle-f-sys.md#getSlotByBundle（系统接口）) |
| [getSlotFlagsByBundle](arkts-notification-notificationmanager-getslotflagsbybundle-f-sys.md#getSlotFlagsByBundle（系统接口）) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md#getSlotNumByBundle（系统接口）) |
| [getSlotNumByBundle](arkts-notification-notificationmanager-getslotnumbybundle-f-sys.md#getSlotNumByBundle（系统接口）) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md#getSlotsByBundle（系统接口）) |
| [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md#getSlotsByBundle（系统接口）) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md#getSyncNotificationEnabledWithoutApp（系统接口）) |
| [getSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-getsyncnotificationenabledwithoutapp-f-sys.md#getSyncNotificationEnabledWithoutApp（系统接口）) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isBadgeDisplayed（系统接口）) |
| [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isBadgeDisplayed（系统接口）) |
| [isDistributedEnabled](arkts-notification-notificationmanager-isdistributedenabled-f-sys.md#isDistributedEnabled（系统接口）) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isDistributedEnabledByBundle（系统接口）) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isDistributedEnabledByBundle（系统接口）) |
| [isDistributedEnabledByBundle](arkts-notification-notificationmanager-isdistributedenabledbybundle-f-sys.md#isDistributedEnabledByBundle（系统接口）) |
| [isDistributedEnabledBySlot](arkts-notification-notificationmanager-isdistributedenabledbyslot-f-sys.md#isDistributedEnabledBySlot（系统接口）) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled（系统接口）) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled（系统接口）) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled（系统接口）) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled（系统接口）) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled（系统接口）) |
| [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f-sys.md#isNotificationEnabled（系统接口）) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md#isNotificationSlotEnabled（系统接口）) |
| [isNotificationSlotEnabled](arkts-notification-notificationmanager-isnotificationslotenabled-f-sys.md#isNotificationSlotEnabled（系统接口）) |
| [isNotificationSlotEnabledByBundles](arkts-notification-notificationmanager-isnotificationslotenabledbybundles-f-sys.md#isNotificationSlotEnabledByBundles（系统接口）) |
| [isPriorityEnabled](arkts-notification-notificationmanager-ispriorityenabled-f-sys.md#isPriorityEnabled（系统接口）) |
| [isPriorityEnabledByBundle](arkts-notification-notificationmanager-ispriorityenabledbybundle-f-sys.md#isPriorityEnabledByBundle（系统接口）) |
| [isPriorityIntelligentEnabled](arkts-notification-notificationmanager-ispriorityintelligentenabled-f-sys.md#isPriorityIntelligentEnabled（系统接口）) |
| [isSilentReminderEnabled](arkts-notification-notificationmanager-issilentreminderenabled-f-sys.md#isSilentReminderEnabled（系统接口）) |
| [isSmartReminderEnabled](arkts-notification-notificationmanager-issmartreminderenabled-f-sys.md#isSmartReminderEnabled（系统接口）) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md#isSupportDoNotDisturbMode（系统接口）) |
| [isSupportDoNotDisturbMode](arkts-notification-notificationmanager-issupportdonotdisturbmode-f-sys.md#isSupportDoNotDisturbMode（系统接口）) |
| [offBadgeNumberQuery](arkts-notification-notificationmanager-offbadgenumberquery-f-sys.md#offBadgeNumberQuery（系统接口）) |
| [offCheckNotification](arkts-notification-notificationmanager-offchecknotification-f-sys.md#offCheckNotification（系统接口）) |
| [off_checkNotification](arkts-notification-notificationmanager-offchecknotification-f-sys.md) |
| [onBadgeNumberQuery](arkts-notification-notificationmanager-onbadgenumberquery-f-sys.md#onBadgeNumberQuery（系统接口）) |
| [onCheckNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md#onCheckNotification（系统接口）) |
| [onCheckNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md#onCheckNotification（系统接口）) |
| [on_checkNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md) |
| [on_checkNotification](arkts-notification-notificationmanager-onchecknotification-f-sys.md) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md#publish（系统接口）) |
| [publish](arkts-notification-notificationmanager-publish-f-sys.md#publish（系统接口）) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishAsBundle（系统接口）) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishAsBundle（系统接口）) |
| [publishAsBundle](arkts-notification-notificationmanager-publishasbundle-f-sys.md#publishAsBundle（系统接口）) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md#removeDoNotDisturbProfile（系统接口）) |
| [removeDoNotDisturbProfile](arkts-notification-notificationmanager-removedonotdisturbprofile-f-sys.md#removeDoNotDisturbProfile（系统接口）) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md#removeGroupByBundle（系统接口）) |
| [removeGroupByBundle](arkts-notification-notificationmanager-removegroupbybundle-f-sys.md#removeGroupByBundle（系统接口）) |
| [setAdditionalConfig](arkts-notification-notificationmanager-setadditionalconfig-f-sys.md#setAdditionalConfig（系统接口）) |
| [setBadgeDisplayStatusByBundles](arkts-notification-notificationmanager-setbadgedisplaystatusbybundles-f-sys.md#setBadgeDisplayStatusByBundles（系统接口）) |
| [setBadgeNumberByBundle](arkts-notification-notificationmanager-setbadgenumberbybundle-f-sys.md#setBadgeNumberByBundle（系统接口）) |
| [setBundlePriorityConfig](arkts-notification-notificationmanager-setbundlepriorityconfig-f-sys.md#setBundlePriorityConfig（系统接口）) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setDistributedEnable（系统接口）) |
| [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setDistributedEnable（系统接口）) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setDistributedEnableByBundle（系统接口）) |
| [setDistributedEnableByBundle](arkts-notification-notificationmanager-setdistributedenablebybundle-f-sys.md#setDistributedEnableByBundle（系统接口）) |
| [setDistributedEnableByBundles](arkts-notification-notificationmanager-setdistributedenablebybundles-f-sys.md#setDistributedEnableByBundles（系统接口）) |
| [setDistributedEnabled](arkts-notification-notificationmanager-setdistributedenabled-f-sys.md#setDistributedEnabled（系统接口）) |
| [setDistributedEnabledByBundle](arkts-notification-notificationmanager-setdistributedenabledbybundle-f-sys.md#setDistributedEnabledByBundle（系统接口）) |
| [setDistributedEnabledBySlot](arkts-notification-notificationmanager-setdistributedenabledbyslot-f-sys.md#setDistributedEnabledBySlot（系统接口）) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setDoNotDisturbDate（系统接口）) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setDoNotDisturbDate（系统接口）) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setDoNotDisturbDate（系统接口）) |
| [setDoNotDisturbDate](arkts-notification-notificationmanager-setdonotdisturbdate-f-sys.md#setDoNotDisturbDate（系统接口）) |
| [setGeofenceEnabled](arkts-notification-notificationmanager-setgeofenceenabled-f-sys.md#setGeofenceEnabled（系统接口）) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md#setNotificationEnable（系统接口）) |
| [setNotificationEnable](arkts-notification-notificationmanager-setnotificationenable-f-sys.md#setNotificationEnable（系统接口）) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setNotificationEnableSlot（系统接口）) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setNotificationEnableSlot（系统接口）) |
| [setNotificationEnableSlot](arkts-notification-notificationmanager-setnotificationenableslot-f-sys.md#setNotificationEnableSlot（系统接口）) |
| [setNotificationSwitch](arkts-notification-notificationmanager-setnotificationswitch-f-sys.md#setNotificationSwitch（系统接口）) |
| [setPriorityEnabled](arkts-notification-notificationmanager-setpriorityenabled-f-sys.md#setPriorityEnabled（系统接口）) |
| [setPriorityEnabledByBundle](arkts-notification-notificationmanager-setpriorityenabledbybundle-f-sys.md#setPriorityEnabledByBundle（系统接口）) |
| [setPriorityEnabledByBundles](arkts-notification-notificationmanager-setpriorityenabledbybundles-f-sys.md#setPriorityEnabledByBundles（系统接口）) |
| [setPriorityIntelligentEnabled](arkts-notification-notificationmanager-setpriorityintelligentenabled-f-sys.md#setPriorityIntelligentEnabled（系统接口）) |
| [setPriorityStrategyByBundles](arkts-notification-notificationmanager-setprioritystrategybybundles-f-sys.md#setPriorityStrategyByBundles（系统接口）) |
| [setReminderInfoByBundles](arkts-notification-notificationmanager-setreminderinfobybundles-f-sys.md#setReminderInfoByBundles（系统接口）) |
| [setRingtoneInfoByBundle](arkts-notification-notificationmanager-setringtoneinfobybundle-f-sys.md#setRingtoneInfoByBundle（系统接口）) |
| [setSilentReminderEnabled](arkts-notification-notificationmanager-setsilentreminderenabled-f-sys.md#setSilentReminderEnabled（系统接口）) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md#setSlotByBundle（系统接口）) |
| [setSlotByBundle](arkts-notification-notificationmanager-setslotbybundle-f-sys.md#setSlotByBundle（系统接口）) |
| [setSlotFlagsByBundle](arkts-notification-notificationmanager-setslotflagsbybundle-f-sys.md#setSlotFlagsByBundle（系统接口）) |
| [setSmartReminderEnabled](arkts-notification-notificationmanager-setsmartreminderenabled-f-sys.md#setSmartReminderEnabled（系统接口）) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md#setSyncNotificationEnabledWithoutApp（系统接口）) |
| [setSyncNotificationEnabledWithoutApp](arkts-notification-notificationmanager-setsyncnotificationenabledwithoutapp-f-sys.md#setSyncNotificationEnabledWithoutApp（系统接口）) |
| [setTargetDeviceStatus](arkts-notification-notificationmanager-settargetdevicestatus-f-sys.md#setTargetDeviceStatus（系统接口）) |
| [snoozeNotification](arkts-notification-notificationmanager-snoozenotification-f-sys.md#snoozeNotification（系统接口）) |
| [subscribeSystemLiveView](arkts-notification-notificationmanager-subscribesystemliveview-f-sys.md#subscribeSystemLiveView（系统接口）) |
| [triggerSystemLiveView](arkts-notification-notificationmanager-triggersystemliveview-f-sys.md#triggerSystemLiveView（系统接口）) |
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
