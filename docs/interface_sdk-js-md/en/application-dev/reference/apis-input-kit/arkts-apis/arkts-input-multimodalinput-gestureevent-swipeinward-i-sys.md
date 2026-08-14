# SwipeInward (System API)

Defines an inward swipe event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface SwipeInward--><!--Device-unnamed-export declare interface SwipeInward-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { ActionType } from 'ActionType';
import { FourFingersSwipe } from 'FourFingersSwipe';
import { Pinch } from 'Pinch';
import { Rotate } from 'Rotate';
import { ThreeFingersSwipe } from 'ThreeFingersSwipe';
import { ThreeFingersTap } from 'ThreeFingersTap';
import { SwipeInward } from 'SwipeInward';
import { TouchGestureEvent } from 'TouchGestureEvent';
```

## type

```TypeScript
type: ActionType
```

Type of the inward swipe event. The value is fixed at **SwipeInward**.

**Type:** [ActionType](arkts-input-multimodalinput-gestureevent-actiontype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SwipeInward-type: ActionType--><!--Device-SwipeInward-type: ActionType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## x

```TypeScript
x: int
```

X-coordinate of the swipe event trigger point, in pixels.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SwipeInward-x: int--><!--Device-SwipeInward-x: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## y

```TypeScript
y: int
```

Y-coordinate of the swipe event trigger point, in pixels.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-SwipeInward-y: int--><!--Device-SwipeInward-y: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

