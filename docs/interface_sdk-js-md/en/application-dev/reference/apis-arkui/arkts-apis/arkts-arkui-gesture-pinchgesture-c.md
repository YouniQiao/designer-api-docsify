# PinchGesture

Defines PinchGesture.

**Inheritance/Implementation:** PinchGesture extends [Gesture](arkts-arkui-gesture-gesture-c.md#gesture)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class PinchGesture--><!--Device-unnamed-export declare class PinchGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => PinchGesture, value?: PinchGestureHandlerOptions): PinchGesture
```

Set the value.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGesture-static $_instantiate(factory: () => PinchGesture, value?: PinchGestureHandlerOptions): PinchGesture--><!--Device-PinchGesture-static $_instantiate(factory: () => PinchGesture, value?: PinchGestureHandlerOptions): PinchGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; PinchGesture | Yes |  |
| value | [PinchGestureHandlerOptions](arkts-arkui-gesture-pinchgesturehandleroptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [PinchGesture](arkts-arkui-gesture-pinchgesture-c.md) |  |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): this
```

The Pinch gesture is successfully recognized and a callback is triggered when the touch cancel event is received.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGesture-onActionCancel(event: Callback<GestureEvent>): this--><!--Device-PinchGesture-onActionCancel(event: Callback<GestureEvent>): this-End-->

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

The Pinch gesture is successfully recognized. When the finger is lifted, the callback is triggered.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGesture-onActionEnd(event: Callback<GestureEvent>): this--><!--Device-PinchGesture-onActionEnd(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onActionStart

```TypeScript
onActionStart(event: Callback<GestureEvent>): this
```

Pinch gesture recognition success callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGesture-onActionStart(event: Callback<GestureEvent>): this--><!--Device-PinchGesture-onActionStart(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onActionUpdate

```TypeScript
onActionUpdate(event: Callback<GestureEvent>): this
```

Callback when the Pinch gesture is moving.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGesture-onActionUpdate(event: Callback<GestureEvent>): this--><!--Device-PinchGesture-onActionUpdate(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

