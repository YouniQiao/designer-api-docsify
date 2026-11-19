# BlenderBase（系统接口）

```TypeScript
class BlenderBase
```

混合器基础类型，提供各类混合效果的统一创建入口。推荐统一使用本类型的方法创建混合器。

**起始版本：** 26.1.0

<!--Device-uiEffect-class BlenderBase--><!--Device-uiEffect-class BlenderBase-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## createBrightnessBlender

```TypeScript
static createBrightnessBlender(param: BrightnessBlenderParam, hdrEnabled?: boolean): BlenderBase
```

输入提亮混合器参数创建提亮混合的BlenderBase实例。可选参数hdrEnabled为false时效果与调用uiEffect.createBrightnessBlender()相同，为true时效果与调用uiEffect.createHdrBrightnessBlender()相同。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-BlenderBase-static createBrightnessBlender(param: BrightnessBlenderParam, hdrEnabled?: boolean): BlenderBase--><!--Device-BlenderBase-static createBrightnessBlender(param: BrightnessBlenderParam, hdrEnabled?: boolean): BlenderBase-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [BrightnessBlenderParam](arkts-arkgraphics2d-graphics-uieffect-brightnessblenderparam-i-sys.md) | 是 | 提亮混合器参数，包含灰度调整系数、饱和度和混合比例等配置项，用于配置提亮混合效果。 |
| hdrEnabled | boolean | 否 | 是否为提亮混合效果开启HDR。设置为true时，提亮混合效果开启HDR；设置为false时，提亮混合效果不开启HDR。默认值为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BlenderBase](arkts-arkgraphics2d-uieffect-blenderbase-c-sys.md) | 返回带有提亮混合效果的BlenderBase实例。 |

## createColorfulBrightnessBlender

```TypeScript
static createColorfulBrightnessBlender(brightnessBlenderParam: BrightnessBlenderParam,
      options?: ColorfulBrightnessBlenderOptions): BlenderBase
```

创建BlenderBase实例，用于给组件添加基于保持色相的提亮压暗效果。效果与调用uiEffect.createColorfulBrightnessBlender()相同。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-BlenderBase-static createColorfulBrightnessBlender(brightnessBlenderParam: BrightnessBlenderParam,      options?: ColorfulBrightnessBlenderOptions): BlenderBase--><!--Device-BlenderBase-static createColorfulBrightnessBlender(brightnessBlenderParam: BrightnessBlenderParam,      options?: ColorfulBrightnessBlenderOptions): BlenderBase-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightnessBlenderParam | [BrightnessBlenderParam](arkts-arkgraphics2d-graphics-uieffect-brightnessblenderparam-i-sys.md) | 是 | 提亮压暗的常规参数，用于配置亮度映射、饱和度曲线等基础属性。 |
| options | [ColorfulBrightnessBlenderOptions](arkts-arkgraphics2d-uieffect-colorfulbrightnessblenderoptions-i-sys.md) | 否 | 提亮压暗的增强参数，用于控制提亮压暗方向、色彩增强强度、可读性阈值及HDR开关。此参数不填时，使用ColorfulBrightnessBlenderOptions各字段的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BlenderBase](arkts-arkgraphics2d-uieffect-blenderbase-c-sys.md) | 返回带有基于保持色相的提亮压暗混合效果的BlenderBase实例。 |

## createHdrDarkenBlender

```TypeScript
static createHdrDarkenBlender(hdrBrightnessRatio: number, grayscaleFactor?: [number, number, number]): BlenderBase
```

创建HDR压暗混合的BlenderBase实例，用于HDR图层的压暗混合效果。效果与调用uiEffect.createHdrDarkenBlender()相同。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BlenderBase-static createHdrDarkenBlender(hdrBrightnessRatio: double, grayscaleFactor?: [double, double, double]): BlenderBase--><!--Device-BlenderBase-static createHdrDarkenBlender(hdrBrightnessRatio: double, grayscaleFactor?: [double, double, double]): BlenderBase-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hdrBrightnessRatio | number | 是 | HDR的提亮倍数。取值范围为[1.0, 设备当前支持最大提亮倍数]，超出边界时会自动截断。当取值等于1.0时，为组件原本亮度。设备当前支持最大提亮倍数 = 设备最大亮度 / 设备默认亮度。设备最大亮度通过hdc命令获取：hdc shell param get const.display.brightness.max设备默认亮度通过hdc命令获取：hdc shell param get const.display.brightness.default |
| grayscaleFactor | [number, number, number] | 否 | 将RGB颜色转换为灰度值。灰度转换公式的权重可随当前色域自动调整，不同色域下使用不同的权重计算方式；适用于sRGB等标准色域场景。当需要根据特定色域或视觉效果自定义灰度转换权重时传入此参数。三个分量均无边界限制。默认值为标准灰度权重[0.299, 0.587, 0.114]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BlenderBase](arkts-arkgraphics2d-uieffect-blenderbase-c-sys.md) | 返回带有HDR压暗混合效果的BlenderBase实例，用于将压暗效果添加到指定的组件上。 |
