# TouchGestureEvent (System API)

Defines a touchscreen gesture event.

**Since:** 23

<!--Device-unnamed-export declare interface TouchGestureEvent--><!--Device-unnamed-export declare interface TouchGestureEvent-End-->

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

## action

```TypeScript
action: TouchGestureAction
```

Enumerates touchscreen gesture types.

**Type:** [TouchGestureAction](arkts-input-multimodalinput-gestureevent-touchgestureaction-e-sys.md)

**Since:** 23

<!--Device-TouchGestureEvent-action: TouchGestureAction--><!--Device-TouchGestureEvent-action: TouchGestureAction-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## touches

```TypeScript
touches: Touch[]
```

Touch point information.

**Type:** [Touch](arkts-input-multimodalinput-touchevent-touch-i.md)[]

**Since:** 23

<!--Device-TouchGestureEvent-touches: Touch[]--><!--Device-TouchGestureEvent-touches: Touch[]-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

