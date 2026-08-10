# LongPressGestureHandlerOptions

长按手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。

**Inheritance/Implementation:** LongPressGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface LongPressGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-export interface LongPressGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowableMovement

```TypeScript
allowableMovement?: double
```

长按手势识别器识别的手势的最大移动距离，单位为px。

默认值：15 

取值范围：(0, +∞)，设置小于等于0时，按照默认值15处理。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressGestureHandlerOptions-allowableMovement?: double--><!--Device-LongPressGestureHandlerOptions-allowableMovement?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

触发长按的最短时间，单位为毫秒（ms）。

默认值：500 

**说明：**

取值范围：[0, +∞)，设置小于等于0时，按照默认值500处理。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressGestureHandlerOptions-duration?: int--><!--Device-LongPressGestureHandlerOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: int
```

触发长按的最少手指数，最小为1指， 最大取值为10指。

默认值：1 

取值范围：[1, 10]

**说明：**

手指按下后若发生超过15px的移动，则判定当前长按手势识别失败。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressGestureHandlerOptions-fingers?: int--><!--Device-LongPressGestureHandlerOptions-fingers?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## repeat

```TypeScript
repeat?: boolean
```

是否连续触发事件回调。true表示为连续触发事件回调，false表示不连续触发事件回调。

默认值：false

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressGestureHandlerOptions-repeat?: boolean--><!--Device-LongPressGestureHandlerOptions-repeat?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

