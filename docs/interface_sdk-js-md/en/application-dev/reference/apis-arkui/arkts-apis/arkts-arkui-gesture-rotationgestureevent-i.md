# RotationGestureEvent

继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](arkts-arkui-common-commonmethod-i.md#ongesturejudgebegin)的event参数来传递。

**Inheritance/Implementation:** RotationGestureEvent extends [BaseGestureEvent](arkts-arkui-basegestureevent-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface RotationGestureEvent extends BaseGestureEvent--><!--Device-unnamed-export interface RotationGestureEvent extends BaseGestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angle

```TypeScript
angle: double
```

表示旋转角度，单位为deg。

**说明：**

角度计算方式：当滑动手势被识别后，连接两根手指之间的线被识别为起始线条。随着手指的滑动，手指之间的线条会发生旋转。根据起始线条和当前线条两端点的坐标，使用反正切函数分别计算其相对于水平方向的夹角。

最终的旋转角度为：arctan2(cy2-cy1, cx2-cx1) - arctan2(y2-y1, x2-x1) 

在起始线条为坐标系的情况下，顺时针旋转为0到180度，逆时针旋转为0到-180度。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGestureEvent-angle: double--><!--Device-RotationGestureEvent-angle: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

