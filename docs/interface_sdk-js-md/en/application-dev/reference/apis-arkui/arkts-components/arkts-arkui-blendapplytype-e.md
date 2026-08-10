# BlendApplyType

指示如何将指定的混合模式应用于视图的内容。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare enum BlendApplyType--><!--Device-unnamed-declare enum BlendApplyType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FAST

```TypeScript
FAST = 0
```

在目标图像上按顺序混合视图的内容。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BlendApplyType-FAST = 0--><!--Device-BlendApplyType-FAST = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OFFSCREEN

```TypeScript
OFFSCREEN = 1
```

将此组件和子组件内容绘制到离屏画布上，然后整体进行混合。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BlendApplyType-OFFSCREEN = 1--><!--Device-BlendApplyType-OFFSCREEN = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

