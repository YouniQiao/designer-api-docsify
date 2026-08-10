# PinchGestureHandlerOptions

捏合手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。

**Inheritance/Implementation:** PinchGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface PinchGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-export interface PinchGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distance

```TypeScript
distance?: double
```

最小识别距离，单位为vp。

默认值：5 

**说明：**

当识别距离的值小于等于0时，会被转化为默认值。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGestureHandlerOptions-distance?: double--><!--Device-PinchGestureHandlerOptions-distance?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: int
```

触发捏合的最少手指数，最小为2指，最大为5指。

默认值：2 

取值范围：[2, 5]

触发手势手指可以多于fingers数目，但只有先落下的与fingers相同数目的手指参与手势计算。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGestureHandlerOptions-fingers?: int--><!--Device-PinchGestureHandlerOptions-fingers?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

