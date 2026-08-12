# LineTypeset

Implements a carrier that stores the text content and style. It can be used to compute layout details for individual lines of text.

Before calling any of the following APIs, you must use  
[buildLineTypeset()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#buildLineTypeset) in the  
[ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md#ParagraphBuilder) class to create a **LineTypeset** object.

**Since:** 18

<!--Device-text-class LineTypeset--><!--Device-text-class LineTypeset-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from '@kit.ArkGraphics2D';
```

## createLine

```TypeScript
createLine(startIndex: number, count: number): TextLine
```

Generates a text line object based on the specified layout range.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineTypeset-createLine(startIndex: int, count: int): TextLine--><!--Device-LineTypeset-createLine(startIndex: int, count: int): TextLine-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let startIndex = 0;
let width = 100.0;
let count = lineTypeset.getLineBreak(startIndex, width);
let line : text.TextLine = lineTypeset.createLine(startIndex, count);
```

## getLineBreak

```TypeScript
getLineBreak(startIndex: number, width: number): number
```

Obtains the number of characters that can fit in the layout from the specified position within a limited width.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineTypeset-getLineBreak(startIndex: int, width: double): int--><!--Device-LineTypeset-getLineBreak(startIndex: int, width: double): int-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let startIndex = 0;
let width = 100.0;
let count = lineTypeset.getLineBreak(startIndex, width);
```
