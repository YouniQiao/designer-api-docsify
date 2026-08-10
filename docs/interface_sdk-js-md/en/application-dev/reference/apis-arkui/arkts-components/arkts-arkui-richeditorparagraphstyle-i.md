# RichEditorParagraphStyle

段落样式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface RichEditorParagraphStyle--><!--Device-unnamed-declare interface RichEditorParagraphStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## leadingMargin

```TypeScript
leadingMargin?: Dimension | LeadingMarginPlaceholder
```

设置文本段落缩进，当段落仅存在ImageSpan或BuilderSpan时，此属性值不生效。参数为Dimension类型时，不支持以Percentage形式设置，默认单位为vp。默认值：{"size":  
["0.00px","0.00px"]}

**Type:** [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| LeadingMarginPlaceholder

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorParagraphStyle-leadingMargin?: Dimension | LeadingMarginPlaceholder--><!--Device-RichEditorParagraphStyle-leadingMargin?: Dimension | LeadingMarginPlaceholder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineBreakStrategy

```TypeScript
lineBreakStrategy?: LineBreakStrategy
```

设置折行规则。 

默认值：LineBreakStrategy.GREEDY

在wordBreak不等于breakAll的时候生效，不支持连字符。

**Type:** [LineBreakStrategy](../arkts-apis/arkts-arkui-enums-linebreakstrategy-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorParagraphStyle-lineBreakStrategy?: LineBreakStrategy--><!--Device-RichEditorParagraphStyle-lineBreakStrategy?: LineBreakStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paragraphSpacing

```TypeScript
paragraphSpacing?: number
```

设置段落间距大小。

单位：fp

取值范围：[0, +∞)。传入负值时，按默认值处理。

段落间距默认大小为0。

**Type:** number

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RichEditorParagraphStyle-paragraphSpacing?: number--><!--Device-RichEditorParagraphStyle-paragraphSpacing?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shaderStyle

```TypeScript
shaderStyle?: ShaderStyle
```

设置文本着色器效果。

默认值：undefined，不设置着色器效果。

该接口与[RichEditorTextStyle](arkts-arkui-richeditortextstyle-i.md)中的strokeWidth同时设置时，该接口不生效，shaderStyle的优先级高于  
[RichEditorTextStyle](arkts-arkui-richeditortextstyle-i.md)的fontColor。

**Type:** [ShaderStyle](../arkts-apis/arkts-arkui-shaderstyle-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RichEditorParagraphStyle-shaderStyle?: ShaderStyle--><!--Device-RichEditorParagraphStyle-shaderStyle?: ShaderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign?: TextAlign
```

设置文本段落在水平方向的对齐方式。默认值：TextAlign.START

**Type:** [TextAlign](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textalign-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorParagraphStyle-textAlign?: TextAlign--><!--Device-RichEditorParagraphStyle-textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textDirection

```TypeScript
textDirection?: TextDirection
```

设置文本方向。

默认值：TextDirection.DEFAULT

**Type:** [TextDirection](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textdirection-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-RichEditorParagraphStyle-textDirection?: TextDirection--><!--Device-RichEditorParagraphStyle-textDirection?: TextDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textVerticalAlign

```TypeScript
textVerticalAlign?: TextVerticalAlign
```

设置文本段落在垂直方向的对齐方式。

默认值：TextVerticalAlign.BASELINE

**Type:** [TextVerticalAlign](../arkts-apis/arkts-arkui-textverticalalign-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RichEditorParagraphStyle-textVerticalAlign?: TextVerticalAlign--><!--Device-RichEditorParagraphStyle-textVerticalAlign?: TextVerticalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## wordBreak

```TypeScript
wordBreak?: WordBreak
```

设置断行规则。

默认值：WordBreak.BREAK_WORD。

**Type:** [WordBreak](../arkts-apis/arkts-arkui-enums-wordbreak-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorParagraphStyle-wordBreak?: WordBreak--><!--Device-RichEditorParagraphStyle-wordBreak?: WordBreak-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

