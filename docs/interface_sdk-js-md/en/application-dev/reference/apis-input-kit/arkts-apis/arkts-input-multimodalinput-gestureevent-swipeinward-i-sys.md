# SwipeInward (System API)

向内滑动事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface SwipeInward--><!--Device-unnamed-export declare interface SwipeInward-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { SwipeInward, FourFingersSwipe, Pinch, ActionType, Rotate, ThreeFingersTap, ThreeFingersSwipe, TouchGestureEvent } from 'kits/@kit.InputKit';
```

## type

```TypeScript
type: ActionType
```

表示向内滑动事件的类型，固定为SwipeInward。

**Type:** [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SwipeInward-type: ActionType--><!--Device-SwipeInward-type: ActionType-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## x

```TypeScript
x: int
```

滑动事件触发点的横坐标，单位为像素。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SwipeInward-x: int--><!--Device-SwipeInward-x: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## y

```TypeScript
y: int
```

滑动事件触发点的纵坐标，单位为像素。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SwipeInward-y: int--><!--Device-SwipeInward-y: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

