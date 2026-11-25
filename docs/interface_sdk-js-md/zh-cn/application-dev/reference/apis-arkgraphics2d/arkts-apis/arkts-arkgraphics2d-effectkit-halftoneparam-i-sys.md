# HalftoneParam（系统接口）

```TypeScript
interface HalftoneParam
```

网点的配置参数。

**起始版本：** 26.1.0

<!--Device-effectKit-interface HalftoneParam--><!--Device-effectKit-interface HalftoneParam-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { effectKit } from '@kit.ArkGraphics2D';
```

## angle

```TypeScript
angle?: number
```

可选参数，网格坐标的旋转角度，以逆时针为正方向，单位为rad（弧度），用于调整网点排列方向。取值范围为(-∞, +∞)，默认值为0。值为0时网格不旋转，网点排列方向为水平向右。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HalftoneParam-angle?: double--><!--Device-HalftoneParam-angle?: double-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## colorWidthRatio

```TypeScript
colorWidthRatio?: number
```

可选参数，彩色圆环宽度系数，取值范围为[0, 1]，默认值为0.5，超出取值范围时按边界值截断。设定宽度为colorWidthRatio * gridSize / 2。黑色内圆半径为实际外圆半径减去该宽度，结果小于0时按0处理。值为0时无彩色圆环；设定宽度大于或等于外圆半径时，效果等同于外圆半径内全部为彩色区域。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HalftoneParam-colorWidthRatio?: double--><!--Device-HalftoneParam-colorWidthRatio?: double-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## gridSize

```TypeScript
gridSize: number
```

网格单元边长，即相邻网点的中心间距，单位为px。取值范围为[3, +∞)，超出取值范围时按边界值截断。值越大，网点整体尺寸越大，排列越稀疏。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HalftoneParam-gridSize: double--><!--Device-HalftoneParam-gridSize: double-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## lumCoeff

```TypeScript
lumCoeff?: number
```

可选参数，亮度对外圆半径的影响系数，取值范围为[0, +∞)，默认值为0，超出取值范围时按边界值截断。实际外圆半径为clamp(1 - lum * lumCoeff, 0, maxRadiusRatio) * gridSize / 2，其中lum为网格中心采样颜色的亮度，该值为采样所得，不需要设置。其他参数不变时，lumCoeff越大，亮度对外圆半径的缩小作用越强。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HalftoneParam-lumCoeff?: double--><!--Device-HalftoneParam-lumCoeff?: double-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## maxRadiusRatio

```TypeScript
maxRadiusRatio?: number
```

可选参数，外圆直径上限与网格边长的比值。取值范围为[0, 1]，默认值为1，超出取值范围时按边界值截断。外圆直径会被maxRadiusRatio * gridSize截断。值为1时，允许的外圆最大直径等于网格边长。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HalftoneParam-maxRadiusRatio?: double--><!--Device-HalftoneParam-maxRadiusRatio?: double-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## saturation

```TypeScript
saturation?: number
```

可选参数，彩色区域的饱和度插值系数，用于在采样颜色对应的灰度颜色与采样颜色之间进行插值。取值范围为[0, 1]，默认值为1，超出取值范围时按边界值截断。值为0时使用灰度颜色，值为1时保留采样颜色。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HalftoneParam-saturation?: double--><!--Device-HalftoneParam-saturation?: double-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## smoothness

```TypeScript
smoothness?: number
```

可选参数，边缘过渡带半宽与gridSize的比值，取值范围为[0, +∞)，默认值为0，超出取值范围时按边界值截断。分别以内圆和外圆的边界为中心，向两侧各延伸smoothness * gridSize，形成总宽度为2 * smoothness * gridSize的过渡带，先处理内圆边缘，再处理外圆边缘。值为0时无过渡带，边缘无平滑过渡，值越大，过渡带越宽，边缘越柔和。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-HalftoneParam-smoothness?: double--><!--Device-HalftoneParam-smoothness?: double-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。
