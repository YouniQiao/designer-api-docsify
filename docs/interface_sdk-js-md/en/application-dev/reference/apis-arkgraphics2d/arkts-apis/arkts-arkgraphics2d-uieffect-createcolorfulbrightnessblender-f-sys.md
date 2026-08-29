# createColorfulBrightnessBlender (System API)

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## createColorfulBrightnessBlender

```TypeScript
function createColorfulBrightnessBlender(brightnessBlenderParam: BrightnessBlenderParam,
    options?: ColorfulBrightnessBlenderOptions): ColorfulBrightnessBlender
```

Creates a ColorfulBrightnessBlender instance for adding a colorful brightness darken effect to a component.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.1.0.

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightnessBlenderParam | [BrightnessBlenderParam](arkts-arkgraphics2d-graphics-uieffect-brightnessblenderparam-i-sys.md) | Yes | Regular parameters for the colorful brightness darken effect. |
| options | [ColorfulBrightnessBlenderOptions](arkts-arkgraphics2d-uieffect-colorfulbrightnessblenderoptions-i-sys.md) | No | Enhanced parameters for the colorful brightness darken effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorfulBrightnessBlender](arkts-arkgraphics2d-uieffect-colorfulbrightnessblender-i-sys.md) | Returns the colorful brightness darken blender. |
