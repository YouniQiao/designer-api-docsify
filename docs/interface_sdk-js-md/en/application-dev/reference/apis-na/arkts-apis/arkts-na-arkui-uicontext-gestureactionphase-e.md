# GestureActionPhase

This is an enumeration type representing the gesture callback phases to be triggered, corresponding to the action callbacks defined in gesture.d.ts. Therefore, not all gesture types have all the following phase definitions. For example, SwipeGesture only has one callback named onAction, so it also only has one enumeration type, which is WILL_START.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export const enum GestureActionPhase--><!--Device-unnamed-export const enum GestureActionPhase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## WILL_START

```TypeScript
WILL_START = 0
```

The gesture has been successfully recognized by the system, and the action-start/action callback will be executed immediately.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureActionPhase-WILL_START = 0--><!--Device-GestureActionPhase-WILL_START = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## WILL_END

```TypeScript
WILL_END = 1
```

This indicates the gesture has been determined to be an end, which usually happens when the user lifts their fingers, ending the entire interaction, and the action-end callback will be executed immediately.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureActionPhase-WILL_END = 1--><!--Device-GestureActionPhase-WILL_END = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

