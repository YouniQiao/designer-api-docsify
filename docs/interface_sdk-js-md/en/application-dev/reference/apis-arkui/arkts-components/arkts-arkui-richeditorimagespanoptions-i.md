# RichEditorImageSpanOptions

Sets the offset and style of an image span.

**Since:** 10

<!--Device-unnamed-declare interface RichEditorImageSpanOptions--><!--Device-unnamed-declare interface RichEditorImageSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gesture

```TypeScript
gesture?: RichEditorGesture
```

Behavior-triggered callback. If this parameter is left empty, only the default system behavior is supported.

**Type:** RichEditorGesture

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorImageSpanOptions-gesture?: RichEditorGesture--><!--Device-RichEditorImageSpanOptions-gesture?: RichEditorGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageStyle

```TypeScript
imageStyle?: RichEditorImageSpanStyle
```

Image style.

**Type:** RichEditorImageSpanStyle

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanOptions-imageStyle?: RichEditorImageSpanStyle--><!--Device-RichEditorImageSpanOptions-imageStyle?: RichEditorImageSpanStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: number
```

Position of the image span to be added. If this parameter is omitted, the span is added to the end of all content.

If the value specified is less than 0, the span is placed at the beginning of all content. If the value is greater than the length of all content, the span is placed at the end of all content.

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanOptions-offset?: number--><!--Device-RichEditorImageSpanOptions-offset?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHover

```TypeScript
onHover?: OnHoverCallback
```

Callback triggered on mouse hover. If this parameter is omitted, no corresponding action is taken.

**Type:** OnHoverCallback

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-RichEditorImageSpanOptions-onHover?: OnHoverCallback--><!--Device-RichEditorImageSpanOptions-onHover?: OnHoverCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

