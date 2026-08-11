# ParagraphStyleInterface

ParagraphStyleInterface

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ParagraphStyleInterface--><!--Device-unnamed-export declare interface ParagraphStyleInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## leadingMargin

```TypeScript
leadingMargin?: LengthMetrics | LeadingMarginPlaceholder
```

Leading margin.

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| LeadingMarginPlaceholder

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-leadingMargin?: LengthMetrics | LeadingMarginPlaceholder--><!--Device-ParagraphStyleInterface-leadingMargin?: LengthMetrics | LeadingMarginPlaceholder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## leadingMarginSpan

```TypeScript
leadingMarginSpan?: LeadingMarginSpan
```

Leading margin span.

**Type:** [LeadingMarginSpan](arkts-arkui-styledstring-leadingmarginspan-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-leadingMarginSpan?: LeadingMarginSpan--><!--Device-ParagraphStyleInterface-leadingMarginSpan?: LeadingMarginSpan-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxLines

```TypeScript
maxLines?: int
```

The maximum number of lines of content.The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-maxLines?: int--><!--Device-ParagraphStyleInterface-maxLines?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow?: TextOverflow
```

The overflow mode of the content.

**Type:** [TextOverflow](arkts-arkui-textoverflow-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-overflow?: TextOverflow--><!--Device-ParagraphStyleInterface-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paragraphSpacing

```TypeScript
paragraphSpacing?: LengthMetrics
```

Set the paragraph spacing of the StyledString.

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-paragraphSpacing?: LengthMetrics--><!--Device-ParagraphStyleInterface-paragraphSpacing?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shaderStyle

```TypeScript
shaderStyle?: ShaderStyle
```

Set the shader style of the StyledString.

**Type:** [ShaderStyle](arkts-arkui-shaderstyle-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-shaderStyle?: ShaderStyle--><!--Device-ParagraphStyleInterface-shaderStyle?: ShaderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tailIndents

```TypeScript
tailIndents?: LengthMetrics | Array<LengthMetrics>
```

Specify the tail indentation for each line in a paragraph.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;When a single LengthMetrics value is provided, all lines share the same tail indent.&lt;br&gt;When an array is provided, the i-th element specifies the tail indent for the i-th line.If the number of text lines exceeds the array length, the last element in the array is used for the remaining lines.&lt;br&gt;Negative values are treated as 0.&lt;/p&gt;.

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| Array&lt;[LengthMetrics](arkts-arkui-lengthmetrics-t.md)&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-tailIndents?: LengthMetrics | Array<LengthMetrics>--><!--Device-ParagraphStyleInterface-tailIndents?: LengthMetrics | Array<LengthMetrics>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign?: TextAlign
```

Alignment of text.

**Type:** [TextAlign](arkts-arkui-textalign-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-textAlign?: TextAlign--><!--Device-ParagraphStyleInterface-textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textDirection

```TypeScript
textDirection?: TextDirection
```

Set the text direction of the StyledString.

**Type:** [TextDirection](arkts-arkui-textdirection-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-textDirection?: TextDirection--><!--Device-ParagraphStyleInterface-textDirection?: TextDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textIndent

```TypeScript
textIndent?: LengthMetrics
```

Set the first line indentation.

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-textIndent?: LengthMetrics--><!--Device-ParagraphStyleInterface-textIndent?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textVerticalAlign

```TypeScript
textVerticalAlign?: TextVerticalAlign
```

Vertical alignment of text.

**Type:** [TextVerticalAlign](arkts-arkui-textverticalalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-textVerticalAlign?: TextVerticalAlign--><!--Device-ParagraphStyleInterface-textVerticalAlign?: TextVerticalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## wordBreak

```TypeScript
wordBreak?: WordBreak
```

Set word break type.

**Type:** [WordBreak](arkts-arkui-wordbreak-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyleInterface-wordBreak?: WordBreak--><!--Device-ParagraphStyleInterface-wordBreak?: WordBreak-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

