# SpeedParams (System API)

Parameters for moving or turning at a speed.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-mechanicManager-export interface SpeedParams--><!--Device-mechanicManager-export interface SpeedParams-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## angle

```TypeScript
angle: double
```

Turning angle, unit degree.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-SpeedParams-angle: double--><!--Device-SpeedParams-angle: double-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## mode

```TypeScript
mode?: MarchingMode
```

Movement mode.

**Type:** [MarchingMode](arkts-mechanic-mechanicmanager-marchingmode-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-SpeedParams-mode?: MarchingMode--><!--Device-SpeedParams-mode?: MarchingMode-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## speed

```TypeScript
speed: int
```

Turning or moving speed, unit cm.The value should be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-SpeedParams-speed: int--><!--Device-SpeedParams-speed: int-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

