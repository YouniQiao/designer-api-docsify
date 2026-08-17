# ParagraphStyle

Defines ParagraphStyle.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ParagraphStyle--><!--Device-unnamed-export declare class ParagraphStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value?: ParagraphStyleInterface)
```

constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-constructor(value?: ParagraphStyleInterface)--><!--Device-ParagraphStyle-constructor(value?: ParagraphStyleInterface)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ParagraphStyleInterface](arkts-arkui-styledstring-paragraphstyleinterface-i.md) | No | paragraph property object. |

## leadingMargin

```TypeScript
readonly leadingMargin?: double | LeadingMarginPlaceholder
```

Get the leading margin of the StyledString.

**Type:** double \| [LeadingMarginPlaceholder](arkts-arkui-richeditor-leadingmarginplaceholder-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly leadingMargin?: double | LeadingMarginPlaceholder--><!--Device-ParagraphStyle-readonly leadingMargin?: double | LeadingMarginPlaceholder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## leadingMarginSpan

```TypeScript
readonly leadingMarginSpan?: LeadingMarginSpan
```

Get the leading margin span of the StyledString.

**Type:** [LeadingMarginSpan](arkts-arkui-styledstring-leadingmarginspan-c.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly leadingMarginSpan?: LeadingMarginSpan--><!--Device-ParagraphStyle-readonly leadingMarginSpan?: LeadingMarginSpan-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxLines

```TypeScript
readonly maxLines?: int
```

Get the maximum number of lines of the StyledString. The value should be an integer.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly maxLines?: int--><!--Device-ParagraphStyle-readonly maxLines?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
readonly overflow?: TextOverflow
```

Get the overflow mode of the StyledString.

**Type:** [TextOverflow](arkts-arkui-textoverflow-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly overflow?: TextOverflow--><!--Device-ParagraphStyle-readonly overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paragraphSpacing

```TypeScript
readonly paragraphSpacing?: double
```

Get the paragraph spacing of the StyledString. The unit is vp.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly paragraphSpacing?: double--><!--Device-ParagraphStyle-readonly paragraphSpacing?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shaderStyle

```TypeScript
readonly shaderStyle?: ShaderStyle
```

Get the shader style of the StyledString.

**Type:** [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly shaderStyle?: ShaderStyle--><!--Device-ParagraphStyle-readonly shaderStyle?: ShaderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tailIndents

```TypeScript
readonly tailIndents?: Array<double>
```

Get the tail indentation of the StyledString. The unit is vp.

**Type:** Array&lt;double&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly tailIndents?: Array<double>--><!--Device-ParagraphStyle-readonly tailIndents?: Array<double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
readonly textAlign?: TextAlign
```

Get the text alignment of the StyledString.

**Type:** [TextAlign](arkts-arkui-textalign-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly textAlign?: TextAlign--><!--Device-ParagraphStyle-readonly textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textDirection

```TypeScript
readonly textDirection?: TextDirection
```

Get the text direction of the StyledString.

**Type:** [TextDirection](arkts-arkui-textcommon-textdirection-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly textDirection?: TextDirection--><!--Device-ParagraphStyle-readonly textDirection?: TextDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textIndent

```TypeScript
readonly textIndent?: double
```

Get the first line indentation of the StyledString. The unit is vp.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly textIndent?: double--><!--Device-ParagraphStyle-readonly textIndent?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textVerticalAlign

```TypeScript
readonly textVerticalAlign?: TextVerticalAlign
```

Get the text vertical alignment of the StyledString.

**Type:** [TextVerticalAlign](arkts-arkui-textcommon-textverticalalign-e.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly textVerticalAlign?: TextVerticalAlign--><!--Device-ParagraphStyle-readonly textVerticalAlign?: TextVerticalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## wordBreak

```TypeScript
readonly wordBreak?: WordBreak
```

Get the wordBreak mode of the StyledString.

**Type:** [WordBreak](arkts-arkui-wordbreak-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ParagraphStyle-readonly wordBreak?: WordBreak--><!--Device-ParagraphStyle-readonly wordBreak?: WordBreak-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

