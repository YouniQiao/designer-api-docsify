# BatteryStatsInfo (System API)

Describes the device power consumption information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { batteryStats } from '@kit.BasicServicesKit';
```

## power

```TypeScript
power: double
```

The power consumption, in unit of mAh.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

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

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.
