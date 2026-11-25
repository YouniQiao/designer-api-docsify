# ShadowOptions（系统接口）

```TypeScript
interface ShadowOptions
```

阴影的配置参数。

> **说明：** 
> 
> 超出图像范围的阴影会被截断。

**起始版本：** 26.1.0

<!--Device-effectKit-interface ShadowOptions--><!--Device-effectKit-interface ShadowOptions-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { effectKit } from '@kit.ArkGraphics2D';
```

## color

```TypeScript
color?: common2D.Color
```

可选参数，阴影颜色，默认值为黑色{red:0, green:0, blue:0, alpha:26}。可通过Alpha通道设置阴影透明度。

**类型：** [common2D.Color](arkts-arkgraphics2d-common2d-color-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ShadowOptions-color?: common2D.Color--><!--Device-ShadowOptions-color?: common2D.Color-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## lightDirection

```TypeScript
lightDirection?: common2D.Point
```

可选参数，光照方向向量，默认值为(0, 0)，取值范围为(-∞, +∞)。X轴向右为正，Y轴向下为正。光照方向向量表示阴影偏移的方向。当向量为(0, 0)时，shadowDistance取任何值，阴影均不发生偏移。

**类型：** [common2D.Point](arkts-arkgraphics2d-common2d-point-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ShadowOptions-lightDirection?: common2D.Point--><!--Device-ShadowOptions-lightDirection?: common2D.Point-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## radius

```TypeScript
radius?: number
```

可选参数，阴影模糊半径，单位为px，取值范围为[0, +∞)，默认值为0，超出取值范围时按边界值截断。值为0时无阴影效果，值越大阴影边缘越柔和。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ShadowOptions-radius?: double--><!--Device-ShadowOptions-radius?: double-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

## shadowDistance

```TypeScript
shadowDistance?: number
```

可选参数，阴影偏移距离，单位为px，取值范围为[0, +∞)，默认值为0，超出取值范围时按边界值截断。该参数决定阴影偏移距离，与lightDirection共同确定阴影覆盖区域，当值为0时，lightDirection为任意方向时，阴影均不发生偏移。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ShadowOptions-shadowDistance?: double--><!--Device-ShadowOptions-shadowDistance?: double-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。
