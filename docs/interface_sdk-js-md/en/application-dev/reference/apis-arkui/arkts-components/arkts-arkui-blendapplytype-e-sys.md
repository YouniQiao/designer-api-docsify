# BlendApplyType

指示如何将指定的混合模式应用于视图的内容。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare enum BlendApplyType--><!--Device-unnamed-declare enum BlendApplyType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OFFSCREEN_WITH_BACKGROUND

```TypeScript
OFFSCREEN_WITH_BACKGROUND = 2
```

创建离屏画布时，先拷贝一份背景初始化画布，再将此组件和子组件内容绘制到离屏画布上，然后整体进行混合。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-BlendApplyType-OFFSCREEN_WITH_BACKGROUND = 2--><!--Device-BlendApplyType-OFFSCREEN_WITH_BACKGROUND = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

