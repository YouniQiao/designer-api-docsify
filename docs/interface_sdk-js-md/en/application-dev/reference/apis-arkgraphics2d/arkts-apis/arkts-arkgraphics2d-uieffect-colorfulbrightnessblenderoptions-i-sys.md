# ColorfulBrightnessBlenderOptions (System API)

Parameter list of ColorfulBrightnessBlenderOptions, used to configure various properties of the colorful brightness darken effect, including the foreground darken weight, brightness darken strength, luma difference threshold, and HDR switch parameters.

**Since:** 26.1.0

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## darkenWeight

```TypeScript
darkenWeight?: number
```

Foreground color darken weight. When the value is 1, the color tends to be darker than the original color; when the value is 0, the color tends to be brighter than the original color. The value range is [0, 1], and values outside the range will be clamped during implementation.

**Type:** number

**Default:** 1

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.1.0.

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## hdrEnabled

```TypeScript
hdrEnabled?: boolean
```

Whether to actively enable HDR. When disabled, HDR may still be passively triggered if the foreground or background is HDR.

**Type:** boolean

**Default:** true

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.1.0.

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## lumaDiff

```TypeScript
lumaDiff?: number
```

Luma difference threshold to ensure readability. The value range is [0, 1], and values outside the range will be clamped during implementation.

**Type:** number

**Default:** 0

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.1.0.

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## vibrancyStrength

```TypeScript
vibrancyStrength?: number
```

Brightness darken effect strength. The value range is [0, 1], and values outside the range will be clamped during implementation.

**Type:** number

**Default:** 0

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.1.0.

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.
