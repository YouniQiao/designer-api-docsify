# LeadingMarginSpan

Defines custom indentation for text paragraphs. Only a base class is provided; the specific implementation is left to developers.

**Since:** 22

**Deprecated since:** -1

<!--Device-unnamed-declare abstract class LeadingMarginSpan--><!--Device-unnamed-declare abstract class LeadingMarginSpan-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLeadingMargin

```TypeScript
abstract getLeadingMargin(): LengthMetrics
```

Returns the indentation distance for a text paragraph.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LeadingMarginSpan-abstract getLeadingMargin(): LengthMetrics--><!--Device-LeadingMarginSpan-abstract getLeadingMargin(): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LengthMetrics](../../apis-na/arkts-apis/arkts-na-lengthmetrics-t.md) |

## onDraw

```TypeScript
abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void
```

Draws a custom pattern. This API is triggered once for each line of text in a paragraph.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LeadingMarginSpan-abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void--><!--Device-LeadingMarginSpan-abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [DrawContext](../../apis-na/arkts-apis/arkts-na-graphics-drawcontext-c.md) | Yes |
| drawInfo | [LeadingMarginSpanDrawInfo](arkts-arkui-leadingmarginspandrawinfo-i.md) | Yes |
