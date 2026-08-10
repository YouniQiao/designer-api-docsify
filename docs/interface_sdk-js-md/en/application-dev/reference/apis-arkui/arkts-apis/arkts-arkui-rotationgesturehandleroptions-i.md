# RotationGestureHandlerOptions

旋转手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。

**Inheritance/Implementation:** RotationGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface RotationGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-interface RotationGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## angle

```TypeScript
angle?: number
```

触发旋转手势的最小改变度数，单位为deg。

默认值：1 

**说明：**

当改变度数的值小于等于0或大于360时，会被转化为默认值。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandlerOptions-angle?: number--><!--Device-RotationGestureHandlerOptions-angle?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: number
```

触发旋转的最少手指数，最小为2指，最大为5指。

默认值：2 

取值范围：[2, 5]

触发手势时手指数量可以多于fingers参数值，但仅最先落下的两指参与手势计算。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandlerOptions-fingers?: number--><!--Device-RotationGestureHandlerOptions-fingers?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

