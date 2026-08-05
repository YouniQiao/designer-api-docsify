# TransitionHierarchyStrategy (System API)

Source and target are two matched elements during the geometry transition. The animation starts at the source and ends at the target. TransitionHierarchyStrategy enumeration defines how levels of source and target elements would be changed in the hierarchy during the geometry transition.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum TransitionHierarchyStrategy--><!--Device-unnamed-export declare enum TransitionHierarchyStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## NONE

```TypeScript
NONE = 0
```

None mode. Source and target staty in the original level in the hierarchy during geometry transition.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionHierarchyStrategy-NONE = 0--><!--Device-TransitionHierarchyStrategy-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## ADAPTIVE

```TypeScript
ADAPTIVE = 1
```

ADAPTIVE mode. Lower level one of source and target is elevated to higher level of both, indicating that two elements are in same high level.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TransitionHierarchyStrategy-ADAPTIVE = 1--><!--Device-TransitionHierarchyStrategy-ADAPTIVE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

