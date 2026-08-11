# Rotate

Defines a rotation gesture event.

**Since:** 11

<!--Device-unnamed-export declare interface Rotate--><!--Device-unnamed-export declare interface Rotate-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { SwipeInward, FourFingersSwipe, Pinch, ActionType, Rotate, ThreeFingersTap, ThreeFingersSwipe, TouchGestureEvent } from 'kits/@kit.InputKit';
```

## angle

```TypeScript
angle: number
```

Rotation angle, in degrees.

**Type:** number

**Since:** 11

<!--Device-Rotate-angle: double--><!--Device-Rotate-angle: double-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## type

```TypeScript
type: ActionType
```

Gesture event type, for example, gesture start, gesture update, or gesture end.

**Type:** [ActionType](../../apis-data-protection-kit/arkts-apis/arkts-dataprotection-dlppermission-actiontype-e.md)

**Since:** 11

<!--Device-Rotate-type: ActionType--><!--Device-Rotate-type: ActionType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core
