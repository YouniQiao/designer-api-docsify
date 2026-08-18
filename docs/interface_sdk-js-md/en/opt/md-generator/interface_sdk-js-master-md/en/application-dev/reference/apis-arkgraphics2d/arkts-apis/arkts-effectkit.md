# @ohos.effectKit

The Image Effect module provides basic capabilities for processing images, including brightness adjustment, blurring, grayscale adjustment, and intelligent color picking. It is applicable to scenarios such as adding filter effects in image editing apps, blurring the background image of app startup pages, automatically extracting UI theme colors, and analyzing image color schemes. This module is used for offline processing of image.PixelMap to obtain visual effects, while uiEffect (UI Effect Service) connects to the rendering service in real time to process screen frame buffers for dynamic visual effects. This module provides the following classes: - [Filter](arkts-arkgraphics2d-effectkit-filter-i.md#filter): an effect class used to add a specified effect to the effect chain, enabling combined processing of multiple image effects through chained calls. - [Color](arkts-arkgraphics2d-effectkit-color-i.md#color): a class used to store the color picked. - [ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md#colorpicker): a smart color picker.

**Since:** 23

<!--Device-unnamed-declare namespace effectKit--><!--Device-unnamed-declare namespace effectKit-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md#createcolorpicker) |
| [createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md#createcolorpicker) |
| [createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md#createcolorpicker) |
| [createColorPicker](arkts-arkgraphics2d-effectkit-createcolorpicker-f.md#createcolorpicker) |
| [createEffect](arkts-arkgraphics2d-effectkit-createeffect-f.md#createeffect) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Color](arkts-arkgraphics2d-effectkit-color-i.md) |
| [ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i.md) |
| [Filter](arkts-arkgraphics2d-effectkit-filter-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ColorPicker](arkts-arkgraphics2d-effectkit-colorpicker-i-sys.md) |
| [Filter](arkts-arkgraphics2d-effectkit-filter-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PictureComplexityDegree](arkts-arkgraphics2d-effectkit-picturecomplexitydegree-e-sys.md) |
| [PictureLightDegree](arkts-arkgraphics2d-effectkit-picturelightdegree-e-sys.md) |
| [PictureShadeDegree](arkts-arkgraphics2d-effectkit-pictureshadedegree-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EllipticalMaskCenter](arkts-arkgraphics2d-effectkit-ellipticalmaskcenter-t-sys.md) |
| [EllipticalMaskRadius](arkts-arkgraphics2d-effectkit-ellipticalmaskradius-t-sys.md) |
<!--DelEnd-->
