# ColorFilter

Defines a color filter. > **NOTE：**> > - This module uses the physical pixel unit, px. > > - This module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

<!--Device-drawing-class ColorFilter--><!--Device-drawing-class ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
```

## createBlendModeColorFilter

```TypeScript
static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter
```

Creates a **ColorFilter** object with a given color and blend mode.

**Since:** 11

<!--Device-ColorFilter-static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter--><!--Device-ColorFilter-static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color | Yes |
| mode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createBlendModeColorFilter

```TypeScript
static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter | undefined
```

Creates a ColorFilter object with a given color and blend mode.

**Since:** 23

<!--Device-ColorFilter-static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter | undefined--><!--Device-ColorFilter-static createBlendModeColorFilter(color: common2D.Color, mode: BlendMode): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color | Yes |
| mode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createBlendModeColorFilter

```TypeScript
static createBlendModeColorFilter(color: common2D.Color | number, mode: BlendMode): ColorFilter
```

Creates a **ColorFilter** object with a given color and blend mode.

**Since:** 18

<!--Device-ColorFilter-static createBlendModeColorFilter(color: common2D.Color | number, mode: BlendMode): ColorFilter--><!--Device-ColorFilter-static createBlendModeColorFilter(color: common2D.Color | number, mode: BlendMode): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color \| number | Yes |
| mode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createBlendModeColorFilter

```TypeScript
static createBlendModeColorFilter(color: common2D.Color | number, mode: BlendMode): ColorFilter | undefined
```

Creates a ColorFilter object with a given color and blend mode.

**Since:** 23

<!--Device-ColorFilter-static createBlendModeColorFilter(color: common2D.Color | int, mode: BlendMode): ColorFilter | undefined--><!--Device-ColorFilter-static createBlendModeColorFilter(color: common2D.Color | int, mode: BlendMode): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color \| number | Yes |
| mode | [BlendMode](../../apis-na/arkts-apis/arkts-na-common-blendmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createComposeColorFilter

```TypeScript
static createComposeColorFilter(outer: ColorFilter, inner: ColorFilter): ColorFilter
```

Creates a **ColorFilter** object by combining another two color filters.

**Since:** 11

<!--Device-ColorFilter-static createComposeColorFilter(outer: ColorFilter, inner: ColorFilter): ColorFilter--><!--Device-ColorFilter-static createComposeColorFilter(outer: ColorFilter, inner: ColorFilter): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| outer | [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) | Yes |
| inner | [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createComposeColorFilter

```TypeScript
static createComposeColorFilter(outer: ColorFilter, inner: ColorFilter): ColorFilter | undefined
```

Creates a ColorFilter object by combining another two color filters.

**Since:** 23

<!--Device-ColorFilter-static createComposeColorFilter(outer: ColorFilter, inner: ColorFilter): ColorFilter | undefined--><!--Device-ColorFilter-static createComposeColorFilter(outer: ColorFilter, inner: ColorFilter): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| outer | [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) | Yes |
| inner | [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createLightingColorFilter

```TypeScript
static createLightingColorFilter(mutColor: common2D.Color | number, addColor: common2D.Color | number): ColorFilter
```

Creates a lighting color filter. It multiplies the RGB channel values by one color and then adds another color value. The final output stays between 0 and 255.

**Since:** 20

<!--Device-ColorFilter-static createLightingColorFilter(mutColor: common2D.Color | number, addColor: common2D.Color | number): ColorFilter--><!--Device-ColorFilter-static createLightingColorFilter(mutColor: common2D.Color | number, addColor: common2D.Color | number): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mutColor | common2D.Color \| number | Yes |
| addColor | common2D.Color \| number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## createLightingColorFilter

```TypeScript
static createLightingColorFilter(mutColor: common2D.Color | number, addColor: common2D.Color | number): ColorFilter | undefined
```

Makes a color filter with the given mutColor and addColor.

**Since:** 24

<!--Device-ColorFilter-static createLightingColorFilter(mutColor: common2D.Color | int, addColor: common2D.Color | int): ColorFilter | undefined--><!--Device-ColorFilter-static createLightingColorFilter(mutColor: common2D.Color | int, addColor: common2D.Color | int): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mutColor | common2D.Color \| number | Yes |
| addColor | common2D.Color \| number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## createLinearToSRGBGamma

```TypeScript
static createLinearToSRGBGamma(): ColorFilter
```

Creates a **ColorFilter** object that applies the sRGB gamma curve to the RGB channels.

**Since:** 11

<!--Device-ColorFilter-static createLinearToSRGBGamma(): ColorFilter--><!--Device-ColorFilter-static createLinearToSRGBGamma(): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## createLinearToSRGBGamma

```TypeScript
static createLinearToSRGBGamma(): ColorFilter | undefined
```

Creates a ColorFilter object that applies the sRGB gamma curve to the RGB channels.

**Since:** 23

<!--Device-ColorFilter-static createLinearToSRGBGamma(): ColorFilter | undefined--><!--Device-ColorFilter-static createLinearToSRGBGamma(): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## createLumaColorFilter

```TypeScript
static createLumaColorFilter(): ColorFilter
```

Creates a **ColorFilter** object that multiplies the luma into the alpha channel and sets the RGB channels to zero.

**Since:** 11

<!--Device-ColorFilter-static createLumaColorFilter(): ColorFilter--><!--Device-ColorFilter-static createLumaColorFilter(): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## createLumaColorFilter

```TypeScript
static createLumaColorFilter(): ColorFilter | undefined
```

Creates a ColorFilter object that multiplies the luma into the alpha channel and sets the RGB channels to zero.

**Since:** 23

<!--Device-ColorFilter-static createLumaColorFilter(): ColorFilter | undefined--><!--Device-ColorFilter-static createLumaColorFilter(): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## createMatrixColorFilter

```TypeScript
static createMatrixColorFilter(matrix: Array<number>): ColorFilter
```

Creates a color filter object with a 4*5 color matrix.

**Since:** 12

<!--Device-ColorFilter-static createMatrixColorFilter(matrix: Array<double>): ColorFilter--><!--Device-ColorFilter-static createMatrixColorFilter(matrix: Array<double>): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createMatrixColorFilter

```TypeScript
static createMatrixColorFilter(matrix: Array<number>): ColorFilter | undefined
```

Creates a color filter object with a 4*5 color matrix.

**Since:** 23

<!--Device-ColorFilter-static createMatrixColorFilter(matrix: Array<double>): ColorFilter | undefined--><!--Device-ColorFilter-static createMatrixColorFilter(matrix: Array<double>): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createSRGBGammaToLinear

```TypeScript
static createSRGBGammaToLinear(): ColorFilter
```

Creates a **ColorFilter** object that applies the RGB channels to the sRGB gamma curve.

**Since:** 11

<!--Device-ColorFilter-static createSRGBGammaToLinear(): ColorFilter--><!--Device-ColorFilter-static createSRGBGammaToLinear(): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## createSRGBGammaToLinear

```TypeScript
static createSRGBGammaToLinear(): ColorFilter | undefined
```

Creates a ColorFilter object that applies the RGB channels to the sRGB gamma curve.

**Since:** 23

<!--Device-ColorFilter-static createSRGBGammaToLinear(): ColorFilter | undefined--><!--Device-ColorFilter-static createSRGBGammaToLinear(): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |
