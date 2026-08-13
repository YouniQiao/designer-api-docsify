# Font

Describes the attributes used for text rendering, such as size and typeface. > **NOTE：**> > - This module uses the physical pixel unit, px. > > - This module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

**Deprecated since:** -1

<!--Device-drawing-class Font--><!--Device-drawing-class Font-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## countText

```TypeScript
countText(text: string): number
```

Obtains the number of glyphs represented by text.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-countText(text: string): int--><!--Device-Font-countText(text: string): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createPathForGlyph

```TypeScript
createPathForGlyph(index: number): Path
```

Obtains the outline path of a glyph.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-createPathForGlyph(index: number): Path--><!--Device-Font-createPathForGlyph(index: number): Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## createPathForGlyph

```TypeScript
createPathForGlyph(index: number): Path | undefined
```

Obtains the outline path of a glyph.

**Since:** 23

**Deprecated since:** -1

<!--Device-Font-createPathForGlyph(index: int): Path | undefined--><!--Device-Font-createPathForGlyph(index: int): Path | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## enableEmbolden

```TypeScript
enableEmbolden(isEmbolden: boolean): void
```

Enables emboldened fonts.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-enableEmbolden(isEmbolden: boolean): void--><!--Device-Font-enableEmbolden(isEmbolden: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isEmbolden](arkts-arkgraphics2d-drawing-font-c.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## enableLinearMetrics

```TypeScript
enableLinearMetrics(isLinearMetrics: boolean): void
```

Enables linear font scaling.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-enableLinearMetrics(isLinearMetrics: boolean): void--><!--Device-Font-enableLinearMetrics(isLinearMetrics: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isLinearMetrics](arkts-arkgraphics2d-drawing-font-c.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## enableSubpixel

```TypeScript
enableSubpixel(isSubpixel: boolean): void
```

Enables subpixel font rendering.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-enableSubpixel(isSubpixel: boolean): void--><!--Device-Font-enableSubpixel(isSubpixel: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isSubpixel](arkts-arkgraphics2d-drawing-font-c.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getBounds

```TypeScript
getBounds(glyphs: Array<number>): Array<common2D.Rect>
```

Obtains the rectangular bounding box of each glyph in an array.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getBounds(glyphs: Array<number>): Array<common2D.Rect>--><!--Device-Font-getBounds(glyphs: Array<number>): Array<common2D.Rect>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| glyphs | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Rect & gt; |

## getBounds

```TypeScript
getBounds(glyphs: Array<number>): Array<common2D.Rect> | undefined
```

Obtains the rectangular bounding box of each glyph in an array.

**Since:** 23

**Deprecated since:** -1

<!--Device-Font-getBounds(glyphs: Array<int>): Array<common2D.Rect> | undefined--><!--Device-Font-getBounds(glyphs: Array<int>): Array<common2D.Rect> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| glyphs | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Rect & gt; |

## getEdging

```TypeScript
getEdging(): FontEdging
```

Obtains the font edging effect.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getEdging(): FontEdging--><!--Device-Font-getEdging(): FontEdging-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FontEdging](arkts-arkgraphics2d-drawing-fontedging-e.md) |

## getEdging

```TypeScript
getEdging(): FontEdging | undefined
```

Obtains the font edging effect.

**Since:** 23

**Deprecated since:** -1

<!--Device-Font-getEdging(): FontEdging | undefined--><!--Device-Font-getEdging(): FontEdging | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FontEdging](arkts-arkgraphics2d-drawing-fontedging-e.md) |

## getHinting

```TypeScript
getHinting(): FontHinting
```

Obtains the font hinting effect.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getHinting(): FontHinting--><!--Device-Font-getHinting(): FontHinting-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FontHinting](arkts-arkgraphics2d-drawing-fonthinting-e.md) |

## getHinting

```TypeScript
getHinting(): FontHinting | undefined
```

Obtains the font hinting effect.

**Since:** 23

**Deprecated since:** -1

<!--Device-Font-getHinting(): FontHinting | undefined--><!--Device-Font-getHinting(): FontHinting | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FontHinting](arkts-arkgraphics2d-drawing-fonthinting-e.md) |

## getMetrics

```TypeScript
getMetrics(): FontMetrics
```

Obtains the font metrics of the typeface.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getMetrics(): FontMetrics--><!--Device-Font-getMetrics(): FontMetrics-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FontMetrics](arkts-arkgraphics2d-drawing-fontmetrics-i.md) |

## getMetrics

```TypeScript
getMetrics(): FontMetrics | undefined
```

Obtains the font metrics of the typeface.

**Since:** 23

**Deprecated since:** -1

<!--Device-Font-getMetrics(): FontMetrics | undefined--><!--Device-Font-getMetrics(): FontMetrics | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FontMetrics](arkts-arkgraphics2d-drawing-fontmetrics-i.md) |

## getScaleX

```TypeScript
getScaleX(): number
```

Obtains the horizontal scale ratio of this font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getScaleX(): double--><!--Device-Font-getScaleX(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getSize

```TypeScript
getSize(): number
```

Obtains the font size.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getSize(): double--><!--Device-Font-getSize(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getSkewX

```TypeScript
getSkewX(): number
```

Obtains the horizontal skew factor of this font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getSkewX(): double--><!--Device-Font-getSkewX(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getTextPath

```TypeScript
getTextPath(text: string, byteLength: number, x: number, y: number): Path
```

Obtains the outline path of a text.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getTextPath(text: string, byteLength: number, x: number, y: number): Path--><!--Device-Font-getTextPath(text: string, byteLength: number, x: number, y: number): Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| byteLength | number | Yes |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getTextPath

```TypeScript
getTextPath(text: string, byteLength: number, x: number, y: number): Path | undefined
```

Obtains the outline path of a text.

**Since:** 23

**Deprecated since:** -1

<!--Device-Font-getTextPath(text: string, byteLength: int, x: double, y: double): Path | undefined--><!--Device-Font-getTextPath(text: string, byteLength: int, x: double, y: double): Path | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| byteLength | number | Yes |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getTextPathWithFallback

```TypeScript
getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path
```

Gets the path outline for the given text with font fallback support.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path--><!--Device-Font-getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| byteLength | number | Yes |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## getTextPathWithFallback

```TypeScript
getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path | undefined
```

Gets the path outline for the given text with font fallback support.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-getTextPathWithFallback(text: string, byteLength: int, x: double, y: double): Path | undefined--><!--Device-Font-getTextPathWithFallback(text: string, byteLength: int, x: double, y: double): Path | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| byteLength | number | Yes |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |

## getTypeface

```TypeScript
getTypeface(): Typeface
```

Obtains the typeface.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getTypeface(): Typeface--><!--Device-Font-getTypeface(): Typeface-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## getTypeface

```TypeScript
getTypeface(): Typeface | undefined
```

Obtains the typeface.

**Since:** 23

**Deprecated since:** -1

<!--Device-Font-getTypeface(): Typeface | undefined--><!--Device-Font-getTypeface(): Typeface | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## getWidths

```TypeScript
getWidths(glyphs: Array<number>): Array<number>
```

Obtains the width of each glyph in an array.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-getWidths(glyphs: Array<number>): Array<number>--><!--Device-Font-getWidths(glyphs: Array<number>): Array<number>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| glyphs | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getWidths

```TypeScript
getWidths(glyphs: Array<number>): Array<number> | undefined
```

Obtains the width of each glyph in an array.

**Since:** 23

**Deprecated since:** -1

<!--Device-Font-getWidths(glyphs: Array<int>): Array<double> | undefined--><!--Device-Font-getWidths(glyphs: Array<int>): Array<double> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| glyphs | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## isBaselineSnap

```TypeScript
isBaselineSnap(): boolean
```

Checks whether baselines are requested to be snapped to pixels when the current canvas matrix is axis aligned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-isBaselineSnap(): boolean--><!--Device-Font-isBaselineSnap(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEmbeddedBitmaps

```TypeScript
isEmbeddedBitmaps(): boolean
```

Checks whether bitmaps are used in this font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-isEmbeddedBitmaps(): boolean--><!--Device-Font-isEmbeddedBitmaps(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEmbolden

```TypeScript
isEmbolden(): boolean
```

Checks whether the bold effect is set for this font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-isEmbolden(): boolean--><!--Device-Font-isEmbolden(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isForceAutoHinting

```TypeScript
isForceAutoHinting(): boolean
```

Checks whether auto hinting is forcibly used.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-isForceAutoHinting(): boolean--><!--Device-Font-isForceAutoHinting(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isLinearMetrics

```TypeScript
isLinearMetrics(): boolean
```

Checks whether linear scaling is used for this font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-isLinearMetrics(): boolean--><!--Device-Font-isLinearMetrics(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isSubpixel

```TypeScript
isSubpixel(): boolean
```

Checks whether sub-pixel rendering is used for a font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-isSubpixel(): boolean--><!--Device-Font-isSubpixel(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isThemeFontFollowed

```TypeScript
isThemeFontFollowed(): boolean
```

Checks whether the font follows the theme font. By default, the font follows the theme font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-isThemeFontFollowed(): boolean--><!--Device-Font-isThemeFontFollowed(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## measureSingleCharacter

```TypeScript
measureSingleCharacter(text: string): number
```

Measures the width of a single character. If the typeface of the current font does not support the character to measure, the system typeface is used to measure the character width.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-measureSingleCharacter(text: string): double--><!--Device-Font-measureSingleCharacter(text: string): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## measureSingleCharacterWithFeatures

```TypeScript
measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): number
```

Measures the width of a single character with font features. If the typeface of the current font does not support the character to measure, the system typeface is used to measure the character width.

**Since:** 24

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): double--><!--Device-Font-measureSingleCharacterWithFeatures(text: string, features: Array<FontFeature>): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| features | Array & lt;FontFeature & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## measureText

```TypeScript
measureText(text: string, encoding: TextEncoding): number
```

Measures the text width. > **NOTE：**> > This API is used to measure the text width of the original string. To measure the text width after typesetting, > call [measure.measureText](../../../reference/apis-arkui/arkts-apis-uicontext-measureutils.md#measuretext12).

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-measureText(text: string, encoding: TextEncoding): double--><!--Device-Font-measureText(text: string, encoding: TextEncoding): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| encoding | [TextEncoding](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textencoding-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setBaselineSnap

```TypeScript
setBaselineSnap(isBaselineSnap: boolean): void
```

Sets whether to request that baselines be snapped to pixels when the current canvas matrix is axis aligned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setBaselineSnap(isBaselineSnap: boolean): void--><!--Device-Font-setBaselineSnap(isBaselineSnap: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isBaselineSnap](arkts-arkgraphics2d-drawing-font-c.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setEdging

```TypeScript
setEdging(edging: FontEdging): void
```

Sets a font edging effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setEdging(edging: FontEdging): void--><!--Device-Font-setEdging(edging: FontEdging): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| edging | [FontEdging](arkts-arkgraphics2d-drawing-fontedging-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setEmbeddedBitmaps

```TypeScript
setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void
```

Sets whether to use bitmaps in this font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void--><!--Device-Font-setEmbeddedBitmaps(isEmbeddedBitmaps: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isEmbeddedBitmaps](arkts-arkgraphics2d-drawing-font-c.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setForceAutoHinting

```TypeScript
setForceAutoHinting(isForceAutoHinting: boolean): void
```

Sets whether to forcibly use auto hinting, that is, whether to always hint glyphs.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setForceAutoHinting(isForceAutoHinting: boolean): void--><!--Device-Font-setForceAutoHinting(isForceAutoHinting: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [isForceAutoHinting](arkts-arkgraphics2d-drawing-font-c.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setHinting

```TypeScript
setHinting(hinting: FontHinting): void
```

Sets a font hinting effect.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setHinting(hinting: FontHinting): void--><!--Device-Font-setHinting(hinting: FontHinting): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hinting | [FontHinting](arkts-arkgraphics2d-drawing-fonthinting-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setScaleX

```TypeScript
setScaleX(scaleX: number): void
```

Sets a horizontal scale factor for this font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setScaleX(scaleX: double): void--><!--Device-Font-setScaleX(scaleX: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scaleX | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setSize

```TypeScript
setSize(textSize: number): void
```

Sets the font size.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setSize(textSize: double): void--><!--Device-Font-setSize(textSize: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| textSize | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setSkewX

```TypeScript
setSkewX(skewX: number): void
```

Sets a horizontal skew factor for this font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setSkewX(skewX: double): void--><!--Device-Font-setSkewX(skewX: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [skewX](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setThemeFontFollowed

```TypeScript
setThemeFontFollowed(followed: boolean): void
```

Sets whether to follow the theme font. When **followed** is set to **true**, the theme font is used if it is enabled by the system and no typeface is set.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setThemeFontFollowed(followed: boolean): void--><!--Device-Font-setThemeFontFollowed(followed: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| followed | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setTypeface

```TypeScript
setTypeface(typeface: Typeface): void
```

Sets the typeface style (including attributes such as font name, weight, and italic) for the font.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-setTypeface(typeface: Typeface): void--><!--Device-Font-setTypeface(typeface: Typeface): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| typeface | [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## textToGlyphs

```TypeScript
textToGlyphs(text: string, glyphCount?: number): Array<number>
```

Converts text into glyph indexes.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Font-textToGlyphs(text: string, glyphCount?: number): Array<number>--><!--Device-Font-textToGlyphs(text: string, glyphCount?: number): Array<number>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| glyphCount | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## textToGlyphs

```TypeScript
textToGlyphs(text: string, glyphCount?: number): Array<number> | undefined
```

Converts text into glyph indexes.

**Since:** 23

**Deprecated since:** -1

<!--Device-Font-textToGlyphs(text: string, glyphCount?: int): Array<int> | undefined--><!--Device-Font-textToGlyphs(text: string, glyphCount?: int): Array<int> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| glyphCount | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
