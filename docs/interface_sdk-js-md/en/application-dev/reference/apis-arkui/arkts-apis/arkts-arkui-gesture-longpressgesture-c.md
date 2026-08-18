# LongPressGesture

Defines LongPressGesture.

**Inheritance/Implementation:** LongPressGesture extends [Gesture](arkts-arkui-gesture-gesture-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class LongPressGesture--><!--Device-unnamed-export declare class LongPressGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => LongPressGesture, value?: LongPressGestureHandlerOptions): LongPressGesture
```

Set the value. fingers: Indicates the hand index that triggers the long press. repeat: Indicates whether to trigger event callback continuously. duration: Minimum press and hold time, in milliseconds.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressGesture-static $_instantiate(factory: () => LongPressGesture, value?: LongPressGestureHandlerOptions): LongPressGesture--><!--Device-LongPressGesture-static $_instantiate(factory: () => LongPressGesture, value?: LongPressGestureHandlerOptions): LongPressGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; LongPressGesture | Yes |  |
| value | [LongPressGestureHandlerOptions](arkts-arkui-gesture-longpressgesturehandleroptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [LongPressGesture](arkts-arkui-gesture-longpressgesture-c.md) |  |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): this
```

LongPress gesture recognition success callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressGesture-onAction(event: Callback<GestureEvent>): this--><!--Device-LongPressGesture-onAction(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): this
```

The LongPress gesture is successfully recognized and a callback is triggered when the touch cancel event is received.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressGesture-onActionCancel(event: Callback<GestureEvent>): this--><!--Device-LongPressGesture-onActionCancel(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onActionEnd

```TypeScript
onActionEnd(event: Callback<GestureEvent>): this
```

The LongPress gesture is successfully recognized. When the finger is lifted, the callback is triggered.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LongPressGesture-onActionEnd(event: Callback<GestureEvent>): this--><!--Device-LongPressGesture-onActionEnd(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

