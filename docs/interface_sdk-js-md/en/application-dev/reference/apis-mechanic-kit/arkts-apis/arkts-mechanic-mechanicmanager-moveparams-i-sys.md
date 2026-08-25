# MoveParams (System API)

Parameters for moving the target.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## angle

```TypeScript
angle: double
```

Turning angle, unit degree.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## distance

```TypeScript
distance: int
```

Moving distance, unit cm. The value should be an integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

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

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

## speedGear

```TypeScript
speedGear?: SpeedGear
```

Speed gear.

**Type:** [SpeedGear](arkts-mechanic-mechanicmanager-speedgear-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.
