# @ohos.notificationExtensionSubscription

本模块提供管理通知扩展的能力，具体包括：打开通知扩展订阅设置界面、订阅和取消订阅通知扩展、获取和设置通知授权状态。

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Notification.Notification

## 导入模块

```TypeScript
import { notificationExtensionSubscription } from '@kit.NotificationKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getSubscribeInfo](arkts-notification-notificationextensionsubscription-getsubscribeinfo-f.md) |
| [getUserGrantedEnabledBundles](arkts-notification-notificationextensionsubscription-getusergrantedenabledbundles-f.md) |
| [isUserGranted](arkts-notification-notificationextensionsubscription-isusergranted-f.md) |
| [openSubscriptionSettings](arkts-notification-notificationextensionsubscription-opensubscriptionsettings-f.md) |
| [openSubscriptionSettingsWithResult](arkts-notification-notificationextensionsubscription-opensubscriptionsettingswithresult-f.md) |
| [subscribe](arkts-notification-notificationextensionsubscription-subscribe-f.md) |
| [unsubscribe](arkts-notification-notificationextensionsubscription-unsubscribe-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getAllSubscriptionBundles](arkts-notification-notificationextensionsubscription-getallsubscriptionbundles-f-sys.md) |
| [getUserGrantedEnabledBundles](arkts-notification-notificationextensionsubscription-getusergrantedenabledbundles-f-sys.md) |
| [getUserGrantedState](arkts-notification-notificationextensionsubscription-getusergrantedstate-f-sys.md) |
| [setUserGrantedBundleState](arkts-notification-notificationextensionsubscription-setusergrantedbundlestate-f-sys.md) |
| [setUserGrantedState](arkts-notification-notificationextensionsubscription-setusergrantedstate-f-sys.md) |
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
