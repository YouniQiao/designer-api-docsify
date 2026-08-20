# RenderSort

Describes the order in which materials are rendered, controlling the sequence of drawing in the rendering pipeline.

@interface RenderSort

**Since:** 23

<!--Device-unnamed-export interface RenderSort--><!--Device-unnamed-export interface RenderSort-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderSortLayer

```TypeScript
renderSortLayer?: int
```

Rendering layer ID. A smaller value indicates an earlier rendering order. The value range is [0, 63]. The default layer ID is 32.

**Type:** int

**Default:** 32

**Since:** 23

<!--Device-RenderSort-renderSortLayer?: int--><!--Device-RenderSort-renderSortLayer?: int-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderSortLayerOrder

```TypeScript
renderSortLayerOrder?: int
```

Rendering order of different objects within the same rendering layer. A smaller value indicates an earlier rendering order. The value range is [0, 255]. The default value is 0.

**Type:** int

**Default:** 0

**Since:** 23

<!--Device-RenderSort-renderSortLayerOrder?: int--><!--Device-RenderSort-renderSortLayerOrder?: int-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

