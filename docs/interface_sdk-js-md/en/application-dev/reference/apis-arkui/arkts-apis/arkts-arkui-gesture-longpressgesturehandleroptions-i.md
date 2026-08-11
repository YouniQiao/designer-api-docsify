# LongPressGestureHandlerOptions

Defines the LongPressGestureHandler options.

**Inheritance/Implementation:** LongPressGestureHandlerOptions extends [BaseHandlerOptions](arkts-arkui-basehandleroptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface LongPressGestureHandlerOptions extends BaseHandlerOptions--><!--Device-unnamed-export interface LongPressGestureHandlerOptions extends BaseHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowableMovement

```TypeScript
allowableMovement?: double
```

Indicates maximum moving distance, in px.The default value is 15px.

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

Indicates minimum press and hold time, in milliseconds.The default value is 500ms.

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

Indicates the hand index that triggers the long press. If the value is less than 1, the default value is used.The default value is 1.

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

Indicates whether an event is triggered repeatedly.The default value is false.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressGestureHandlerOptions-repeat?: boolean--><!--Device-LongPressGestureHandlerOptions-repeat?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

