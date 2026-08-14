# Pinch

Defines a pinch event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface Pinch--><!--Device-unnamed-export declare interface Pinch-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

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

## scale

```TypeScript
scale: double
```

Pinch scale factor. The value is greater than or equal to 0.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Pinch-scale: double--><!--Device-Pinch-scale: double-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## type

```TypeScript
type: ActionType
```

Gesture event type, for example, gesture start, gesture update, or gesture end.

**Type:** [ActionType](arkts-input-multimodalinput-gestureevent-actiontype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Pinch-type: ActionType--><!--Device-Pinch-type: ActionType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

