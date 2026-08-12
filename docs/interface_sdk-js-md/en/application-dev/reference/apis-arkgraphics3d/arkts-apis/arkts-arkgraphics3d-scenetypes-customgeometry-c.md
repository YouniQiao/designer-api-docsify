# CustomGeometry

An array of vertices and their data defining a custom geometric shape.

**Inheritance/Implementation:** CustomGeometry extends [GeometryDefinition](arkts-arkgraphics3d-scenetypes-geometrydefinition-c.md#GeometryDefinition)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class CustomGeometry extends GeometryDefinition--><!--Device-unnamed-export declare class CustomGeometry extends GeometryDefinition-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## colors

```TypeScript
colors?: Color[]
```

Vertex color. If colors is not null, colors[N] is for vertices[N].

**Type:** [Color](arkts-arkgraphics3d-scenetypes-color-i.md)[]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CustomGeometry-colors?: Color[]--><!--Device-CustomGeometry-colors?: Color[]-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## indices

```TypeScript
indices?: int[]
```

Indices of those vertices that form triangles. PrimitiveTopology is applied to the sequence defined by indices.

An example of creating an identical pair of triangles, given vertices = [a, b, c, d]: topology = PrimitiveTopology.TRIANGLE_LIST  indices = [0, 1, 2, 2, 1, 3] resulting triangles: abc, cbd

 topology = PrimitiveTopology.TRIANGLE_STRIP  indices = [0, 1, 2, 3] resulting triangles: abc, cbd (b and c are reversed in cbd, to match the face direction of the first triangle)

**Type:** int[]

**Default:** indices: [0, 1 ,2,..., vertices.size() - 1]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CustomGeometry-indices?: int[]--><!--Device-CustomGeometry-indices?: int[]-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## normals

```TypeScript
normals?: Vec3[]
```

Vertex normal. If normals is not null. normals[N] is for vertices[N] and generateNormals is ignored.

**Type:** [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md)[]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CustomGeometry-normals?: Vec3[]--><!--Device-CustomGeometry-normals?: Vec3[]-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## topology

```TypeScript
topology?: PrimitiveTopology
```

How to form mesh triangles from the indexed vertices.

**Type:** [PrimitiveTopology](arkts-arkgraphics3d-scenetypes-primitivetopology-e.md)

**Default:** PrimitiveTopology.TRIANGLE_LIST

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CustomGeometry-topology?: PrimitiveTopology--><!--Device-CustomGeometry-topology?: PrimitiveTopology-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## uvs

```TypeScript
uvs?: Vec2[]
```

Vertex texture mapping UV coordinate. If uvs is not null, uvs[N] is for vertices[N]

**Type:** [Vec2](arkts-arkgraphics3d-scenetypes-vec2-i.md)[]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CustomGeometry-uvs?: Vec2[]--><!--Device-CustomGeometry-uvs?: Vec2[]-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## vertices

```TypeScript
set vertices(value: Vec3[])
```

An array of vertices.

**Type:** [Vec3](arkts-arkgraphics3d-scenetypes-vec3-i.md)[]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-CustomGeometry-set vertices(value: Vec3[])--><!--Device-CustomGeometry-set vertices(value: Vec3[])-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

