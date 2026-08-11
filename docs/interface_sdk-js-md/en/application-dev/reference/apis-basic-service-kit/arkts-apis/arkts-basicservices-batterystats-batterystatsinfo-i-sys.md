# BatteryStatsInfo (System API)

Describes the device power consumption information.

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

The power consumption, in unit of mAh.

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

The power consumption type.

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

The uid related with the power consumption info.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-BatteryStatsInfo-uid: int--><!--Device-BatteryStatsInfo-uid: int-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

