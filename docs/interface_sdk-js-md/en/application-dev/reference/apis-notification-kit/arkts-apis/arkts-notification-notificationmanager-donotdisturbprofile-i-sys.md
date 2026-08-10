# DoNotDisturbProfile (System API)

勿扰模式的配置信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-notificationManager-export interface DoNotDisturbProfile--><!--Device-notificationManager-export interface DoNotDisturbProfile-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## id

```TypeScript
id: long
```

勿扰模式编号。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DoNotDisturbProfile-id: long--><!--Device-DoNotDisturbProfile-id: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## name

```TypeScript
name: string
```

勿扰模式名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DoNotDisturbProfile-name: string--><!--Device-DoNotDisturbProfile-name: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## trustlist

```TypeScript
trustlist?: Array<BundleOption>
```

勿扰模式的信任列表。

**Type:** Array&lt;BundleOption&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-DoNotDisturbProfile-trustlist?: Array<BundleOption>--><!--Device-DoNotDisturbProfile-trustlist?: Array<BundleOption>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

