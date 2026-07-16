# SphereGeometry

Define a sphere.

**Inheritance/Implementation:** SphereGeometry extends [GeometryDefinition](arkts-arkgraphics3d-geometrydefinition-c.md)

**Since:** 18

<!--Device-unnamed-export declare class SphereGeometry extends GeometryDefinition--><!--Device-unnamed-export declare class SphereGeometry extends GeometryDefinition-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## radius

```TypeScript
set radius(value: number)
```

The radius of the sphere, the unit is the scene unit in the world coordinate system (e.g., cm, m, km).

**Type:** number

**Since:** 18

<!--Device-SphereGeometry-set radius(value: double)--><!--Device-SphereGeometry-set radius(value: double)-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## segmentCount

```TypeScript
set segmentCount(value: number)
```

Divide the sphere latitudinally into this many circles and each circle longitudinally into this many segments.

**Type:** number

**Since:** 18

<!--Device-SphereGeometry-set segmentCount(value: int)--><!--Device-SphereGeometry-set segmentCount(value: int)-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

