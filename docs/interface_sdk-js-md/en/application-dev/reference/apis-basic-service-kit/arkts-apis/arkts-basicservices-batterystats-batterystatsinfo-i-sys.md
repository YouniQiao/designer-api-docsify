# BatteryStatsInfo (System API)

设备的耗电信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-batteryStats-interface BatteryStatsInfo--><!--Device-batteryStats-interface BatteryStatsInfo-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { batteryStats } from 'kits/@kit.BasicServicesKit';
```

## power

```TypeScript
power: double
```

耗电的值，单位毫安时。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-BatteryStatsInfo-power: double--><!--Device-BatteryStatsInfo-power: double-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

## type

```TypeScript
type: ConsumptionType
```

耗电信息相关的类型。

**Type:** [ConsumptionType](arkts-basicservices-batterystats-consumptiontype-e-sys.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-BatteryStatsInfo-type: ConsumptionType--><!--Device-BatteryStatsInfo-type: ConsumptionType-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

## uid

```TypeScript
uid: int
```

耗电信息相关的UID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-BatteryStatsInfo-uid: int--><!--Device-BatteryStatsInfo-uid: int-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

