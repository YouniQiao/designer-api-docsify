# Pen

Defines a pen, which is used to describe the style and color to outline a shape.

> **NOTE：**
> 
> - This module uses the physical pixel unit, px.
> 
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 11

<!--Device-drawing-class Pen--><!--Device-drawing-class Pen-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Pen** object.

**Since:** 12

<!--Device-Pen-constructor()--><!--Device-Pen-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(pen: Pen)
```

Copies a **Pen** object to create a new one.

**Since:** 12

<!--Device-Pen-constructor(pen: Pen)--><!--Device-Pen-constructor(pen: Pen)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pen | [Pen](arkts-arkgraphics2d-drawing-pen-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getAlpha

```TypeScript
getAlpha(): number
```

Obtains the alpha value of this pen.

**Since:** 12

<!--Device-Pen-getAlpha(): int--><!--Device-Pen-getAlpha(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCapStyle

```TypeScript
getCapStyle(): CapStyle
```

Obtains the cap style of this pen.

**Since:** 12

<!--Device-Pen-getCapStyle(): CapStyle--><!--Device-Pen-getCapStyle(): CapStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) |

## getColor

```TypeScript
getColor(): common2D.Color
```

Obtains the color of this pen.

**Since:** 12

<!--Device-Pen-getColor(): common2D.Color--><!--Device-Pen-getColor(): common2D.Color-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Color |

## getColor4f

```TypeScript
getColor4f(): common2D.Color4f
```

Obtains the pen color. The difference between this method and [getColor](#getColor) is that this method returns a floating point number.

**Since:** 20

<!--Device-Pen-getColor4f(): common2D.Color4f--><!--Device-Pen-getColor4f(): common2D.Color4f-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Color4f |

## getColorFilter

```TypeScript
getColorFilter(): ColorFilter
```

Obtains the color filter of this pen.

**Since:** 12

<!--Device-Pen-getColorFilter(): ColorFilter--><!--Device-Pen-getColorFilter(): ColorFilter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) |

## getFillPath

```TypeScript
getFillPath(src: Path, dst: Path): boolean
```

Obtains the source path outline drawn using this pen and represents it using a destination path.

**Since:** 12

<!--Device-Pen-getFillPath(src: Path, dst: Path): boolean--><!--Device-Pen-getFillPath(src: Path, dst: Path): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## getHexColor

```TypeScript
getHexColor(): number
```

Obtains the color of this pen.

**Since:** 18

<!--Device-Pen-getHexColor(): int--><!--Device-Pen-getHexColor(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getJoinStyle

```TypeScript
getJoinStyle(): JoinStyle
```

Obtains the join style of this pen.

**Since:** 12

<!--Device-Pen-getJoinStyle(): JoinStyle--><!--Device-Pen-getJoinStyle(): JoinStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) |

## getMiterLimit

```TypeScript
getMiterLimit(): number
```

Obtains the maximum ratio allowed between the sharp corner length of a polyline and its line width.

**Since:** 12

<!--Device-Pen-getMiterLimit(): double--><!--Device-Pen-getMiterLimit(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getWidth

```TypeScript
getWidth(): number
```

Obtains the stroke width of this pen. The width describes the thickness of the outline of a shape.

**Since:** 12

<!--Device-Pen-getWidth(): double--><!--Device-Pen-getWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## isAntiAlias

```TypeScript
isAntiAlias(): boolean
```

Checks whether anti-aliasing is enabled for this pen.

**Since:** 12

<!--Device-Pen-isAntiAlias(): boolean--><!--Device-Pen-isAntiAlias(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## reset

```TypeScript
reset(): void
```

Resets this pen to the initial state.

**Since:** 12

<!--Device-Pen-reset(): void--><!--Device-Pen-reset(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## setAlpha

```TypeScript
setAlpha(alpha: number): void
```

Sets an alpha value for this pen.

**Since:** 11

<!--Device-Pen-setAlpha(alpha: int): void--><!--Device-Pen-setAlpha(alpha: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alpha | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setAntiAlias

```TypeScript
setAntiAlias(aa: boolean): void
```

Enables anti-aliasing for this pen. Anti-aliasing makes the edges of the content smoother. If this API is not called, anti-aliasing is disabled by default.

**Since:** 11

<!--Device-Pen-setAntiAlias(aa: boolean): void--><!--Device-Pen-setAntiAlias(aa: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aa | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setBlendMode

```TypeScript
setBlendMode(mode: BlendMode): void
```

Sets a blend mode for this pen.

**Since:** 11

<!--Device-Pen-setBlendMode(mode: BlendMode): void--><!--Device-Pen-setBlendMode(mode: BlendMode): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [BlendMode](../../apis-arkui/arkts-apis/arkts-arkui-common-blendmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setCapStyle

```TypeScript
setCapStyle(style: CapStyle): void
```

Sets the cap style for this pen. If this API is not called, the default cap style is **FLAT_CAP**.

**Since:** 12

<!--Device-Pen-setCapStyle(style: CapStyle): void--><!--Device-Pen-setCapStyle(style: CapStyle): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setColor

```TypeScript
setColor(color: common2D.Color): void
```

Sets a color for this pen.

**Since:** 11

<!--Device-Pen-setColor(color: common2D.Color): void--><!--Device-Pen-setColor(color: common2D.Color): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setColor

```TypeScript
setColor(alpha: number, red: number, green: number, blue: number): void
```

Sets a color for this pen. This API provides better performance than  
[setColor](#setColor) and is recommended.

**Since:** 12

<!--Device-Pen-setColor(alpha: int, red: int, green: int, blue: int): void--><!--Device-Pen-setColor(alpha: int, red: int, green: int, blue: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alpha | number | Yes |
| red | number | Yes |
| green | number | Yes |
| blue | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setColor

```TypeScript
setColor(color: number): void
```

Sets a color for this pen.

**Since:** 18

<!--Device-Pen-setColor(color: int): void--><!--Device-Pen-setColor(color: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | number | Yes |

## setColor4f

```TypeScript
setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void
```

Sets the color and standard color gamut for this pen. The difference between this method and  
[setColor](#setColor) is that the color gamut can be set separately.

**Since:** 20

<!--Device-Pen-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void--><!--Device-Pen-setColor4f(color4f: common2D.Color4f, colorSpace: colorSpaceManager.ColorSpaceManager | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color4f | common2D.Color4f | Yes |
| colorSpace | colorSpaceManager.ColorSpaceManager \| null | Yes |

## setColorFilter

```TypeScript
setColorFilter(filter: ColorFilter | null): void
```

Sets a color filter for this pen.

**Since:** 11

<!--Device-Pen-setColorFilter(filter: ColorFilter | null): void--><!--Device-Pen-setColorFilter(filter: ColorFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | ColorFilter \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setDither

```TypeScript
setDither(dither: boolean): void
```

Enables dithering for this pen. Dithering make the drawn color more realistic.

**Since:** 11

<!--Device-Pen-setDither(dither: boolean): void--><!--Device-Pen-setDither(dither: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dither | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setImageFilter

```TypeScript
setImageFilter(filter: ImageFilter | null): void
```

Sets an image filter for this pen.

**Since:** 12

<!--Device-Pen-setImageFilter(filter: ImageFilter | null): void--><!--Device-Pen-setImageFilter(filter: ImageFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setJoinStyle

```TypeScript
setJoinStyle(style: JoinStyle): void
```

Sets the join style for this pen. If this API is not called, the default join style is **MITER_JOIN**.

**Since:** 12

<!--Device-Pen-setJoinStyle(style: JoinStyle): void--><!--Device-Pen-setJoinStyle(style: JoinStyle): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setMaskFilter

```TypeScript
setMaskFilter(filter: MaskFilter | null): void
```

Adds a mask filter for this pen.

**Since:** 12

<!--Device-Pen-setMaskFilter(filter: MaskFilter | null): void--><!--Device-Pen-setMaskFilter(filter: MaskFilter | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setMiterLimit

```TypeScript
setMiterLimit(miter: number): void
```

Sets the maximum ratio allowed between the sharp corner length of a polyline and its line width. When drawing a polyline with the pen, if [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md#JoinStyle) is set to **MITER_JOIN**and this maximum ratio is exceeded, the corner will be displayed as beveled instead of mitered.

**Since:** 12

<!--Device-Pen-setMiterLimit(miter: double): void--><!--Device-Pen-setMiterLimit(miter: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| miter | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setPathEffect

```TypeScript
setPathEffect(effect: PathEffect | null): void
```

Sets the path effect for this pen.

**Since:** 12

<!--Device-Pen-setPathEffect(effect: PathEffect | null): void--><!--Device-Pen-setPathEffect(effect: PathEffect | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setShaderEffect

```TypeScript
setShaderEffect(shaderEffect: ShaderEffect | null): void
```

Sets the shader effect for this pen.

**Since:** 12

<!--Device-Pen-setShaderEffect(shaderEffect: ShaderEffect | null): void--><!--Device-Pen-setShaderEffect(shaderEffect: ShaderEffect | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shaderEffect | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setShadowLayer

```TypeScript
setShadowLayer(shadowLayer: ShadowLayer | null): void
```

Sets a shadow layer for this pen. The shadow layer effect takes effect only when text is drawn.

**Since:** 12

<!--Device-Pen-setShadowLayer(shadowLayer: ShadowLayer | null): void--><!--Device-Pen-setShadowLayer(shadowLayer: ShadowLayer | null): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shadowLayer | [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) \| null | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## setStrokeWidth

```TypeScript
setStrokeWidth(width: number): void
```

Sets the stroke width for this pen. The value **0** is treated as an unusually thin width. During drawing, the width of 0 is always drawn as 1 pixel wide, regardless of any scaling applied to the canvas. Negative values are also regarded as the value **0** during the drawing process.

**Since:** 11

<!--Device-Pen-setStrokeWidth(width: double): void--><!--Device-Pen-setStrokeWidth(width: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
