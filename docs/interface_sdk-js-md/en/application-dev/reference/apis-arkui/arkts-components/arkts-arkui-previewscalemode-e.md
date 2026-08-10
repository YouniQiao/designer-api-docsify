# PreviewScaleMode

预览图的缩放方式。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare enum PreviewScaleMode--><!--Device-unnamed-declare enum PreviewScaleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 0
```

预览图根据[Placement](../arkts-apis/arkts-arkui-enums-placement-e.md/arkts-arkui-enums-placement-e.md)自动调整预览图宽高及缩放。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PreviewScaleMode-AUTO = 0--><!--Device-PreviewScaleMode-AUTO = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CONSTANT

```TypeScript
CONSTANT = 1
```

预览图不缩放，大小保持不变。最终仍会受到安全区的限制而出现压缩、裁剪。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PreviewScaleMode-CONSTANT = 1--><!--Device-PreviewScaleMode-CONSTANT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MAINTAIN

```TypeScript
MAINTAIN = 2
```

预览图缩放时保持宽高比。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PreviewScaleMode-MAINTAIN = 2--><!--Device-PreviewScaleMode-MAINTAIN = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

