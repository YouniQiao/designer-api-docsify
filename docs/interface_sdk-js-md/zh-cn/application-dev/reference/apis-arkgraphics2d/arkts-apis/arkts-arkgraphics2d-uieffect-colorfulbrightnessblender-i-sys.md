# ColorfulBrightnessBlender（系统接口）

彩色提亮压暗混合器，用于将提亮效果添加到指定的组件上。在调用ColorfulBrightnessBlender前，需要先通过createColorfulBrightnessBlender创建一个ColorfulBrightnessBlender实例。

**起始版本：** 26.1.0

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## brightnessBlenderParam

```TypeScript
brightnessBlenderParam: BrightnessBlenderParam
```

实现彩色提亮压暗效果的常规参数，具体可参考BrightnessBlenderParam。

**类型：** [BrightnessBlenderParam](arkts-arkgraphics2d-graphics-uieffect-brightnessblenderparam-i-sys.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

## options

```TypeScript
options?: ColorfulBrightnessBlenderOptions
```

实现彩色提亮压暗效果的增强参数，具体可参考ColorfulBrightnessBlenderOptions。

**类型：** [ColorfulBrightnessBlenderOptions](arkts-arkgraphics2d-uieffect-colorfulbrightnessblenderoptions-i-sys.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。
