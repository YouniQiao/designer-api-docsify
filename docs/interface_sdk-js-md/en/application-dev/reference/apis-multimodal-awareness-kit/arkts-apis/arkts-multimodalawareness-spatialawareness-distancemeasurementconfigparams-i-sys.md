# DistanceMeasurementConfigParams (System API)

Configuration parameters for the distance measurement interface @interface DistanceMeasurementConfigParams

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**System capability:** SystemCapability.MultimodalAwareness.DistanceMeasurement

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { spatialAwareness } from '@kit.MultimodalAwarenessKit';
```

## deviceList

```TypeScript
deviceList: string[]
```

distance measurement supported devices list

**Type:** string[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalAwareness.DistanceMeasurement

**System API:** This is a system API.

## reportFrequency

```TypeScript
reportFrequency: int
```

distance measurement result reporting frequency

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalAwareness.DistanceMeasurement

**System API:** This is a system API.

## reportMode

```TypeScript
reportMode: ReportingMode
```

distance measurement result reporting mode

**Type:** [ReportingMode](arkts-multimodalawareness-spatialawareness-reportingmode-e-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalAwareness.DistanceMeasurement

**System API:** This is a system API.

## techType

```TypeScript
techType: TechnologyType
```

distance measurement technology type

**Type:** [TechnologyType](arkts-multimodalawareness-spatialawareness-technologytype-e-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MultimodalAwareness.DistanceMeasurement

**System API:** This is a system API.
