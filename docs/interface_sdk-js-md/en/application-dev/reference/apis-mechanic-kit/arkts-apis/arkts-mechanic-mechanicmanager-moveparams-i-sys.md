# MoveParams (System API)

设备移动参数

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-mechanicManager-export interface MoveParams--><!--Device-mechanicManager-export interface MoveParams-End-->

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

<!--Device-MoveParams-angle: double--><!--Device-MoveParams-angle: double-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## distance

```TypeScript
distance: int
```

移动距离。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-MoveParams-distance: int--><!--Device-MoveParams-distance: int-End-->

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

<!--Device-MoveParams-mode?: MarchingMode--><!--Device-MoveParams-mode?: MarchingMode-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## speedGear

```TypeScript
speedGear?: SpeedGear
```

速度档位。

**Type:** [SpeedGear](arkts-mechanic-mechanicmanager-speedgear-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-MoveParams-speedGear?: SpeedGear--><!--Device-MoveParams-speedGear?: SpeedGear-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

