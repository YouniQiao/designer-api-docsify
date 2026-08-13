# @ohos.notificationExtensionSubscription

本模块提供管理通知扩展的能力，具体包括：打开通知扩展订阅设置界面、订阅和取消订阅通知扩展、获取和设置通知授权状态。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace notificationExtensionSubscription--><!--Device-unnamed-declare namespace notificationExtensionSubscription-End-->

**系统能力：** SystemCapability.Notification.Notification

## 导入模块

```TypeScript
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getSubscribeInfo](arkts-notification-notificationextensionsubscription-getsubscribeinfo-f.md#getSubscribeInfo) |
| [getUserGrantedEnabledBundles](arkts-notification-notificationextensionsubscription-getusergrantedenabledbundles-f.md#getUserGrantedEnabledBundles) |
| [isUserGranted](arkts-notification-notificationextensionsubscription-isusergranted-f.md#isUserGranted) |
| [openSubscriptionSettings](arkts-notification-notificationextensionsubscription-opensubscriptionsettings-f.md#openSubscriptionSettings) |
| [openSubscriptionSettingsWithResult](arkts-notification-notificationextensionsubscription-opensubscriptionsettingswithresult-f.md#openSubscriptionSettingsWithResult) |
| [subscribe](arkts-notification-notificationextensionsubscription-subscribe-f.md#subscribe) |
| [unsubscribe](arkts-notification-notificationextensionsubscription-unsubscribe-f.md#unsubscribe) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getAllSubscriptionBundles](arkts-notification-notificationextensionsubscription-getallsubscriptionbundles-f-sys.md#getAllSubscriptionBundles（系统接口）) |
| [getUserGrantedEnabledBundles](arkts-notification-notificationextensionsubscription-getusergrantedenabledbundles-f-sys.md#getUserGrantedEnabledBundles（系统接口）) |
| [getUserGrantedState](arkts-notification-notificationextensionsubscription-getusergrantedstate-f-sys.md#getUserGrantedState（系统接口）) |
| [setUserGrantedBundleState](arkts-notification-notificationextensionsubscription-setusergrantedbundlestate-f-sys.md#setUserGrantedBundleState（系统接口）) |
| [setUserGrantedState](arkts-notification-notificationextensionsubscription-setusergrantedstate-f-sys.md#setUserGrantedState（系统接口）) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [SubscribeType](arkts-notification-notificationextensionsubscription-subscribetype-e.md) |

### 类型

| 名称 |
| --- |
| [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) |
| [GrantedBundleInfo](arkts-notification-notificationextensionsubscription-grantedbundleinfo-t.md) |
| [NotificationExtensionSubscriptionInfo](arkts-notification-notificationextensionsubscription-notificationextensionsubscriptioninfo-t.md) |
| [NotificationInfo](arkts-notification-notificationextensionsubscription-notificationinfo-t.md) |
| [UserGrantSetting](arkts-notification-notificationextensionsubscription-usergrantsetting-t.md) |
