# SphereGeometry

球体几何类型，继承自GeometryDefinition。@extends GeometryDefinition

**继承/实现关系：** SphereGeometry extends [GeometryDefinition](arkts-arkgraphics3d-scenetypes-geometrydefinition-c.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

## radius

```TypeScript
set radius(value: double)
```

球体半径，单位为世界坐标系下的场景单位（比如cm、m、km等），取值范围大于0。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D

## segmentCount

```TypeScript
set segmentCount(value: int)
```

在球体上以经纬度分割的段数，取值范围是大于等于3的正整数。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUi.Graphics3D
