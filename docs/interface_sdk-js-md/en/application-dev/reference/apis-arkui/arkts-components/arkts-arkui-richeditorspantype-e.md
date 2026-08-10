# RichEditorSpanType

Span类型信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare enum RichEditorSpanType--><!--Device-unnamed-declare enum RichEditorSpanType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TEXT

```TypeScript
TEXT = 0
```

Span类型为文字。 

 

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorSpanType-TEXT = 0--><!--Device-RichEditorSpanType-TEXT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IMAGE

```TypeScript
IMAGE = 1
```

Span类型为图像。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorSpanType-IMAGE = 1--><!--Device-RichEditorSpanType-IMAGE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MIXED

```TypeScript
MIXED = 2
```

Span类型为图文混合。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorSpanType-MIXED = 2--><!--Device-RichEditorSpanType-MIXED = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BUILDER

```TypeScript
BUILDER = 3
```

Span类型为BuilderSpan。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorSpanType-BUILDER = 3--><!--Device-RichEditorSpanType-BUILDER = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 4
```

注册此类型的菜单，但未注册TEXT、IMAGE、MIXED、BUILDER菜单时，文字类型、图像类型、图文混合类型、BuilderSpan类型都会触发并显示此类型对应的菜单。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-RichEditorSpanType-DEFAULT = 4--><!--Device-RichEditorSpanType-DEFAULT = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

