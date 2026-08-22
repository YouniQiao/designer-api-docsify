# RotationGestureHandlerOptions

Defines the RotationGestureHandler options.

@extends BaseHandlerOptions @interface RotationGestureHandlerOptions

**Inheritance/Implementation:** RotationGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-gesture-basehandleroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RotationGestureHandlerOptions--><!--Device-unnamed-export interface RotationGestureHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angle

```TypeScript
angle?: double
```

Indicates minimum rotate angle. The default value is 1deg.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGestureHandlerOptions-angle?: double--><!--Device-RotationGestureHandlerOptions-angle?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: int
```

Indicates the hand index that triggers the rotation. If the value is less than 1, the default value is used. The default value is 1.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGestureHandlerOptions-fingers?: int--><!--Device-RotationGestureHandlerOptions-fingers?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

