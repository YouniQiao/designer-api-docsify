# LineTypeset

Implements a carrier that stores the text content and style. It can be used to compute layout details for individual lines of text.Before calling any of the following APIs, you must use [buildLineTypeset()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#buildlinetypeset) in the [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md) class to create a **LineTypeset** object.

**Since:** 18

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## createLine

```TypeScript
createLine(startIndex: number, count: number): TextLine
```

Generates a text line object based on the specified layout range.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startIndex | number | Yes |
| count | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## getLineBreak

```TypeScript
getLineBreak(startIndex: number, width: number): number
```

Obtains the number of characters that can fit in the layout from the specified position within a limited width.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startIndex | number | Yes |
| width | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
