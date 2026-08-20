# BlendApplyType

Enum for BlendApplyType. Indicate how to apply specified blend mode to the view's content.

@enum { number }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum BlendApplyType--><!--Device-unnamed-export declare enum BlendApplyType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FAST

```TypeScript
FAST = 0
```

The content of the view is blended in sequence on the target image.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlendApplyType-FAST = 0--><!--Device-BlendApplyType-FAST = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OFFSCREEN

```TypeScript
OFFSCREEN = 1
```

The content of the component and its child components are drawn on the offscreen canvas, and then blended with the existing content on the canvas.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlendApplyType-OFFSCREEN = 1--><!--Device-BlendApplyType-OFFSCREEN = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

