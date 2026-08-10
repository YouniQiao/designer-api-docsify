# RaycastResult

射线检测命中结果.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RaycastResult--><!--Device-unnamed-export interface RaycastResult-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## centerDistance

```TypeScript
centerDistance: double
```

到轴对齐包围盒中心的距离, 单位为世界坐标系下的场景单位（例如cm、m、km等）.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RaycastResult-centerDistance: double--><!--Device-RaycastResult-centerDistance: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## hitPosition

```TypeScript
hitPosition: Position3
```

命中点的世界坐标位置, 单位为世界坐标系下的场景单位（例如cm、m、km等）.

**Type:** [Position3](arkts-arkgraphics3d-position3-t.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RaycastResult-hitPosition: Position3--><!--Device-RaycastResult-hitPosition: Position3-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## node

```TypeScript
node: Node
```

被击中的节点.

**Type:** [Node](arkts-arkgraphics3d-scenenodes-node-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RaycastResult-node: Node--><!--Device-RaycastResult-node: Node-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

