# RichEditorTextSpanOptions

添加文本的偏移位置和文本样式信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RichEditorTextSpanOptions--><!--Device-unnamed-export declare interface RichEditorTextSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gesture

```TypeScript
gesture?: RichEditorGesture
```

行为触发回调。省略时，仅使用系统默认行为。

**Type:** [RichEditorGesture](../arkts-components/arkts-arkui-richeditorgesture-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextSpanOptions-gesture?: RichEditorGesture--><!--Device-RichEditorTextSpanOptions-gesture?: RichEditorGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: int
```

添加文本的位置。省略时，添加到所有内容的最后。

当值小于0时，放在所有内容最前面；当值大于所有内容长度时，放在所有内容最后面。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextSpanOptions-offset?: int--><!--Device-RichEditorTextSpanOptions-offset?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## paragraphStyle

```TypeScript
paragraphStyle?: RichEditorParagraphStyle
```

段落样式。

**Type:** [RichEditorParagraphStyle](arkts-arkui-richeditor-richeditorparagraphstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextSpanOptions-paragraphStyle?: RichEditorParagraphStyle--><!--Device-RichEditorTextSpanOptions-paragraphStyle?: RichEditorParagraphStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: RichEditorTextStyle
```

文本Span样式信息。

**Type:** [RichEditorTextStyle](../arkts-components/arkts-arkui-richeditortextstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextSpanOptions-style?: RichEditorTextStyle--><!--Device-RichEditorTextSpanOptions-style?: RichEditorTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## urlStyle

```TypeScript
urlStyle?: RichEditorUrlStyle
```

url信息。

默认值：undefined

**Type:** [RichEditorUrlStyle](../arkts-components/arkts-arkui-richeditorurlstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorTextSpanOptions-urlStyle?: RichEditorUrlStyle--><!--Device-RichEditorTextSpanOptions-urlStyle?: RichEditorUrlStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

