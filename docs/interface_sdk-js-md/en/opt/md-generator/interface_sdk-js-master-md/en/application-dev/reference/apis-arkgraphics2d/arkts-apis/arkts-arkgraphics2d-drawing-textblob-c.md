# TextBlob

Defines a block consisting of one or more characters with the same font. > **NOTE：**> > - This module uses the physical pixel unit, px. > > - The module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

**Deprecated since:** -1

<!--Device-drawing-class TextBlob--><!--Device-drawing-class TextBlob-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## bounds

```TypeScript
bounds(): common2D.Rect
```

Obtains the rectangular bounding box of the text blob.

**Since:** 11

**Deprecated since:** -1

<!--Device-TextBlob-bounds(): common2D.Rect--><!--Device-TextBlob-bounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## bounds

```TypeScript
bounds(): common2D.Rect | undefined
```

Obtains the rectangular bounding box of the text blob.

**Since:** 23

**Deprecated since:** -1

<!--Device-TextBlob-bounds(): common2D.Rect | undefined--><!--Device-TextBlob-bounds(): common2D.Rect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## makeFromPosText

```TypeScript
static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob
```

Creates a **TextBlob** object from the text. The coordinates of each font in the **TextBlob** object are determined by the coordinate information in the **points** array.

**Since:** 12

**Deprecated since:** -1

<!--Device-TextBlob-static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob--><!--Device-TextBlob-static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| len | number | Yes |
| points | common2D.Point[] | Yes |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## makeFromPosText

```TypeScript
static makeFromPosText(text: string, len: number, points: common2D.Point[], font: Font): TextBlob | undefined
```

Creates a TextBlob object from the text. The coordinates of each font in the TextBlob object are determined by the coordinate information in the points array.

**Since:** 23

**Deprecated since:** -1

<!--Device-TextBlob-static makeFromPosText(text: string, len: int, points: common2D.Point[], font: Font): TextBlob | undefined--><!--Device-TextBlob-static makeFromPosText(text: string, len: int, points: common2D.Point[], font: Font): TextBlob | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| len | number | Yes |
| points | common2D.Point[] | Yes |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## makeFromRunBuffer

```TypeScript
static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob
```

Creates a **TextBlob** object based on the **RunBuffer** information.

**Since:** 11

**Deprecated since:** -1

<!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob--><!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | Array&lt;[TextBlobRunBuffer](arkts-arkgraphics2d-drawing-textblobrunbuffer-i.md)&gt; | Yes |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | Yes |
| [bounds](arkts-arkgraphics2d-drawing-textblob-c.md) | common2D.Rect | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## makeFromRunBuffer

```TypeScript
static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | undefined
```

Creates a Textblob object based on the RunBuffer information.

**Since:** 23

**Deprecated since:** -1

<!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | undefined--><!--Device-TextBlob-static makeFromRunBuffer(pos: Array<TextBlobRunBuffer>, font: Font, bounds?: common2D.Rect): TextBlob | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | Array&lt;[TextBlobRunBuffer](arkts-arkgraphics2d-drawing-textblobrunbuffer-i.md)&gt; | Yes |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | Yes |
| [bounds](arkts-arkgraphics2d-drawing-textblob-c.md) | common2D.Rect | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## makeFromString

```TypeScript
static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob
```

Converts a value of the string type into a **TextBlob** object.

**Since:** 11

**Deprecated since:** -1

<!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob--><!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | Yes |
| encoding | [TextEncoding](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textencoding-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## makeFromString

```TypeScript
static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob | undefined
```

Converts a value of the string type into a TextBlob object.

**Since:** 23

**Deprecated since:** -1

<!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob | undefined--><!--Device-TextBlob-static makeFromString(text: string, font: Font, encoding?: TextEncoding): TextBlob | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| font | [Font](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-font-c.md) | Yes |
| encoding | [TextEncoding](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textencoding-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## uniqueID

```TypeScript
uniqueID(): number
```

Obtains the unique, non-zero identifier of this **TextBlob** object.

**Since:** 23

**Deprecated since:** -1

<!--Device-TextBlob-uniqueID(): long--><!--Device-TextBlob-uniqueID(): long-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
