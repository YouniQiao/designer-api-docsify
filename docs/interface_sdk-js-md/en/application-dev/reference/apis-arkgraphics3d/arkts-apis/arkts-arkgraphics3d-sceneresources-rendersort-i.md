# RenderSort

Describes the order in which materials are rendered, controlling the sequence of drawing in the rendering pipeline.@interface RenderSort

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderSortLayer

```TypeScript
renderSortLayer?: int
```

Rendering layer ID. A smaller value indicates an earlier rendering order. The value range is [0, 63]. The default layer ID is 32.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 32

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderSortLayerOrder

```TypeScript
renderSortLayerOrder?: int
```

Rendering order of different objects within the same rendering layer. A smaller value indicates an earlier rendering order. The value range is [0, 255]. The default value is 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 0

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUi.Graphics3D
