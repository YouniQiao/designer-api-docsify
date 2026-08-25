# uiEffect

本模块提供组件效果的一些基础能力，包括模糊、提亮等。效果被分为Filter和VisualEffect大类，同类效果可以级联在一个效果大类的实例下。 使用该模块可以快速实现复杂的视觉效果，无需开发者掌握底层的图像处理算法，降低了开发复杂度，提升了用户体验。 在实际开发中，模糊可用于背景虚化，提亮可用于亮屏显示等。  
- [Filter](arkts-arkgraphics2d-uieffect-filter-i.md)：用于添加指定Filter效果到组件上。  
- [VisualEffect](arkts-arkgraphics2d-uieffect-visualeffect-i-sys.md)：用于添加指定VisualEffect效果到组件上。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createFilter](arkts-arkgraphics2d-uieffect-createfilter-f.md) |
| [createEffect](arkts-arkgraphics2d-uieffect-createeffect-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createBrightnessBlender](arkts-arkgraphics2d-uieffect-createbrightnessblender-f-sys.md) |
| [createHdrBrightnessBlender](arkts-arkgraphics2d-uieffect-createhdrbrightnessblender-f-sys.md) |
| [createHdrDarkenBlender](arkts-arkgraphics2d-uieffect-createhdrdarkenblender-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类（系统接口）

| 名称 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [Filter](arkts-arkgraphics2d-uieffect-filter-i.md) |
| [HdrBrightnessBlender](arkts-arkgraphics2d-uieffect-hdrbrightnessblender-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [Filter](arkts-arkgraphics2d-uieffect-filter-i-sys.md) |
| [VisualEffect](arkts-arkgraphics2d-uieffect-visualeffect-i-sys.md) |
| [BrightnessParam](arkts-arkgraphics2d-uieffect-brightnessparam-i-sys.md) |
| [HeatDistortionEffectParam](arkts-arkgraphics2d-uieffect-heatdistortioneffectparam-i-sys.md) |
| [BlurBubblesRiseEffectParam](arkts-arkgraphics2d-uieffect-blurbubblesriseeffectparam-i-sys.md) |
| [LiquidMaterialEffectParam](arkts-arkgraphics2d-uieffect-liquidmaterialeffectparam-i-sys.md) |
| [BrightnessBlender](arkts-arkgraphics2d-uieffect-brightnessblender-i-sys.md) |
| [HdrDarkenBlender](arkts-arkgraphics2d-uieffect-hdrdarkenblender-i-sys.md) |
| [Color](arkts-arkgraphics2d-uieffect-color-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [TileMode](arkts-arkgraphics2d-uieffect-tilemode-e-sys.md) |
| [WaterRippleMode](arkts-arkgraphics2d-uieffect-waterripplemode-e-sys.md) |
| [FlyMode](arkts-arkgraphics2d-uieffect-flymode-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [Blender](arkts-arkgraphics2d-uieffect-blender-t-sys.md) |
<!--DelEnd-->
