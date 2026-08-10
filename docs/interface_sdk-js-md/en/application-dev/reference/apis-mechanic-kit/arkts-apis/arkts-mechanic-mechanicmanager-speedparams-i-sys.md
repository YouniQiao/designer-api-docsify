# SpeedParams (System API)

速度控制参数

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

转动角度。

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

行进方式。

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

转动或移动速度。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-SpeedParams-speed: int--><!--Device-SpeedParams-speed: int-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

