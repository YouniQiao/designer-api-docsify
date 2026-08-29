# ColorfulBrightnessBlenderOptions（系统接口）

ColorfulBrightnessBlenderOptions的参数列表，用于配置彩色提亮压暗效果的各项属性，包括前景压暗权重、提亮压暗强度、亮度差阈值和hdr开关参数。

**起始版本：** 26.1.0

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## darkenWeight

```TypeScript
darkenWeight?: number
```

前景颜色压暗权重。为1的时候，颜色倾向比原始颜色暗；为0的时候，颜色倾向比原始颜色亮。取值范围为[0, 1]，超出边界会在实现时自动截断。

**类型：** number

**默认值：** 1

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

## hdrEnabled

```TypeScript
hdrEnabled?: boolean
```

是否主动开启hdr。关闭时也可能在前景或背景为hdr时被动触发hdr。

**类型：** boolean

**默认值：** true

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

## lumaDiff

```TypeScript
lumaDiff?: number
```

保证可读性的亮度差阈值。取值范围为[0, 1]，超出边界会在实现时自动截断。

**类型：** number

**默认值：** 0

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

## vibrancyStrength

```TypeScript
vibrancyStrength?: number
```

提亮压暗效果强度。取值范围为[0, 1]，超出边界会在实现时自动截断。

**类型：** number

**默认值：** 0

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**卡片能力：** 从API版本26.1.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。
