# GestureGroupGestureHandlerOptions

Provides the parameters of the gesture group handler.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface GestureGroupGestureHandlerOptions--><!--Device-unnamed-interface GestureGroupGestureHandlerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## gestures

```TypeScript
gestures: GestureHandler<TapGestureHandler | LongPressGestureHandler | PanGestureHandler | SwipeGestureHandler | PinchGestureHandler | RotationGestureHandler | GestureGroupHandler>[]
```

Gestures to be included in a gesture group. **NOTE** To add both single-tap and double-tap gestures for a component, add two [TapGesture]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ instances as the [combined gestures]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, with the double-tap gesture preceding the single-tap gesture. The gestures will not work correctly if this order is reversed.

**Type:** GestureHandler&lt;TapGestureHandler \| LongPressGestureHandler \| PanGestureHandler \| SwipeGestureHandler \| PinchGestureHandler \| RotationGestureHandler \| GestureGroupHandler&gt;[]

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

Recognition mode of combined gestures. Default value: **GestureMode.Sequence**

**Type:** GestureMode

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GestureGroupGestureHandlerOptions-mode: GestureMode--><!--Device-GestureGroupGestureHandlerOptions-mode: GestureMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

