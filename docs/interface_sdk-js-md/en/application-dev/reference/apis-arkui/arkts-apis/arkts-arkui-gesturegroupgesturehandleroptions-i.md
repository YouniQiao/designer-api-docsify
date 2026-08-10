# GestureGroupGestureHandlerOptions

手势组处理器配置参数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface GestureGroupGestureHandlerOptions--><!--Device-unnamed-interface GestureGroupGestureHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gestures

```TypeScript
gestures: GestureHandler<TapGestureHandler | LongPressGestureHandler | PanGestureHandler | SwipeGestureHandler | PinchGestureHandler | RotationGestureHandler | GestureGroupHandler>[]
```

设置手势组中需要包含的手势集合。

**说明：**

当需要为一个组件同时添加单击和双击手势时，可在[GestureGroup](arkts-arkui-gesture-con.md#gesturegroup)中添加两个[TapGesture](arkts-arkui-gesture-con.md#tapgesture)，需要双击手势在前，单击手势在后，否则不生效。

**Type:** [GestureHandler](arkts-arkui-gesturehandler-c.md)&lt;TapGestureHandler \| LongPressGestureHandler \| PanGestureHandler \| SwipeGestureHandler \| PinchGestureHandler \| RotationGestureHandler \| GestureGroupHandler&gt;[]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureGroupGestureHandlerOptions-gestures: GestureHandler<TapGestureHandler | LongPressGestureHandler | PanGestureHandler | SwipeGestureHandler | PinchGestureHandler | RotationGestureHandler | GestureGroupHandler>[]--><!--Device-GestureGroupGestureHandlerOptions-gestures: GestureHandler<TapGestureHandler | LongPressGestureHandler | PanGestureHandler | SwipeGestureHandler | PinchGestureHandler | RotationGestureHandler | GestureGroupHandler>[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode: GestureMode
```

设置组合手势识别模式。

默认值：GestureMode.Sequence

**Type:** [GestureMode](arkts-arkui-gesture-gesturemode-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureGroupGestureHandlerOptions-mode: GestureMode--><!--Device-GestureGroupGestureHandlerOptions-mode: GestureMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

