# RichEditorParagraphStyle

Describes the paragraph style.

**Since:** 11

<!--Device-unnamed-declare interface RichEditorParagraphStyle--><!--Device-unnamed-declare interface RichEditorParagraphStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## leadingMargin

```TypeScript
leadingMargin?: Dimension | LeadingMarginPlaceholder
```

Indent of the paragraph. It has no effect if the paragraph starts with an image or builder span. If of the **Dimension** type, this parameter cannot be set in percentage. Default value: **{"size":["0.00px","0.00px"]}**

**Type:** Dimension \| LeadingMarginPlaceholder

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorParagraphStyle-leadingMargin?: Dimension | LeadingMarginPlaceholder--><!--Device-RichEditorParagraphStyle-leadingMargin?: Dimension | LeadingMarginPlaceholder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineBreakStrategy

```TypeScript
lineBreakStrategy?: LineBreakStrategy
```

Line break rule.

Default value: **LineBreakStrategy.GREEDY**

This parameter takes effect when **wordBreak** is not set to **breakAll**. Hyphens are not supported.

**Type:** LineBreakStrategy

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorParagraphStyle-lineBreakStrategy?: LineBreakStrategy--><!--Device-RichEditorParagraphStyle-lineBreakStrategy?: LineBreakStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paragraphSpacing

```TypeScript
paragraphSpacing?: number
```

Spacing between paragraphs.

Unit: fp

Default value: **0**

**Type:** number

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RichEditorParagraphStyle-paragraphSpacing?: number--><!--Device-RichEditorParagraphStyle-paragraphSpacing?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shaderStyle

```TypeScript
shaderStyle?: ShaderStyle
```

Set shader style.

**Type:** ShaderStyle

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RichEditorParagraphStyle-shaderStyle?: ShaderStyle--><!--Device-RichEditorParagraphStyle-shaderStyle?: ShaderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign?: TextAlign
```

Horizontal alignment mode of the text.

Default value: **TextAlign.START**

**Type:** TextAlign

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorParagraphStyle-textAlign?: TextAlign--><!--Device-RichEditorParagraphStyle-textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textDirection

```TypeScript
textDirection?: TextDirection
```

Sets the text direction.

Default value: TextDirection.DEFAULT

**Type:** TextDirection

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-RichEditorParagraphStyle-textDirection?: TextDirection--><!--Device-RichEditorParagraphStyle-textDirection?: TextDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textVerticalAlign

```TypeScript
textVerticalAlign?: TextVerticalAlign
```

Vertical alignment of text paragraphs.

Default value: **TextVerticalAlign.BASELINE**.

**Type:** TextVerticalAlign

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RichEditorParagraphStyle-textVerticalAlign?: TextVerticalAlign--><!--Device-RichEditorParagraphStyle-textVerticalAlign?: TextVerticalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## wordBreak

```TypeScript
wordBreak?: WordBreak
```

Word break rule.

Default value: **WordBreak.BREAK_WORD**

**Type:** WordBreak

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorParagraphStyle-wordBreak?: WordBreak--><!--Device-RichEditorParagraphStyle-wordBreak?: WordBreak-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

