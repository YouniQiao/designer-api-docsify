# CylinderGeometry

A cylinder geometry type that inherits from [GeometryDefinition](arkts-arkgraphics3d-scenetypes-geometrydefinition-c.md).

> **NOTE：**
> 
> You must ensure that all three parameters are set correctly.
> Invalid values may prevent cylinder creation or cause undefined behavior.

**Inheritance/Implementation:** CylinderGeometry extends [GeometryDefinition](arkts-arkgraphics3d-scenetypes-geometrydefinition-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class CylinderGeometry extends GeometryDefinition--><!--Device-unnamed-export declare class CylinderGeometry extends GeometryDefinition-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## height

```TypeScript
set height(value: double)
```

The height of the cylinder, the unit is the scene unit in the world coordinate system (e.g., cm, m, km).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CylinderGeometry-set height(value: double)--><!--Device-CylinderGeometry-set height(value: double)-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## radius

```TypeScript
set radius(value: double)
```

The radius of the base of the cylinder, the unit is the scene unit in the world coordinate system (e.g., cm, m, km).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CylinderGeometry-set radius(value: double)--><!--Device-CylinderGeometry-set radius(value: double)-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## segmentCount

```TypeScript
set segmentCount(value: int)
```

Use regular polygons to approximate the circular base of the cylinder,where segmentCount is the number of sides of the regular polygon used.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CylinderGeometry-set segmentCount(value: int)--><!--Device-CylinderGeometry-set segmentCount(value: int)-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

