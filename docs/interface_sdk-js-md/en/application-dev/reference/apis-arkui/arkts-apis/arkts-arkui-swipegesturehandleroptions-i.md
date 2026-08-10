# SwipeGestureHandlerOptions

快滑手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。

**Inheritance/Implementation:** SwipeGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface SwipeGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-interface SwipeGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: SwipeDirection
```

触发快滑手势的滑动方向。

默认值：SwipeDirection.All

**Type:** [SwipeDirection](arkts-arkui-gesture-swipedirection-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeGestureHandlerOptions-direction?: SwipeDirection--><!--Device-SwipeGestureHandlerOptions-direction?: SwipeDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: number
```

触发快滑的最少手指数，默认为1，最小为1指，最大为10指。

默认值：1 

取值范围：[1, 10]

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeGestureHandlerOptions-fingers?: number--><!--Device-SwipeGestureHandlerOptions-fingers?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## speed

```TypeScript
speed?: number
```

识别快滑的最小速度。

默认值：100VP/s 

**说明：**

当滑动速度的值小于等于0时，会被转化为默认值。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeGestureHandlerOptions-speed?: number--><!--Device-SwipeGestureHandlerOptions-speed?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

