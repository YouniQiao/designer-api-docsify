# @ohos.effectKit

图像效果模块提供了处理图像的基础能力，包括亮度调节、模糊化、灰度调节和智能取色等， 适用于图片编辑应用中添加滤镜效果、应用启动页背景图模糊处理、UI主题色自动提取、图片配色分析等场景。 本模块用于离线处理image.PixelMap以获得视觉效果， 而uiEffect（UI效果服务）则实时接入渲染服务，针对屏幕帧缓存进行处理以获得动态视觉效果。 该模块提供以下图像效果相关的常用功能： - [Filter](arkts-arkgraphics2d-effectkit-filter-i.md#filter)：效果类，用于将指定效果添加到效果链表中，通过链式调用实现多种图像效果的组合处理。 - [Color](arkts-arkgraphics2d-effectkit-color-i.md#color)：颜色类，用于保存取色的结果。 - [ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md#colorpicker)：智能取色器。

**起始版本：** 23

<!--Device-unnamed-declare namespace effectKit--><!--Device-unnamed-declare namespace effectKit-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md#createcolorpicker) |
| [createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md#createcolorpicker) |
| [createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md#createcolorpicker) |
| [createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md#createcolorpicker) |
| [createEffect](arkts-arkgraphics2d-effectkit-createeffect-f.md#createeffect) |

### 接口

| 名称 |
| --- |
| [Color](arkts-arkgraphics2d-effectkit-color-i.md) |
| [ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md) |
| [Filter](arkts-arkgraphics2d-effectkit-filter-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i-sys.md) |
| [Filter](arkts-arkgraphics2d-effectkit-filter-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [PictureComplexityDegree](arkts-arkgraphics2d-effectkit-picturecomplexitydegree-e-sys.md) |
| [PictureLightDegree](arkts-arkgraphics2d-effectkit-picturelightdegree-e-sys.md) |
| [PictureShadeDegree](arkts-arkgraphics2d-effectkit-pictureshadedegree-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [EllipticalMaskCenter](arkts-arkgraphics2d-effectkit-ellipticalmaskcenter-t-sys.md) |
| [EllipticalMaskRadius](arkts-arkgraphics2d-effectkit-ellipticalmaskradius-t-sys.md) |
<!--DelEnd-->
