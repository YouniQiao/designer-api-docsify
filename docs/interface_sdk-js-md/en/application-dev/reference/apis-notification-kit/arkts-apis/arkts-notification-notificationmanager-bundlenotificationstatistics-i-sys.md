# BundleNotificationStatistics (System API)

描述指定应用通知统计信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-notificationManager-export interface BundleNotificationStatistics--><!--Device-notificationManager-export interface BundleNotificationStatistics-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## bundle

```TypeScript
bundle: BundleOption
```

指定应用的包信息。

**Type:** [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-BundleNotificationStatistics-bundle: BundleOption--><!--Device-BundleNotificationStatistics-bundle: BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## lastTime

```TypeScript
lastTime: number
```

应用最后一次发布通知的时间。数据格式：时间戳。单位：ms。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-BundleNotificationStatistics-lastTime: number--><!--Device-BundleNotificationStatistics-lastTime: number-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## recentCount

```TypeScript
recentCount: number
```

应用最近7天发布的通知总量。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-BundleNotificationStatistics-recentCount: number--><!--Device-BundleNotificationStatistics-recentCount: number-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

