# Material

Material resource.

**Inheritance/Implementation:** Material extends [SceneResource](sceneresources-sceneresource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Material extends SceneResource--><!--Device-unnamed-export interface Material extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## alphaCutoff

```TypeScript
alphaCutoff?: double
```

Alpha cutoff value [0,1]. Enabled if < 1.

**Type:** double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Material-alphaCutoff?: double--><!--Device-Material-alphaCutoff?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## blend

```TypeScript
blend?: Blend
```

Control whether the blend is enabled

**Type:** Blend

**Default:** undefined, which means that blending is disabled.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Material-blend?: Blend--><!--Device-Material-blend?: Blend-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## cullMode

```TypeScript
cullMode?: CullMode
```

Culling mode.

**Type:** CullMode

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Material-cullMode?: CullMode--><!--Device-Material-cullMode?: CullMode-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## materialType

```TypeScript
readonly materialType: MaterialType
```

Material resource type.

**Type:** MaterialType

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Material-readonly materialType: MaterialType--><!--Device-Material-readonly materialType: MaterialType-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## polygonMode

```TypeScript
polygonMode?: PolygonMode
```

Polygon Mode of the material

**Type:** PolygonMode

**Default:** PolygonMode.FILL

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-Material-polygonMode?: PolygonMode--><!--Device-Material-polygonMode?: PolygonMode-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## renderSort

```TypeScript
renderSort?: RenderSort
```

Render sorting priority for layers.

**Type:** RenderSort

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Material-renderSort?: RenderSort--><!--Device-Material-renderSort?: RenderSort-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## shadowReceiver

```TypeScript
shadowReceiver?: boolean
```

Defines if the material can receive shadows.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Material-shadowReceiver?: boolean--><!--Device-Material-shadowReceiver?: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

