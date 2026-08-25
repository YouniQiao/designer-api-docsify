# Run

Represents a text typesetting unit, which is a continuous text segment with the same style attributes. Run is obtained through the [getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns) API of the [TextLine](arkts-arkgraphics2d-text-textline-c.md) class.Before calling any of the following APIs, you must use [getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns) of the [TextLine](arkts-arkgraphics2d-text-textline-c.md) class to create a **Run** object.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getAdvances

```TypeScript
getAdvances(range: Range): Array<common2D.Point>
```

Obtains the glyph width array of each glyph within the specified range of the run.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

## getFont

```TypeScript
getFont(): drawing.Font
```

Obtains the **Font** object of this run.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| drawing.Font |

## getGlyphCount

```TypeScript
getGlyphCount(): number
```

Obtains the number of glyphs in this run.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getGlyphs

```TypeScript
getGlyphs(): Array<number>
```

Obtains the index of each glyph in this run.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

## getGlyphs

```TypeScript
getGlyphs(range: Range): Array<number>
```

Obtains the index of each glyph in the specified range of this run.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

## getImageBounds

```TypeScript
getImageBounds(): common2D.Rect
```

Obtains the image boundaries of the typographic unit. Equivalent to visual boundaries, these boundaries are associated with the typographic font, font size, and characters. For example, for the string " a b " (which has a space before "a" and a space after "b"), only "a b" is visible to users, and therefore the image boundaries do not include these spaces at the beginning and end of the line.

> **NOTE：**&gt;
> The figure shows the image boundaries for the string " a b ".&gt;
> &gt;
> The figure shows the image boundaries for the string "j" or "E".&gt;
> 

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## getOffsets

```TypeScript
getOffsets(): Array<common2D.Point>
```

Obtains the offset of each glyph in this run relative to its index.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

## getPositions

```TypeScript
getPositions(): Array<common2D.Point>
```

Obtains the position of each glyph relative to the respective line in this run.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

## getPositions

```TypeScript
getPositions(range: Range): Array<common2D.Point>
```

Obtains the position array of each glyph relative to the respective line within the specified range of this run.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

## getStringIndices

```TypeScript
getStringIndices(range?: Range): Array<number>
```

Obtains an array of character indices for glyphs within a specified range of this run, where the indices are offsets relative to the entire paragraph.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

## getStringRange

```TypeScript
getStringRange(): Range
```

Obtains the range of glyphs generated by this run.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## getTextDirection

```TypeScript
getTextDirection(): TextDirection
```

Obtains the text direction of the run.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextDirection](arkts-arkgraphics2d-text-textdirection-e.md) |

## getTextStyle

```TypeScript
getTextStyle(): TextStyle
```

Obtains the text style of this typesetting unit.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md) |

## getTypographicBounds

```TypeScript
getTypographicBounds(): TypographicBounds
```

Obtains the typographic boundaries of the typographic unit. These boundaries are associated with the typographic font and font size, but not with the characters. For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line.

> **NOTE：**&gt;
> The figure shows the typesetting boundaries for the string " a b ".&gt;
> &gt;
> The figure shows the typesetting boundaries for the string "j" or "E".&gt;
> !
> [TypographicBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TypographicBounds](arkts-arkgraphics2d-text-typographicbounds-i.md) |

## paint

```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

Paints this run on the canvas with the coordinate point (x, y) as the upper left corner.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| canvas | drawing.Canvas | Yes |
| x | number | Yes |
| y | number | Yes |
