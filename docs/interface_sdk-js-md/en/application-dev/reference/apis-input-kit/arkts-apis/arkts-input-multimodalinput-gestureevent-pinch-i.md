# Pinch

捏合手势事件。

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

捏合度，取值范围大于等于0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Pinch-scale: double--><!--Device-Pinch-scale: double-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

## type

```TypeScript
type: ActionType
```

手势事件类型。如：手势开始、手势更新、手势结束等。

**Type:** [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Pinch-type: ActionType--><!--Device-Pinch-type: ActionType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

