# BundleNotificationStatistics (System API)

Describes the notification statistics of a specified application.

**Since:** 26.0.0

<!--Device-notificationManager-export interface BundleNotificationStatistics--><!--Device-notificationManager-export interface BundleNotificationStatistics-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## bundle

```TypeScript
bundle: BundleOption
```

Bundle information of the application.

**Type:** BundleOption

**Since:** 26.0.0

<!--Device-BundleNotificationStatistics-bundle: BundleOption--><!--Device-BundleNotificationStatistics-bundle: BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## lastTime

```TypeScript
lastTime: number
```

Time when the app last published a notification.<br>Data format: timestamp.<br>Unit: millisecond.

**Type:** number

**Since:** 26.0.0

<!--Device-BundleNotificationStatistics-lastTime: long--><!--Device-BundleNotificationStatistics-lastTime: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## recentCount

```TypeScript
recentCount: number
```

Total number of notifications published by the application in the last seven days.

**Type:** number

**Since:** 26.0.0

<!--Device-BundleNotificationStatistics-recentCount: int--><!--Device-BundleNotificationStatistics-recentCount: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.
