# ParagraphStyleInterface

ParagraphStyleInterface

**Since:** 12

<!--Device-unnamed-declare interface ParagraphStyleInterface--><!--Device-unnamed-declare interface ParagraphStyleInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## leadingMargin

```TypeScript
leadingMargin?: LengthMetrics | LeadingMarginPlaceholder
```

Indent of the text paragraph. The value cannot be in percentage.

Default value: **0**.

**Type:** LengthMetrics | LeadingMarginPlaceholder

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ParagraphStyleInterface-leadingMargin?: LengthMetrics | LeadingMarginPlaceholder--><!--Device-ParagraphStyleInterface-leadingMargin?: LengthMetrics | LeadingMarginPlaceholder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## leadingMarginSpan

```TypeScript
leadingMarginSpan?: LeadingMarginSpan
```

Custom indentation information for text paragraphs. The value cannot be in percentage.

Default value: **0**.

**Type:** LeadingMarginSpan

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ParagraphStyleInterface-leadingMarginSpan?: LeadingMarginSpan--><!--Device-ParagraphStyleInterface-leadingMarginSpan?: LeadingMarginSpan-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxLines

```TypeScript
maxLines?: number
```

Maximum number of lines in the text paragraph. By default, the number of lines is not limited.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ParagraphStyleInterface-maxLines?: number--><!--Device-ParagraphStyleInterface-maxLines?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow?: TextOverflow
```

Display mode when the text is too long in the text paragraph.

Default value: **TextOverflow.None**.

This parameter must be used with **maxLines** for the settings to take effect. **TextOverflow.MARQUEE** is not supported.

**Type:** TextOverflow

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ParagraphStyleInterface-overflow?: TextOverflow--><!--Device-ParagraphStyleInterface-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paragraphSpacing

```TypeScript
paragraphSpacing?: LengthMetrics
```

Paragraph spacing of the styled string text.

Default value: **0**. The value cannot be in percentage.

**Type:** LengthMetrics

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-ParagraphStyleInterface-paragraphSpacing?: LengthMetrics--><!--Device-ParagraphStyleInterface-paragraphSpacing?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shaderStyle

```TypeScript
shaderStyle?: ShaderStyle
```

Text shader effect.

This API does not take effect when used together with [TextStyleInterface](arkts-arkui-styled-string-textstyleinterface-i.md)**strokeWidth**. **shaderStyle** has a higher priority than [TextStyleInterface](arkts-arkui-styled-string-textstyleinterface-i.md)**fontColor**.

**Since**: 26.0.0.

**Type:** ShaderStyle

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ParagraphStyleInterface-shaderStyle?: ShaderStyle--><!--Device-ParagraphStyleInterface-shaderStyle?: ShaderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tailIndents

```TypeScript
tailIndents?: LengthMetrics | Array<LengthMetrics>
```

Specify the tail indentation for each line in a paragraph.

<p><strong>NOTE</strong>:<br>When a single LengthMetrics value is provided, all lines share the same tail indent.<br>When an array is provided, the i-th element specifies the tail indent for the i-th line.If the number of text lines exceeds the array length, the last element in the array is used for the remaining lines.<br>Negative values are treated as 0.</p>

**Type:** LengthMetrics | Array<LengthMetrics>

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ParagraphStyleInterface-tailIndents?: LengthMetrics | Array<LengthMetrics>--><!--Device-ParagraphStyleInterface-tailIndents?: LengthMetrics | Array<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign?: TextAlign
```

Horizontal alignment of the text paragraph.

Default value: **TextAlign.Start**.

**Type:** TextAlign

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ParagraphStyleInterface-textAlign?: TextAlign--><!--Device-ParagraphStyleInterface-textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textDirection

```TypeScript
textDirection?: TextDirection
```

Text direction.

Default value: **TextDirection.DEFAULT**

**Type:** TextDirection

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ParagraphStyleInterface-textDirection?: TextDirection--><!--Device-ParagraphStyleInterface-textDirection?: TextDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textIndent

```TypeScript
textIndent?: LengthMetrics
```

First line indent of the text paragraph. The value cannot be in percentage.

Default value: **0**.

**Type:** LengthMetrics

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ParagraphStyleInterface-textIndent?: LengthMetrics--><!--Device-ParagraphStyleInterface-textIndent?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textVerticalAlign

```TypeScript
textVerticalAlign?: TextVerticalAlign
```

Vertical alignment mode of text paragraphs.

Default value: **TextVerticalAlign.BASELINE**.

**Type:** TextVerticalAlign

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ParagraphStyleInterface-textVerticalAlign?: TextVerticalAlign--><!--Device-ParagraphStyleInterface-textVerticalAlign?: TextVerticalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## wordBreak

```TypeScript
wordBreak?: WordBreak
```

Word break rule of the text paragraph.

Default value: **WordBreak.NORMAL**.

**Type:** WordBreak

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ParagraphStyleInterface-wordBreak?: WordBreak--><!--Device-ParagraphStyleInterface-wordBreak?: WordBreak-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

