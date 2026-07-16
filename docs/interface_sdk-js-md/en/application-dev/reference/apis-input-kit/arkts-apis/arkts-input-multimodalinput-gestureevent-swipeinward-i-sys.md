# SwipeInward (System API)

Defines an inward swipe event.

**Since:** 12

<!--Device-unnamed-export declare interface SwipeInward--><!--Device-unnamed-export declare interface SwipeInward-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { SwipeInward, FourFingersSwipe, Pinch, ActionType, Rotate, ThreeFingersTap, ThreeFingersSwipe, TouchGestureEvent } from '@kit.InputKit';
```

## type

```TypeScript
type: ActionType
```

Type of the inward swipe event. The value is fixed at **SwipeInward**.

**Type:** ActionType

**Since:** 12

<!--Device-SwipeInward-type: ActionType--><!--Device-SwipeInward-type: ActionType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## x

```TypeScript
x: number
```

X-coordinate of the swipe event trigger point, in pixels.

**Type:** number

**Since:** 12

<!--Device-SwipeInward-x: int--><!--Device-SwipeInward-x: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## y

```TypeScript
y: number
```

Y-coordinate of the swipe event trigger point, in pixels.

**Type:** number

**Since:** 12

<!--Device-SwipeInward-y: int--><!--Device-SwipeInward-y: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

