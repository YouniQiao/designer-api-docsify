# GestureGroupGestureHandlerOptions

Provides the parameters of the gesture group handler.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-interface GestureGroupGestureHandlerOptions--><!--Device-unnamed-interface GestureGroupGestureHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gestures

```TypeScript
gestures: GestureHandler<TapGestureHandler | LongPressGestureHandler | PanGestureHandler | SwipeGestureHandler | PinchGestureHandler | RotationGestureHandler | GestureGroupHandler>[]
```

Gestures to be included in a gesture group. **NOTE：**To add both single-tap and double-tap gestures for a component, add two [TapGesture](arkts-arkui-gesture-con.md#TapGesture) instances as the [combined gestures](arkts-arkui-gesture-con.md#GestureGroup), with the double-tap gesture preceding the single-tap gesture. The gestures will not work correctly if this order is reversed.

**Type:** [GestureHandler](arkts-arkui-gesturehandler-c.md)&lt;[TapGestureHandler](arkts-arkui-tapgesturehandler-c.md) \| [LongPressGestureHandler](arkts-arkui-longpressgesturehandler-c.md) \| [PanGestureHandler](arkts-arkui-pangesturehandler-c.md) \| [SwipeGestureHandler](arkts-arkui-swipegesturehandler-c.md) \| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) \| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) \| [GestureGroupHandler](arkts-arkui-gesturegrouphandler-c.md)&gt;[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureGroupGestureHandlerOptions-gestures: GestureHandler<TapGestureHandler | LongPressGestureHandler | PanGestureHandler | SwipeGestureHandler | PinchGestureHandler | RotationGestureHandler | GestureGroupHandler>[]--><!--Device-GestureGroupGestureHandlerOptions-gestures: GestureHandler<TapGestureHandler | LongPressGestureHandler | PanGestureHandler | SwipeGestureHandler | PinchGestureHandler | RotationGestureHandler | GestureGroupHandler>[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode: GestureMode
```

Recognition mode of combined gestures. Default value: **GestureMode.Sequence**

**Type:** [GestureMode](arkts-arkui-gesturemode-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureGroupGestureHandlerOptions-mode: GestureMode--><!--Device-GestureGroupGestureHandlerOptions-mode: GestureMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

