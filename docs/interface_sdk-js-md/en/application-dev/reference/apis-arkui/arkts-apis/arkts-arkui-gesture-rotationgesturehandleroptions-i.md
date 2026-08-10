# RotationGestureHandlerOptions

旋转手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。

**Inheritance/Implementation:** RotationGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface RotationGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-export interface RotationGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angle

```TypeScript
angle?: double
```

触发旋转手势的最小改变度数，单位为deg。

默认值：1 

**说明：**

当改变度数的值小于等于0或大于360时，会被转化为默认值。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGestureHandlerOptions-angle?: double--><!--Device-RotationGestureHandlerOptions-angle?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: int
```

触发旋转的最少手指数，最小为2指，最大为5指。

默认值：2 

取值范围：[2, 5]

触发手势时手指数量可以多于fingers参数值，但仅最先落下的两指参与手势计算。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGestureHandlerOptions-fingers?: int--><!--Device-RotationGestureHandlerOptions-fingers?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

