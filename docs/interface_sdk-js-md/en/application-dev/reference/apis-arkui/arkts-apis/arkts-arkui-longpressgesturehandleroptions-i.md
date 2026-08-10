# LongPressGestureHandlerOptions

长按手势处理器配置参数。继承自[BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)。

**Inheritance/Implementation:** LongPressGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface LongPressGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-interface LongPressGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowableMovement

```TypeScript
allowableMovement?: number
```

长按手势识别器识别的手势的最大移动距离，单位为px。

默认值：15 

取值范围：(0, +∞)，设置小于等于0时，按照默认值15处理。

**Type:** number

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LongPressGestureHandlerOptions-allowableMovement?: number--><!--Device-LongPressGestureHandlerOptions-allowableMovement?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

触发长按的最短时间，单位为毫秒（ms）。

默认值：500 

**说明：**

取值范围：[0, +∞)，设置小于等于0时，按照默认值500处理。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LongPressGestureHandlerOptions-duration?: number--><!--Device-LongPressGestureHandlerOptions-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fingers

```TypeScript
fingers?: number
```

触发长按的最少手指数，最小为1指， 最大取值为10指。

默认值：1 

取值范围：[1, 10]

**说明：**

手指按下后若发生超过15px的移动，则判定当前长按手势识别失败。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LongPressGestureHandlerOptions-fingers?: number--><!--Device-LongPressGestureHandlerOptions-fingers?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## repeat

```TypeScript
repeat?: boolean
```

是否连续触发事件回调。true表示为连续触发事件回调，false表示不连续触发事件回调。

默认值：false

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LongPressGestureHandlerOptions-repeat?: boolean--><!--Device-LongPressGestureHandlerOptions-repeat?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

