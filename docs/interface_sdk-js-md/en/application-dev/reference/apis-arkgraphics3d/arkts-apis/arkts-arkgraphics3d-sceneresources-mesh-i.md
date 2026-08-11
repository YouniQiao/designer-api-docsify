# Mesh

The mesh instance owned by the mesh node

**Inheritance/Implementation:** Mesh extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Mesh extends SceneResource--><!--Device-unnamed-export interface Mesh extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## aabb

```TypeScript
readonly aabb: Aabb
```

The axis aligned bounding box of the mesh.

**Type:** [Aabb](arkts-arkgraphics3d-scenetypes-aabb-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Mesh-readonly aabb: Aabb--><!--Device-Mesh-readonly aabb: Aabb-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## materialOverride

```TypeScript
materialOverride?: Material
```

The material override sub mesh's material.

**Type:** [Material](arkts-arkgraphics3d-sceneresources-material-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Mesh-materialOverride?: Material--><!--Device-Mesh-materialOverride?: Material-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## subMeshes

```TypeScript
readonly subMeshes: SubMesh[]
```

The sub meshes of the mesh.

**Type:** [SubMesh](arkts-arkgraphics3d-sceneresources-submesh-i.md)[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Mesh-readonly subMeshes: SubMesh[]--><!--Device-Mesh-readonly subMeshes: SubMesh[]-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

