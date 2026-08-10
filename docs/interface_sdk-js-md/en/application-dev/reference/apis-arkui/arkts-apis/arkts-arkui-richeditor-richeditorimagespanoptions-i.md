# RichEditorImageSpanOptions

设置图片的偏移位置和图片样式信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RichEditorImageSpanOptions--><!--Device-unnamed-export declare interface RichEditorImageSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHover

```TypeScript
onHover?: OnHoverCallback
```

鼠标悬停触发回调。省略时，不执行相关行为。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorImageSpanOptions-onHover?: OnHoverCallback--><!--Device-RichEditorImageSpanOptions-onHover?: OnHoverCallback-End-->

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

<!--Device-RichEditorImageSpanOptions-gesture?: RichEditorGesture--><!--Device-RichEditorImageSpanOptions-gesture?: RichEditorGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageStyle

```TypeScript
imageStyle?: RichEditorImageSpanStyle
```

图片样式。

**Type:** [RichEditorImageSpanStyle](../arkts-components/arkts-arkui-richeditorimagespanstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorImageSpanOptions-imageStyle?: RichEditorImageSpanStyle--><!--Device-RichEditorImageSpanOptions-imageStyle?: RichEditorImageSpanStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: int
```

添加图片的位置。省略时，添加到所有内容的末尾。

当值小于0时，设置在所有内容最前面；当值大于所有内容长度时，设置在所有内容最后面。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorImageSpanOptions-offset?: int--><!--Device-RichEditorImageSpanOptions-offset?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

