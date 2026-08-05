# LeadingMarginSpan

Defines custom indentation for text paragraphs. Only a base class is provided; the specific implementation is left to developers.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-unnamed-declare abstract class LeadingMarginSpan--><!--Device-unnamed-declare abstract class LeadingMarginSpan-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLeadingMargin

```TypeScript
abstract getLeadingMargin(): LengthMetrics
```

Returns the indentation distance for a text paragraph.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LeadingMarginSpan-abstract getLeadingMargin(): LengthMetrics--><!--Device-LeadingMarginSpan-abstract getLeadingMargin(): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Paragraph indentation distance. The value cannot be in percentage. |

## onDraw

```TypeScript
abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void
```

Draws a custom pattern. This API is triggered once for each line of text in a paragraph.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LeadingMarginSpan-abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void--><!--Device-LeadingMarginSpan-abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Drawing context.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The **canvas** method of **DrawContext** obtains the canvas of the component. As such, the custom span does not extend beyond the area of the component. |
| drawInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Custom drawing information. |

