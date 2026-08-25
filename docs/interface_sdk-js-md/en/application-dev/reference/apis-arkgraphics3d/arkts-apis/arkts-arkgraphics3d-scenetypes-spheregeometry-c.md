# SphereGeometry

A sphere geometry type that inherits from GeometryDefinition.@extends GeometryDefinition

**Inheritance/Implementation:** SphereGeometry extends [GeometryDefinition](arkts-arkgraphics3d-scenetypes-geometrydefinition-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## radius

```TypeScript
set radius(value: double)
```

Radius of the sphere, measured in the world coordinate system's units (for example, cm, m, or km). The value must be greater than 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## segmentCount

```TypeScript
set segmentCount(value: int)
```

Number of segments divided by longitude and latitude on the sphere. The value range is a positive integer greater than or equal to 3.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D
