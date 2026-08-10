# Mesh

网格节点拥有的网格实例

**Inheritance/Implementation:** Mesh extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Mesh extends SceneResource--><!--Device-unnamed-export interface Mesh extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## aabb

```TypeScript
readonly aabb: Aabb
```

网格的轴对齐包围盒.

**Type:** [Aabb](arkts-arkgraphics3d-scenetypes-aabb-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Mesh-readonly aabb: Aabb--><!--Device-Mesh-readonly aabb: Aabb-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## materialOverride

```TypeScript
materialOverride?: Material
```

覆盖子网格材质的材质.

**Type:** [Material](arkts-arkgraphics3d-sceneresources-material-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Mesh-materialOverride?: Material--><!--Device-Mesh-materialOverride?: Material-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## subMeshes

```TypeScript
readonly subMeshes: SubMesh[]
```

网格的子网格.

**Type:** [SubMesh](arkts-arkgraphics3d-sceneresources-submesh-i.md)[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Mesh-readonly subMeshes: SubMesh[]--><!--Device-Mesh-readonly subMeshes: SubMesh[]-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

