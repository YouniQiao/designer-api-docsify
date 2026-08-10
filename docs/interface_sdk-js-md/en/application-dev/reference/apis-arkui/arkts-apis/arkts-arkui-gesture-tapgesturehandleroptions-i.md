# TapGestureHandlerOptions

点击手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。

**Inheritance/Implementation:** TapGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface TapGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-export interface TapGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: int
```

识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值。

默认值：1

取值范围：[0, +∞)

**说明：**

1. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。2. 当上次点击的位置与当前点击的位置距离超过60vp时，手势识别失败。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandlerOptions-count?: int--><!--Device-TapGestureHandlerOptions-count?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distanceThreshold

```TypeScript
distanceThreshold?: double
```

点击手势移动阈值。当设置的值小于等于0或不设置时，会被转化为默认值。

默认值：2^31-1

单位：vp

**说明：**

当手指的移动距离超出开发者预设的移动阈值时，点击识别失败。如果初始化为默认阈值时，手指移动超过组件热区范围，点击识别失败。

**Type:** double

**Default:** Infinity

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandlerOptions-distanceThreshold?: double--><!--Device-TapGestureHandlerOptions-distanceThreshold?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: int
```

触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值。

默认值：1

**说明：**

1. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败，第一根手指抬起后300毫秒内未有足够的手指抬起，手势识别失败。2. 实际点击手指数超过配置值，手势识别成功。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandlerOptions-fingers?: int--><!--Device-TapGestureHandlerOptions-fingers?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

