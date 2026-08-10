# SwipeGestureHandlerOptions

快滑手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。

**Inheritance/Implementation:** SwipeGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface SwipeGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-export interface SwipeGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: SwipeDirection
```

触发快滑手势的滑动方向。

默认值：SwipeDirection.All

**Type:** [SwipeDirection](arkts-arkui-gesture-swipedirection-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandlerOptions-direction?: SwipeDirection--><!--Device-SwipeGestureHandlerOptions-direction?: SwipeDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: int
```

触发快滑的最少手指数，默认为1，最小为1指，最大为10指。

默认值：1 

取值范围：[1, 10]

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandlerOptions-fingers?: int--><!--Device-SwipeGestureHandlerOptions-fingers?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## speed

```TypeScript
speed?: double
```

识别快滑的最小速度。

默认值：100VP/s 

**说明：**

当滑动速度的值小于等于0时，会被转化为默认值。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandlerOptions-speed?: double--><!--Device-SwipeGestureHandlerOptions-speed?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

