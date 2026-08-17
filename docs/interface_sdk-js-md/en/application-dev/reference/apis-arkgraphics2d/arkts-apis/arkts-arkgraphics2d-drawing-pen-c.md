# Pen

Defines a pen, which is used to describe the style and color to outline a shape. > **NOTE：**> > - This module uses the physical pixel unit, px. > > - The module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

<!--Device-drawing-class Pen--><!--Device-drawing-class Pen-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'drawing';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Pen** object.

**Since:** 23

<!--Device-Pen-constructor()--><!--Device-Pen-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(pen: Pen)
```

Copies a **Pen** object to create a new one.

**Since:** 23

<!--Device-Pen-constructor(pen: Pen)--><!--Device-Pen-constructor(pen: Pen)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pen | Pen | Yes | Pen** object to copy. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## getAlpha

```TypeScript
getAlpha(): int
```

Obtains the alpha value of this pen.

**Since:** 23

<!--Device-Pen-getAlpha(): int--><!--Device-Pen-getAlpha(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| int | Alpha value of the pen. The return value is an integer ranging from 0 to 255. |

## getCapStyle

```TypeScript
getCapStyle(): CapStyle
```

Obtains the cap style of this pen.

**Since:** 23

<!--Device-Pen-getCapStyle(): CapStyle--><!--Device-Pen-getCapStyle(): CapStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) | Cap style. |

## getColor

```TypeScript
getColor(): common2D.Color
```

Obtains the color of this pen.

**Since:** 12

<!--Device-Pen-getColor(): common2D.Color--><!--Device-Pen-getColor(): common2D.Color-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color | Color of the pen. |

## getColor

```TypeScript
getColor(): common2D.Color | undefined
```

Obtains the color of this pen.

**Since:** 23

<!--Device-Pen-getColor(): common2D.Color | undefined--><!--Device-Pen-getColor(): common2D.Color | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color | Returns a 32-bit (ARGB) variable that describes the color. |

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f
```

Obtains the pen color. The difference between this method and [getColor](#getcolor) is that this method returns a floating point number.

**Since:** 20

<!--Device-Pen-getColor4f(): common2D.Color4f--><!--Device-Pen-getColor4f(): common2D.Color4f-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color4f | Color of the pen. |

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f | undefined
```

Obtains the color of a pen. The color is used by the pen to outline a shape.

**Since:** 24

<!--Device-Pen-getColor4f(): common2D.Color4f | undefined--><!--Device-Pen-getColor4f(): common2D.Color4f | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Color4f | Returns four floating point values that describes the color. |

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter
```

Obtains the color filter of this pen.

**Since:** 12

<!--Device-Pen-getColorFilter(): ColorFilter--><!--Device-Pen-getColorFilter(): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ColorFilter | Color filter. |

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter | undefined
```

Obtains the color filter of this pen.

**Since:** 23

<!--Device-Pen-getColorFilter(): ColorFilter | undefined--><!--Device-Pen-getColorFilter(): ColorFilter | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ColorFilter | ColorFilter. |

## getFillPath

```TypeScript
getFillPath(src: Path, dst: Path): boolean
```

Obtains the source path outline drawn using this pen and represents it using a destination path.

**Since:** 23

<!--Device-Pen-getFillPath(src: Path, dst: Path): boolean--><!--Device-Pen-getFillPath(src: Path, dst: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | Path | Yes | Source path. |
| dst | Path | Yes | Destination path. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the source path outline is obtained, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## getHexColor

```TypeScript
getHexColor(): int
```

Obtains the color of this pen.

**Since:** 23

<!--Device-Pen-getHexColor(): int--><!--Device-Pen-getHexColor(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| int | Color, represented as a 32-bit unsigned integer in hexadecimal ARGB format. |

## getJoinStyle

```TypeScript
getJoinStyle(): JoinStyle
```

Obtains the join style of this pen.

**Since:** 23

<!--Device-Pen-getJoinStyle(): JoinStyle--><!--Device-Pen-getJoinStyle(): JoinStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) | Join style. |

## getMiterLimit

```TypeScript
getMiterLimit(): double
```

Obtains the maximum ratio allowed between the sharp corner length of a polyline and its line width.

**Since:** 23

<!--Device-Pen-getMiterLimit(): double--><!--Device-Pen-getMiterLimit(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| double | Maximum ratio obtained. |

## getWidth

```TypeScript
getWidth(): double
```

Obtains the stroke width of this pen. The width describes the thickness of the outline of a shape.

**Since:** 23

<!--Device-Pen-getWidth(): double--><!--Device-Pen-getWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| double | Stroke width for the pen, in px. |

## isAntiAlias

```TypeScript
isAntiAlias(): boolean
```

Checks whether anti-aliasing is enabled for this pen.

**Since:** 23

<!--Device-Pen-isAntiAlias(): boolean--><!--Device-Pen-isAntiAlias(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that anti-aliasing is enabled, and **false** means the opposite. |

## reset

```TypeScript
reset(): void
```

Resets this pen to the initial state.

**Since:** 23

<!--Device-Pen-reset(): void--><!--Device-Pen-reset(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## setAlpha

```TypeScript
setAlpha(alpha: int): void
```

Sets an alpha value for this pen.

**Since:** 23

<!--Device-Pen-setAlpha(alpha: int): void--><!--Device-Pen-setAlpha(alpha: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alpha | int | Yes | Alpha value. The value is an integer in the range [0, 255]. If a floating point number is passed in, the value is rounded down. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

## setAntiAlias

```TypeScript
setAntiAlias(aa: boolean): void
```

Enables anti-aliasing for this pen. Anti-aliasing makes the edges of the content smoother. If this API is not called, anti-aliasing is disabled by default.

**Since:** 23

<!--Device-Pen-setAntiAlias(aa: boolean): void--><!--Device-Pen-setAntiAlias(aa: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aa | boolean | Yes | Whether to enable anti-aliasing. **true** to enable, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setBlendMode

```TypeScript
setBlendMode(mode: BlendMode): void
```

Sets a blend mode for this pen.

**Since:** 23

<!--Device-Pen-setBlendMode(mode: BlendMode): void--><!--Device-Pen-setBlendMode(mode: BlendMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | BlendMode | Yes | Blend mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

## setCapStyle

```TypeScript
setCapStyle(style: CapStyle): void
```

Sets the cap style for this pen. If this API is not called, the default cap style is **FLAT_CAP**.

**Since:** 23

<!--Device-Pen-setCapStyle(style: CapStyle): void--><!--Device-Pen-setCapStyle(style: CapStyle): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) | Yes | Cap style. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

## setColor

```TypeScript
setColor(color: common2D.Color): void
```

Sets a color for this pen.

**Since:** 23

<!--Device-Pen-setColor(color: common2D.Color): void--><!--Device-Pen-setColor(color: common2D.Color): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | common2D.Color | Yes | Color in ARGB format. The value of each color channel is an integer ranging from 0 to 255. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

## setColor

```TypeScript
setColor(alpha: int, red: int, green: int, blue: int): void
```

Sets a color for this pen. This API provides better performance than [setColor](#setcolor) and is recommended.

**Since:** 23

<!--Device-Pen-setColor(alpha: int, red: int, green: int, blue: int): void--><!--Device-Pen-setColor(alpha: int, red: int, green: int, blue: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alpha | int | Yes | Alpha channel value of the color in ARGB format. The value is an integer ranging from 0 to 255. Any passed-in floating point number is rounded down. |
| red | int | Yes | Red channel value of the color in ARGB format. The value is an integer ranging from 0 to 255 . Any passed-in floating point number is rounded down. |
| green | int | Yes | Green channel value of the color in ARGB format. The value is an integer ranging from 0 to 255. Any passed-in floating point number is rounded down. |
| blue | int | Yes | Blue channel value of the color in ARGB format. The value is an integer ranging from 0 to 2 55. Any passed-in floating point number is rounded down. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setColor

```TypeScript
setColor(color: int): void
```

Sets a color for this pen.

**Since:** 23

<!--Device-Pen-setColor(color: int): void--><!--Device-Pen-setColor(color: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | int | Yes | Color in hexadecimal ARGB format. |

## setColor4f

```TypeScript
setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void
```

Sets the color and standard color gamut for this pen. The difference between this method and [setColor](#setcolor) is that the color gamut can be set separately.

**Since:** 24

<!--Device-Pen-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void--><!--Device-Pen-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color4f | common2D.Color4f | Yes | Color in the ARGB format. The value of each color channel is a floating point number ranging from 0.0 to 1.0. Values above 1.0 default to **1.0**, and values below 0.0 default to **0.0**. |
| colorSpace | colorSpaceManager.ColorSpaceManager \| null | Yes | Standard color gamut object. **null** indicates SRGB. |

## setColorFilter

```TypeScript
setColorFilter(filter: ColorFilter | null): void
```

Sets a color filter for this pen.

**Since:** 23

<!--Device-Pen-setColorFilter(filter: ColorFilter | null): void--><!--Device-Pen-setColorFilter(filter: ColorFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | ColorFilter \| null | Yes | Defines a color filter. If **null** is passed in, the color filter is cleared.<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setDither

```TypeScript
setDither(dither: boolean): void
```

Enables dithering for this pen. Dithering make the drawn color more realistic.

**Since:** 23

<!--Device-Pen-setDither(dither: boolean): void--><!--Device-Pen-setDither(dither: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dither | boolean | Yes | Whether to enable dithering. **true** to enable, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setImageFilter

```TypeScript
setImageFilter(filter: ImageFilter | null): void
```

Sets an image filter for this pen.

**Since:** 23

<!--Device-Pen-setImageFilter(filter: ImageFilter | null): void--><!--Device-Pen-setImageFilter(filter: ImageFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | Yes | Image filter. If **null** is passed in, the image filter effect of the pen will be cleared. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setJoinStyle

```TypeScript
setJoinStyle(style: JoinStyle): void
```

Sets the join style for this pen. If this API is not called, the default join style is **MITER_JOIN**.

**Since:** 23

<!--Device-Pen-setJoinStyle(style: JoinStyle): void--><!--Device-Pen-setJoinStyle(style: JoinStyle): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) | Yes | Join style. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

## setMaskFilter

```TypeScript
setMaskFilter(filter: MaskFilter | null): void
```

Adds a mask filter for this pen.

**Since:** 23

<!--Device-Pen-setMaskFilter(filter: MaskFilter | null): void--><!--Device-Pen-setMaskFilter(filter: MaskFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) \| null | Yes | Mask filter. If **null** is passed in, the mask filter is cleared.<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setMiterLimit

```TypeScript
setMiterLimit(miter: double): void
```

Sets the maximum ratio allowed between the sharp corner length of a polyline and its line width. When drawing a polyline with the pen, if [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md#joinstyle) is set to **MITER_JOIN** and this maximum ratio is exceeded, the corner will be displayed as beveled instead of mitered.

**Since:** 23

<!--Device-Pen-setMiterLimit(miter: double): void--><!--Device-Pen-setMiterLimit(miter: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| miter | double | Yes | Maximum ratio of the sharp corner length of the polyline to the line width. A negative number is processed as **4.0** during drawing. Non-negative numbers take effect normally. The value is a floating point number. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setPathEffect

```TypeScript
setPathEffect(effect: PathEffect | null): void
```

Sets the path effect for this pen.

**Since:** 23

<!--Device-Pen-setPathEffect(effect: PathEffect | null): void--><!--Device-Pen-setPathEffect(effect: PathEffect | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) \| null | Yes | Implements a path effect. If **null** is passed in, the path filter is cleared.<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setShaderEffect

```TypeScript
setShaderEffect(shaderEffect: ShaderEffect | null): void
```

Sets the shader effect for this pen.

**Since:** 23

<!--Device-Pen-setShaderEffect(shaderEffect: ShaderEffect | null): void--><!--Device-Pen-setShaderEffect(shaderEffect: ShaderEffect | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) \| null | Yes | ShaderEffect** object. If **null** is passed in, the shader effect will be cleared.<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setShadowLayer

```TypeScript
setShadowLayer(shadowLayer: ShadowLayer | null): void
```

Sets a shadow layer for this pen. The shadow layer effect takes effect only when text is drawn.

**Since:** 23

<!--Device-Pen-setShadowLayer(shadowLayer: ShadowLayer | null): void--><!--Device-Pen-setShadowLayer(shadowLayer: ShadowLayer | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| shadowLayer | [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) \| null | Yes | Implements a shadow layer. If **null** is passed in, the shadow layer is cleared.<br>**Since:** 20 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

## setStrokeWidth

```TypeScript
setStrokeWidth(width: double): void
```

Sets the stroke width for this pen. The value **0** is treated as an unusually thin width. During drawing, the width of 0 is always drawn as 1 pixel wide, regardless of any scaling applied to the canvas. Negative values are also regarded as the value **0** during the drawing process.

**Since:** 23

<!--Device-Pen-setStrokeWidth(width: double): void--><!--Device-Pen-setStrokeWidth(width: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | double | Yes | Stroke width. The value is a floating point number. If a value less than 1 is passed in , the value **1** is used. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types. |

