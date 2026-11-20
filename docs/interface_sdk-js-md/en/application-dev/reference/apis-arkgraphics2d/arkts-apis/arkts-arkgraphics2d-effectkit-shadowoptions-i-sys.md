# ShadowOptions (System API)

```TypeScript
interface ShadowOptions
```

Shadow configuration parameters.

> **NOTE:** 
> 
> Shadows beyond the image range are truncated.

**Since:** 26.1.0

<!--Device-effectKit-interface ShadowOptions--><!--Device-effectKit-interface ShadowOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { effectKit } from '@kit.ArkGraphics2D';
```

## color

```TypeScript
color?: common2D.Color
```

Optional. Shadow color. Default value: black {red:0, green:0, blue:0, alpha:26}. The shadow opacity can be set through the Alpha channel.

**Type:** [common2D.Color](arkts-arkgraphics2d-common2d-color-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-color?: common2D.Color--><!--Device-ShadowOptions-color?: common2D.Color-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## lightDirection

```TypeScript
lightDirection?: common2D.Point
```

Optional. Light direction vector. Default value: (0, 0). Value range: (-∞, +∞). The positive X-axis direction is to the right, and the positive Y-axis direction is downward. The light direction vector indicates the direction of shadow offset. When the vector is (0, 0), the shadow does not shift for any shadowDistance value.

**Type:** [common2D.Point](arkts-arkgraphics2d-common2d-point-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-lightDirection?: common2D.Point--><!--Device-ShadowOptions-lightDirection?: common2D.Point-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## radius

```TypeScript
radius?: number
```

Optional. Shadow blur radius, in px. Value range: [0, +∞). Default value: 0. Values outside the value range are clamped to the boundary value. When the value is 0, no shadow effect is applied. A larger value produces a softer shadow edge.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-radius?: double--><!--Device-ShadowOptions-radius?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## shadowDistance

```TypeScript
shadowDistance?: number
```

Optional. Shadow offset distance, in px. Value range: [0, +∞). Default value: 0. Values outside the value range are clamped to the boundary value. This parameter determines the shadow offset distance, and together with lightDirection, determines the shadow coverage area. When the value is 0, the shadow does not shift for any lightDirection value.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShadowOptions-shadowDistance?: double--><!--Device-ShadowOptions-shadowDistance?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.
