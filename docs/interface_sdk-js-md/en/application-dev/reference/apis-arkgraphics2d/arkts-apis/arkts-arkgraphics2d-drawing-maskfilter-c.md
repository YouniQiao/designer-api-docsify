# MaskFilter

Implements a mask filter. &gt; **NOTE：**&gt; &gt; - The initial APIs of this class are supported since API version 12. &gt; &gt; - This module uses the physical pixel unit, px. &gt; &gt; - This module operates under a single-threaded model. The caller needs to manage thread safety and context state &gt; transitions.

**Since:** 23

<!--Device-drawing-class MaskFilter--><!--Device-drawing-class MaskFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## createBlurMaskFilter

```TypeScript
static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter
```

Creates a mask filter with a blur effect.

**Since:** 12

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

## createBlurMaskFilter

```TypeScript
static createBlurMaskFilter(blurType: BlurType, sigma: double): MaskFilter | undefined
```

Creates a mask filter with a blur effect.

**Since:** 23

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
| [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) \| undefined | MaskFilter object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

