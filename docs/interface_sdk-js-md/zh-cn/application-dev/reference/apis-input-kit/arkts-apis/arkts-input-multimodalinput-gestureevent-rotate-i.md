# Rotate

旋转手势事件。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface Rotate--><!--Device-unnamed-export declare interface Rotate-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Core

## 导入模块

```TypeScript
import { SwipeInward, FourFingersSwipe, Pinch, ActionType, Rotate, ThreeFingersTap, ThreeFingersSwipe, TouchGestureEvent } from 'kits/@kit.InputKit';
```

## angle

```TypeScript
angle: double
```

旋转角度，单位为度。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-Rotate-angle: double--><!--Device-Rotate-angle: double-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Core

## type

```TypeScript
type: ActionType
```

手势事件类型。如：手势开始、手势更新、手势结束等。

**类型：** [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-Rotate-type: ActionType--><!--Device-Rotate-type: ActionType-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Core

