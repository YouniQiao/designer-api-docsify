# DistributedBundleEnableInfo (System API)

描述多设备协同的包信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-notificationManager-export interface DistributedBundleEnableInfo--><!--Device-notificationManager-export interface DistributedBundleEnableInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## bundleName

```TypeScript
bundleName: string
```

包名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DistributedBundleEnableInfo-bundleName: string--><!--Device-DistributedBundleEnableInfo-bundleName: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## enable

```TypeScript
enable?: boolean
```

是否支持跨设备协同，返回true表示支持，返回false表示不支持，默认为false。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DistributedBundleEnableInfo-enable?: boolean--><!--Device-DistributedBundleEnableInfo-enable?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## uid

```TypeScript
uid: int
```

应用的UID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-DistributedBundleEnableInfo-uid: int--><!--Device-DistributedBundleEnableInfo-uid: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

