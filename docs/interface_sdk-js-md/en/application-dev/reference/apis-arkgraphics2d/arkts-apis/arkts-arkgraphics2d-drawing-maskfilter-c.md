# MaskFilter

Implements a mask filter.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 12.
> 
> - This module uses the physical pixel unit, px.
> 
> - This module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-class MaskFilter--><!--Device-drawing-class MaskFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## createBlurMaskFilter

```TypeScript
static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter
```

Creates a mask filter with a blur effect.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-MaskFilter-static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter--><!--Device-MaskFilter-static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurType | [BlurType](arkts-arkgraphics2d-drawing-blurtype-e.md) | Yes | Blur type. |
| sigma | number | Yes | Standard deviation of the Gaussian blur to apply. The value must be a floating point number greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) | Maskfilter** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createBlurMaskFilter

```TypeScript
static createBlurMaskFilter(blurType: BlurType, sigma: double): MaskFilter | undefined
```

Creates a mask filter with a blur effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-MaskFilter-static createBlurMaskFilter(blurType: BlurType, sigma: double): MaskFilter | undefined--><!--Device-MaskFilter-static createBlurMaskFilter(blurType: BlurType, sigma: double): MaskFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurType | [BlurType](arkts-arkgraphics2d-drawing-blurtype-e.md) | Yes | Blur type. |
| sigma | double | Yes | Standard deviation of the Gaussian blur to apply. The value must be a floating point number greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) | MaskFilter object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

