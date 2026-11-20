# HalftoneParam (System API)

```TypeScript
interface HalftoneParam
```

Halftone configuration parameters.

**Since:** 26.1.0

<!--Device-effectKit-interface HalftoneParam--><!--Device-effectKit-interface HalftoneParam-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { effectKit } from '@kit.ArkGraphics2D';
```

## angle

```TypeScript
angle?: number
```

Optional. Rotation angle of the grid coordinates, with counterclockwise as the positive direction. Unit: rad (radians). Used to adjust the dot arrangement direction. Value range: (-∞, +∞). Default value: 0. When the value is 0, the grid does not rotate, and the dot arrangement direction is horizontal to the right.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HalftoneParam-angle?: double--><!--Device-HalftoneParam-angle?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## colorWidthRatio

```TypeScript
colorWidthRatio?: number
```

Optional. Colored ring width coefficient. Value range: [0, 1]. Default value: 0.5. Values outside the value range are clamped to the boundary value. The set width is colorWidthRatio * gridSize / 2. The black inner circle radius is the actual outer circle radius minus this width, and when the result is less than 0, it is treated as 0. When the value is 0, there is no colored ring. When the set width is greater than or equal to the outer circle radius, the effect is equivalent to the entire area within the outer circle radius being colored.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HalftoneParam-colorWidthRatio?: double--><!--Device-HalftoneParam-colorWidthRatio?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## gridSize

```TypeScript
gridSize: number
```

Grid cell side length, i.e., the center distance between adjacent dots, in px. Value range: [3, +∞). Values outside the value range are clamped to the boundary value. A larger value produces larger overall dot size and sparser arrangement.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HalftoneParam-gridSize: double--><!--Device-HalftoneParam-gridSize: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## lumCoeff

```TypeScript
lumCoeff?: number
```

Optional. Influence coefficient of brightness on the outer circle radius. Value range: [0, +∞). Default value: 0. Values outside the value range are clamped to the boundary value. The actual outer circle radius is clamp(1 - lum * lumCoeff, 0, maxRadiusRatio) * gridSize / 2, where lum is the brightness of the sampled color at the grid center. This value is obtained from sampling and does not need to be set. When other parameters remain unchanged, a larger lumCoeff produces a stronger shrinking effect of brightness on the outer circle radius.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HalftoneParam-lumCoeff?: double--><!--Device-HalftoneParam-lumCoeff?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## maxRadiusRatio

```TypeScript
maxRadiusRatio?: number
```

Optional. Ratio of the outer circle diameter upper limit to the grid side length. Value range: [0, 1]. Default value: 1. Values outside the value range are clamped to the boundary value. The outer circle diameter is truncated by maxRadiusRatio * gridSize. When the value is 1, the maximum allowed outer circle diameter equals the grid side length.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HalftoneParam-maxRadiusRatio?: double--><!--Device-HalftoneParam-maxRadiusRatio?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## saturation

```TypeScript
saturation?: number
```

Optional. Saturation interpolation coefficient of the colored area, used to interpolate between the grayscale color corresponding to the sampled color and the sampled color. Value range: [0, 1]. Default value: 1. Values outside the value range are clamped to the boundary value. When the value is 0, the grayscale color is used. When the value is 1, the sampled color is preserved.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HalftoneParam-saturation?: double--><!--Device-HalftoneParam-saturation?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## smoothness

```TypeScript
smoothness?: number
```

Optional. Ratio of the edge transition band half-width to gridSize. Value range: [0, +∞). Default value: 0. Values outside the value range are clamped to the boundary value. With the inner circle and outer circle boundaries as centers, it extends smoothness * gridSize to both sides respectively, forming a transition band with a total width of 2 * smoothness * gridSize. The inner circle edge is processed first, then the outer circle edge. When the value is 0, there is no transition band and the edge has no smooth transition. A larger value produces a wider transition band and softer edges.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HalftoneParam-smoothness?: double--><!--Device-HalftoneParam-smoothness?: double-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.
