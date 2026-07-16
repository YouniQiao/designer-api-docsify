# HdrDarkenBlender (System API)

The HDR-adaptive darken blender.

**Since:** 26.0.0

<!--Device-uiEffect-interface HdrDarkenBlender--><!--Device-uiEffect-interface HdrDarkenBlender-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## grayscaleFactor

```TypeScript
grayscaleFactor?: [number, number, number]
```

Defines the grayscale factor for converting dst's RGB channels to grayscale.Formula: grayscale = dot(grayscaleFactor, dst).

**Type:** [number, number, number]

**Default:** [0.299, 0.587, 0.114]

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HdrDarkenBlender-grayscaleFactor?: [double, double, double]--><!--Device-HdrDarkenBlender-grayscaleFactor?: [double, double, double]-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## hdrBrightnessRatio

```TypeScript
hdrBrightnessRatio: number
```

Defines the HDR brightness ratio of src.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-HdrDarkenBlender-hdrBrightnessRatio: double--><!--Device-HdrDarkenBlender-hdrBrightnessRatio: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

