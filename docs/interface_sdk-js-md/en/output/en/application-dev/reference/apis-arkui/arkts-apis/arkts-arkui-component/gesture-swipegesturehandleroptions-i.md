# SwipeGestureHandlerOptions

Defines the SwipeGestureHandler options.

**Inheritance/Implementation:** SwipeGestureHandlerOptions extends [BaseHandlerOptions](gesture-basehandleroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface SwipeGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-export interface SwipeGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: SwipeDirection
```

Indicates the move direction of the swipe gesture. The default value is SwipeDirection.All.

**Type:** SwipeDirection

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandlerOptions-direction?: SwipeDirection--><!--Device-SwipeGestureHandlerOptions-direction?: SwipeDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: int
```

Indicates the hand index that triggers the swipe. If the value is less than 1, the default value is used. The default value is 1.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandlerOptions-fingers?: int--><!--Device-SwipeGestureHandlerOptions-fingers?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## speed

```TypeScript
speed?: double
```

Indicates minimum move speed. The default value is 100vp/s.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandlerOptions-speed?: double--><!--Device-SwipeGestureHandlerOptions-speed?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

