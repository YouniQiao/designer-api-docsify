# DraggingSizeChangeEffect

Define drag start animation effect from drag preview to the handle drag image

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum DraggingSizeChangeEffect--><!--Device-unnamed-export declare enum DraggingSizeChangeEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

Default effect, no transition.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DraggingSizeChangeEffect-DEFAULT = 0--><!--Device-DraggingSizeChangeEffect-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SIZE_TRANSITION

```TypeScript
SIZE_TRANSITION = 1
```

Only scaled transition, this parameter take effect when PREVIEW_MODE is not DISABLE_SCALE.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DraggingSizeChangeEffect-SIZE_TRANSITION = 1--><!--Device-DraggingSizeChangeEffect-SIZE_TRANSITION = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SIZE_CONTENT_TRANSITION

```TypeScript
SIZE_CONTENT_TRANSITION = 2
```

Scaled and content transition together, this size transition take effect when PREVIEW_MODE is not DISABLE_SCALE.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DraggingSizeChangeEffect-SIZE_CONTENT_TRANSITION = 2--><!--Device-DraggingSizeChangeEffect-SIZE_CONTENT_TRANSITION = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

