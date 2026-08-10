# TapGestureParameters

点击手势参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。

> **说明：**
> 
> 为规范匿名对象的定义，API 12版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Inheritance/Implementation:** TapGestureParameters extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface TapGestureParameters extends BaseHandlerOptions--><!--Device-unnamed-declare interface TapGestureParameters extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: number
```

识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值。

默认值：1

取值范围：[0, +∞)

**说明：**

1. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。2. 当上次点击的位置与当前点击的位置距离超过60vp时，手势识别失败。在多指情况下，点击的位置为所有参与手势响应手指的平均位置。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TapGestureParameters-count?: number--><!--Device-TapGestureParameters-count?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distanceThreshold

```TypeScript
distanceThreshold?: number
```

点击手势移动阈值。当设置的值小于等于0或不设置时，会被转化为默认值。

默认值：2^31-1

单位：vp

**说明：**

当手指的移动距离超出开发者预设的移动阈值时，点击识别失败。如果初始化为默认阈值时，手指移动超过组件热区范围，点击识别失败。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TapGestureParameters-distanceThreshold?: number--><!--Device-TapGestureParameters-distanceThreshold?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: number
```

触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值。

默认值：1

**说明：**

1. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败；手指抬起时，抬起后剩余的手指数小于阈值时开始计时，如300ms内未全部抬起则手势识别失败。2. 实际点击手指数超过配置值，手势识别成功。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TapGestureParameters-fingers?: number--><!--Device-TapGestureParameters-fingers?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

