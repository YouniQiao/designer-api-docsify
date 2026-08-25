# CylinderGeometry

A cylinder geometry type that inherits from GeometryDefinition.

> **NOTE：**&gt;
> You must ensure that all three parameters are set correctly.
> Invalid values may prevent cylinder creation or cause undefined behavior.
@extends GeometryDefinition

**Inheritance/Implementation:** CylinderGeometry extends [GeometryDefinition](arkts-arkgraphics3d-scenetypes-geometrydefinition-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## height

```TypeScript
set height(value: double)
```

Height of the cylinder, in scene units of the world coordinate system (such as cm, m, km, etc.). The value range is greater than 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## radius

```TypeScript
set radius(value: double)
```

Bottom radius of the cylinder, in scene units of the world coordinate system (such as cm, m, km, etc.). The value range is greater than 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## segmentCount

```TypeScript
set segmentCount(value: int)
```

Use regular polygons to approximate the circular base of the cylinder, where segmentCount is the number of sides of the regular polygon used.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D
