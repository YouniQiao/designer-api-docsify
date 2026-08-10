# SwipeGestureEvent

继承自[BaseGestureEvent](arkts-arkui-basegestureevent-i.md)。可将该对象作为[onGestureJudgeBegin](arkts-arkui-common-commonmethod-i.md#ongesturejudgebegin)的event参数来传递。

**Inheritance/Implementation:** SwipeGestureEvent extends [BaseGestureEvent](arkts-arkui-basegestureevent-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface SwipeGestureEvent extends BaseGestureEvent--><!--Device-unnamed-export interface SwipeGestureEvent extends BaseGestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angle

```TypeScript
angle: double
```

表示快滑手势的角度，即手指滑动的瞬时方向与水平正方向的夹角，单位为deg。

**说明：**

以水平正方向为基准，滑动方向位于水平正方向顺时针侧时，角度范围为0到180度；位于水平正方向逆时针侧时，角度范围为0到-180度。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureEvent-angle: double--><!--Device-SwipeGestureEvent-angle: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## speed

```TypeScript
speed: double
```

快滑手势速度，即所有手指相对当前组件元素原始区域滑动的平均速度，单位为vp/s。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureEvent-speed: double--><!--Device-SwipeGestureEvent-speed: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

