# BundleNotificationStatistics (System API)

Describes the notification statistics of a specified application.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-notificationManager-export interface BundleNotificationStatistics--><!--Device-notificationManager-export interface BundleNotificationStatistics-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from 'notificationManager';
```

## bundle

```TypeScript
bundle: BundleOption
```

Bundle information of the application.

**Type:** BundleOption

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-BundleNotificationStatistics-bundle: BundleOption--><!--Device-BundleNotificationStatistics-bundle: BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## lastTime

```TypeScript
lastTime: long
```

Time when the app last published a notification.<br>Data format: timestamp.<br>Unit: millisecond.

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-BundleNotificationStatistics-lastTime: long--><!--Device-BundleNotificationStatistics-lastTime: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## recentCount

```TypeScript
recentCount: int
```

Total number of notifications published by the application in the last seven days.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-BundleNotificationStatistics-recentCount: int--><!--Device-BundleNotificationStatistics-recentCount: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

