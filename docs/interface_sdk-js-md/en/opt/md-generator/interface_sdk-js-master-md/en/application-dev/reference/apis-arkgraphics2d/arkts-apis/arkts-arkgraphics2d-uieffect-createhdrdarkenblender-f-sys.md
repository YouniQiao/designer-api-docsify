# createHdrDarkenBlender (System API)

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## createHdrDarkenBlender

```TypeScript
function createHdrDarkenBlender(hdrBrightnessRatio: number,
    grayscaleFactor?: [number, number, number]): HdrDarkenBlender
```

Creates an HdrDarkenBlender instance for HDR layer darken blending effect.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiEffect-function createHdrDarkenBlender(hdrBrightnessRatio: double,    grayscaleFactor?: [double, double, double]): HdrDarkenBlender--><!--Device-uiEffect-function createHdrDarkenBlender(hdrBrightnessRatio: double,    grayscaleFactor?: [double, double, double]): HdrDarkenBlender-End-->

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

## Examples

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D'

// Create an HDR darken blender instance.
let blender : uiEffect.HdrDarkenBlender = 
  uiEffect.createHdrDarkenBlender(1.3, [0.299, 0.587, 0.114])

@Entry
@Component
struct Example {
  build() { 
    RelativeContainer() { 
      Stack(){ 
          Text("TextWord") 
          Image($r("app.media.screenshot")) 
            .width("100%") 
            .height("100%") 
            .advancedBlendMode(blender) 
      } 
    } 
  } 
}
```
