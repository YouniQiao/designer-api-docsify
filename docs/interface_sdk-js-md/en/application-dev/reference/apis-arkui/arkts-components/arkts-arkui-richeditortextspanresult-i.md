# RichEditorTextSpanResult

文本Span信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface RichEditorTextSpanResult--><!--Device-unnamed-declare interface RichEditorTextSpanResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offsetInSpan

```TypeScript
offsetInSpan: [number, number]
```

文本Span内容里有效内容的起始和结束位置。

**Type:** [number, number]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextSpanResult-offsetInSpan: [number, number]--><!--Device-RichEditorTextSpanResult-offsetInSpan: [number, number]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paragraphStyle

```TypeScript
paragraphStyle?: RichEditorParagraphStyle
```

段落样式。

省略时，使用系统默认段落样式。

**Type:** [RichEditorParagraphStyle](../arkts-apis/arkts-arkui-richeditor-richeditorparagraphstyle-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextSpanResult-paragraphStyle?: RichEditorParagraphStyle--><!--Device-RichEditorTextSpanResult-paragraphStyle?: RichEditorParagraphStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## previewText

```TypeScript
previewText?: string
```

文本Span预上屏内容。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextSpanResult-previewText?: string--><!--Device-RichEditorTextSpanResult-previewText?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spanPosition

```TypeScript
spanPosition: RichEditorSpanPosition
```

Span位置。

**Type:** [RichEditorSpanPosition](arkts-arkui-richeditorspanposition-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextSpanResult-spanPosition: RichEditorSpanPosition--><!--Device-RichEditorTextSpanResult-spanPosition: RichEditorSpanPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolSpanStyle

```TypeScript
symbolSpanStyle?: RichEditorSymbolSpanStyle
```

组件SymbolSpan样式信息。

**Type:** [RichEditorSymbolSpanStyle](../arkts-apis/arkts-arkui-richeditor-richeditorsymbolspanstyle-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextSpanResult-symbolSpanStyle?: RichEditorSymbolSpanStyle--><!--Device-RichEditorTextSpanResult-symbolSpanStyle?: RichEditorSymbolSpanStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textStyle

```TypeScript
textStyle: RichEditorTextStyleResult
```

文本Span样式信息。

**Type:** [RichEditorTextStyleResult](../arkts-apis/arkts-arkui-richeditor-richeditortextstyleresult-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextSpanResult-textStyle: RichEditorTextStyleResult--><!--Device-RichEditorTextSpanResult-textStyle: RichEditorTextStyleResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## urlStyle

```TypeScript
urlStyle?: RichEditorUrlStyle
```

url信息。

默认值：undefined。

当需要为文本设置超链接样式时传入此参数。

**Type:** [RichEditorUrlStyle](arkts-arkui-richeditorurlstyle-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RichEditorTextSpanResult-urlStyle?: RichEditorUrlStyle--><!--Device-RichEditorTextSpanResult-urlStyle?: RichEditorUrlStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: string
```

文本Span内容或Symbol的id。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextSpanResult-value: string--><!--Device-RichEditorTextSpanResult-value: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## valueResource

```TypeScript
valueResource?: Resource
```

SymbolSpan资源内容。

默认值：undefined。

**Type:** [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextSpanResult-valueResource?: Resource--><!--Device-RichEditorTextSpanResult-valueResource?: Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

