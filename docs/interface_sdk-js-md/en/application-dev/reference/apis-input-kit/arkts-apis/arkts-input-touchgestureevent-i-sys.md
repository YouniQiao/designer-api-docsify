# TouchGestureEvent (System API)

Defines a touchscreen gesture event.

**Since:** 18

<!--Device-unnamed-export declare interface TouchGestureEvent--><!--Device-unnamed-export declare interface TouchGestureEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { SwipeInward, FourFingersSwipe, Pinch, ActionType, Rotate, ThreeFingersTap, ThreeFingersSwipe, TouchGestureEvent } from '@kit.InputKit';
```

## action

```TypeScript
action: TouchGestureAction
```

Enumerates touchscreen gesture types.

**Type:** TouchGestureAction

**Since:** 18

<!--Device-TouchGestureEvent-action: TouchGestureAction--><!--Device-TouchGestureEvent-action: TouchGestureAction-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## touches

```TypeScript
touches: Touch[]
```

Touch point information.

**Type:** Touch[]

**Since:** 18

<!--Device-TouchGestureEvent-touches: Touch[]--><!--Device-TouchGestureEvent-touches: Touch[]-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

