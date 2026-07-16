# RenderConfiguration

Global render configuration control

**Since:** 23

<!--Device-unnamed-export interface RenderConfiguration--><!--Device-unnamed-export interface RenderConfiguration-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## shadowResolution

```TypeScript
shadowResolution?: Vec2
```

resolution for single shadow map buffer, undefined by default,which means we use (1024, 1024) as the resolution of a single shadow map.You need to provide the same x and y value to get the right shadow effect, the unit is pixel.

**Type:** Vec2

**Default:** { 1024, 1024 }

**Since:** 23

<!--Device-RenderConfiguration-shadowResolution?: Vec2--><!--Device-RenderConfiguration-shadowResolution?: Vec2-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## softShadowConfig

```TypeScript
softShadowConfig?: SoftShadowConfig
```

param config for soft shadow, control the algorithm type and its configuration

**Type:** SoftShadowConfig

**Default:** { undefined }, means that use the default hard shadow algorithm

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderConfiguration-softShadowConfig?: SoftShadowConfig--><!--Device-RenderConfiguration-softShadowConfig?: SoftShadowConfig-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

