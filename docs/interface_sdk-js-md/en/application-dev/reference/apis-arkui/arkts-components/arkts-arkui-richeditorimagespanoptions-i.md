# RichEditorImageSpanOptions

设置图片的偏移位置和图片样式信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface RichEditorImageSpanOptions--><!--Device-unnamed-declare interface RichEditorImageSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHover

```TypeScript
onHover?: OnHoverCallback
```

鼠标悬停触发回调。省略时，不执行鼠标悬停回调行为。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-RichEditorImageSpanOptions-onHover?: OnHoverCallback--><!--Device-RichEditorImageSpanOptions-onHover?: OnHoverCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gesture

```TypeScript
gesture?: RichEditorGesture
```

行为触发回调。省略时，仅使用系统默认行为。

**Type:** [RichEditorGesture](arkts-arkui-richeditorgesture-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorImageSpanOptions-gesture?: RichEditorGesture--><!--Device-RichEditorImageSpanOptions-gesture?: RichEditorGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageStyle

```TypeScript
imageStyle?: RichEditorImageSpanStyle
```

图片样式信息。当需要自定义图片的大小、垂直对齐方式、缩放类型等样式时传入此参数；省略时，使用系统默认图片样式。

**Type:** [RichEditorImageSpanStyle](arkts-arkui-richeditorimagespanstyle-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanOptions-imageStyle?: RichEditorImageSpanStyle--><!--Device-RichEditorImageSpanOptions-imageStyle?: RichEditorImageSpanStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: number
```

添加图片的位置。省略时，添加到所有内容的末尾。

当值小于0时，设置在所有内容最前面；当值大于所有内容长度时，设置在所有内容最后面。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanOptions-offset?: number--><!--Device-RichEditorImageSpanOptions-offset?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

