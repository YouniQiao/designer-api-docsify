# ColorPicker

取色类，用于从一张图像数据中获取它的主要颜色，适用于UI主题色提取、图片配色分析、智能配色推荐等场景， 可帮助开发者基于图片内容动态生成和谐的配色方案。在调用ColorPicker的方法前，需要先通过 [createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md)创建一个ColorPicker实例。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## discriminatePictureLightDegree

```TypeScript
discriminatePictureLightDegree(): PictureLightDegree
```

获取图片的明亮程度。当无法判别图片明亮程度时，返回UNKNOWN_LIGHT_COLOR_DEGREE_PICTURE。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [PictureLightDegree](arkts-arkgraphics2d-effectkit-picturelightdegree-e-sys.md) |

## getAlphaZeroTransparentProportion

```TypeScript
getAlphaZeroTransparentProportion(): number
```

获取图像中完全透明的像素占比。

**起始版本：** 23

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getComplexityDegree

```TypeScript
getComplexityDegree(): PictureComplexityDegree
```

获取图像内容复杂度。当无法判别图像内容复杂度时，返回默认值UNKNOWN_COMPLEXITY_DEGREE_PICTURE。

**起始版本：** 22

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [PictureComplexityDegree](arkts-arkgraphics2d-effectkit-picturecomplexitydegree-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getDeepenImmersionColor

```TypeScript
getDeepenImmersionColor(): Color
```

生成与背景色融合且比背景色更深的强沉浸感颜色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)里。该接口通过颜色混合算法，创建一种既与背景色协调又具有更强沉浸感的颜色效果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getImmersiveBackgroundColor

```TypeScript
getImmersiveBackgroundColor(): Color
```

生成能够创造沉浸式视觉效果的沉浸式背景色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)里。该接口基于主色生成适合作为沉浸式背景的颜色值。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getImmersiveForegroundColor

```TypeScript
getImmersiveForegroundColor(): Color
```

生成能够创造沉浸式视觉效果的沉浸式前景色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)里。该接口基于主色生成适合作为沉浸式前景的颜色值。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getMorandiShadowColor

```TypeScript
getMorandiShadowColor(): Color
```

从图像的主色中获取莫兰迪阴影色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)。该接口通过特定的颜色转换算法，将主色调转换为具有莫兰迪风格的阴影色调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getReverseColor

```TypeScript
getReverseColor(): Color
```

基于图像亮度判别结果生成反向颜色，并将结果写入[Color](arkts-arkgraphics2d-effectkit-color-i.md)里。根据 [discriminatePictureLightDegree](#discriminatepicturelightdegree)接口获取的图片明亮类型得到一个反色， 仅极亮色图片（EXTREMELY_LIGHT_COLOR_PICTURE）类型返回黑色，其他类型返回白色。用于界面主题或对比度计算。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) |

## getShadeDegree

```TypeScript
getShadeDegree(): PictureShadeDegree
```

获取图像颜色深浅度。当无法判别图像颜色深浅度时，返回默认值UNKNOWN_SHADE_DEGREE_PICTURE。

**起始版本：** 22

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [PictureShadeDegree](arkts-arkgraphics2d-effectkit-pictureshadedegree-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getTopProportionColorsAndPercentage

```TypeScript
getTopProportionColorsAndPercentage(colorCount: number): Map<Color | null, number | null>
```

同步返回图像占比靠前的颜色值及其对应比例，个数由`colorCount`指定。

**起始版本：** 22

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorCount | number | 是 |

**返回值：**

| 类型 |
| --- |
| Map & lt;Color \ | null, number \| null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
