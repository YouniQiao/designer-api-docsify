# LeadingMarginSpan

Defines custom indentation for text paragraphs. Only a base class is provided; the specific implementation is left to developers.

**Since:** 22

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getLeadingMargin

```TypeScript
abstract getLeadingMargin(): LengthMetrics
```

Returns the indentation distance for a text paragraph.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LengthMetrics](arkts-arkui-lengthmetrics-t.md) |

## onDraw

```TypeScript
abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void
```

Draws a custom pattern. This API is triggered once for each line of text in a paragraph.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [DrawContext](arkts-arkui-graphics-drawcontext-c.md) | Yes |
| drawInfo | [LeadingMarginSpanDrawInfo](arkts-arkui-leadingmarginspandrawinfo-i.md) | Yes |
