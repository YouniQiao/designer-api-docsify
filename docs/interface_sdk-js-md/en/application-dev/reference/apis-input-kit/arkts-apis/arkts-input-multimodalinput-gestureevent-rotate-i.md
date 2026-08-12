# Rotate

Defines a rotation gesture event.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface Rotate--><!--Device-unnamed-export declare interface Rotate-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { SwipeInward, FourFingersSwipe, Pinch, ActionType, Rotate, ThreeFingersTap, ThreeFingersSwipe, TouchGestureEvent } from '@kit.InputKit';
```

## angle

```TypeScript
angle: double
```

Rotation angle, in degrees.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Rotate-angle: double--><!--Device-Rotate-angle: double-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## type

```TypeScript
type: ActionType
```

Gesture event type, for example, gesture start, gesture update, or gesture end.

**Type:** [ActionType](arkts-input-multimodalinput-gestureevent-actiontype-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Rotate-type: ActionType--><!--Device-Rotate-type: ActionType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

