# Pinch

Defines a pinch event.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface Pinch--><!--Device-unnamed-export declare interface Pinch-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## Modules to Import

```TypeScript
import { SwipeInward, FourFingersSwipe, Pinch, ActionType, Rotate, ThreeFingersTap, ThreeFingersSwipe, TouchGestureEvent } from 'kits/@kit.InputKit';
```

## scale

```TypeScript
scale: double
```

Pinch scale factor. The value is greater than or equal to 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Pinch-scale: double--><!--Device-Pinch-scale: double-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## type

```TypeScript
type: ActionType
```

Gesture event type, for example, gesture start, gesture update, or gesture end.

**Type:** [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Pinch-type: ActionType--><!--Device-Pinch-type: ActionType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

