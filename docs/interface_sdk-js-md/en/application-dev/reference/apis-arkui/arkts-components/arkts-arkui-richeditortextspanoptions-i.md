# RichEditorTextSpanOptions

添加文本的偏移位置和文本样式信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface RichEditorTextSpanOptions--><!--Device-unnamed-declare interface RichEditorTextSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gesture

```TypeScript
gesture?: RichEditorGesture
```

行为触发回调。当需要自定义文本Span的点击或长按交互行为时传入此参数；省略时，仅使用系统默认行为。

**Type:** [RichEditorGesture](arkts-arkui-richeditorgesture-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextSpanOptions-gesture?: RichEditorGesture--><!--Device-RichEditorTextSpanOptions-gesture?: RichEditorGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: number
```

添加文本的位置。省略时，添加到所有内容的最后。

当值小于0时，放在所有内容最前面；当值大于所有内容长度时，放在所有内容最后面。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextSpanOptions-offset?: number--><!--Device-RichEditorTextSpanOptions-offset?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paragraphStyle

```TypeScript
paragraphStyle?: RichEditorParagraphStyle
```

段落样式。当需要设置文本的对齐方式、缩进、断行规则等段落级排版属性时传入此参数。不传入时，使用系统默认段落样式（左对齐、无缩进、按单词断行）。

**Type:** [RichEditorParagraphStyle](../arkts-apis/arkts-arkui-richeditor-richeditorparagraphstyle-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextSpanOptions-paragraphStyle?: RichEditorParagraphStyle--><!--Device-RichEditorTextSpanOptions-paragraphStyle?: RichEditorParagraphStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: RichEditorTextStyle
```

文本样式信息。当需要设置文本的颜色、字体大小、粗细等自定义样式时传入此参数。省略时，使用系统默认文本信息。

**Type:** [RichEditorTextStyle](arkts-arkui-richeditortextstyle-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextSpanOptions-style?: RichEditorTextStyle--><!--Device-RichEditorTextSpanOptions-style?: RichEditorTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## urlStyle

```TypeScript
urlStyle?: RichEditorUrlStyle
```

url信息。

默认值：undefined

**Type:** [RichEditorUrlStyle](arkts-arkui-richeditorurlstyle-i.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-RichEditorTextSpanOptions-urlStyle?: RichEditorUrlStyle--><!--Device-RichEditorTextSpanOptions-urlStyle?: RichEditorUrlStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

