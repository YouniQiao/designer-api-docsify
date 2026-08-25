# createHdrDarkenBlender (System API)

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## createHdrDarkenBlender

```TypeScript
function createHdrDarkenBlender(hdrBrightnessRatio: number,
    grayscaleFactor?: [number, number, number]): HdrDarkenBlender
```

Creates an HdrDarkenBlender instance for HDR layer darken blending effect.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hdrBrightnessRatio | number | Yes |
| [grayscaleFactor](arkts-arkgraphics2d-uieffect-hdrdarkenblender-i-sys.md) | [number, number, number] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HdrDarkenBlender](arkts-arkgraphics2d-uieffect-hdrdarkenblender-i-sys.md) |
