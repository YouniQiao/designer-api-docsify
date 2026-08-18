# uiEffect

This module provides basic capabilities for component effects, including blur, brightening, and more. Effects are categorized into the Filter and VisualEffect classes, and effects of the same class can be cascaded under an instance of that effect class. Using this module, you can quickly implement complex visual effects without needing to master underlying image processing algorithms, reducing development complexity and improving user experience. In actual development, blur can be used for background blurring, and brightening can be used for bright screen display, etc. - [Filter](arkts-arkgraphics2d-uieffect-filter-i.md#filter): Used to add specified Filter effects to a component. - [VisualEffect](arkts-arkgraphics2d-uieffect-visualeffect-i-sys.md#visualeffect): Used to add specified VisualEffect effects to a component.

**Since:** 23

<!--Device-unnamed-declare namespace uiEffect--><!--Device-unnamed-declare namespace uiEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createFilter](arkts-arkgraphics2d-uieffect-createfilter-f.md#createfilter) |
| [createEffect](arkts-arkgraphics2d-uieffect-createeffect-f.md#createeffect) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createBrightnessBlender](arkts-arkgraphics2d-uieffect-createbrightnessblender-f-sys.md#createbrightnessblender-system-api) |
| [createHdrBrightnessBlender](arkts-arkgraphics2d-uieffect-createhdrbrightnessblender-f-sys.md#createhdrbrightnessblender-system-api) |
| [createHdrDarkenBlender](arkts-arkgraphics2d-uieffect-createhdrdarkenblender-f-sys.md#createhdrdarkenblender-system-api) |
<!--DelEnd-->

<!--Del-->
### Classes（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Filter](arkts-arkgraphics2d-uieffect-filter-i.md) |
| [HdrBrightnessBlender](arkts-arkgraphics2d-uieffect-hdrbrightnessblender-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TileMode](arkts-arkgraphics2d-uieffect-tilemode-e-sys.md) |
| [WaterRippleMode](arkts-arkgraphics2d-uieffect-waterripplemode-e-sys.md) |
| [FlyMode](arkts-arkgraphics2d-uieffect-flymode-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Blender](arkts-arkgraphics2d-uieffect-blender-t-sys.md) |
<!--DelEnd-->
