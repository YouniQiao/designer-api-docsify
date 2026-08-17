# LeadingMarginSpan

Defines LeadingMarginSpan.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-export declare abstract class LeadingMarginSpan--><!--Device-unnamed-export declare abstract class LeadingMarginSpan-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLeadingMargin

```TypeScript
abstract getLeadingMargin(): LengthMetrics
```

Get the amount by which to adjust the leading margin.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LeadingMarginSpan-abstract getLeadingMargin(): LengthMetrics--><!--Device-LeadingMarginSpan-abstract getLeadingMargin(): LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | the literal content of the StyledString |

## onDraw

```TypeScript
abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void
```

Draw the leading margin span.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LeadingMarginSpan-abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void--><!--Device-LeadingMarginSpan-abstract onDraw(context: DrawContext, drawInfo: LeadingMarginSpanDrawInfo): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [DrawContext](../../apis-na/arkts-apis/arkts-na-graphics-drawcontext-c.md) | Yes |  |
| drawInfo | [LeadingMarginSpanDrawInfo](arkts-arkui-styledstring-leadingmarginspandrawinfo-i.md) | Yes |  |

