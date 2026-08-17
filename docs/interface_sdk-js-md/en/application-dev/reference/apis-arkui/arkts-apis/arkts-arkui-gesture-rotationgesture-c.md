# RotationGesture

Defines RotationGesture.

**Inheritance/Implementation:** RotationGesture extends [Gesture](arkts-arkui-gesture-gesture-c.md#gesture)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class RotationGesture--><!--Device-unnamed-export declare class RotationGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => RotationGesture, value?: RotationGestureHandlerOptions): RotationGesture
```

Set the value.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-static $_instantiate(factory: () => RotationGesture, value?: RotationGestureHandlerOptions): RotationGesture--><!--Device-RotationGesture-static $_instantiate(factory: () => RotationGesture, value?: RotationGestureHandlerOptions): RotationGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; RotationGesture | Yes |  |
| value | [RotationGestureHandlerOptions](arkts-arkui-gesture-rotationgesturehandleroptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [RotationGesture](arkts-arkui-gesture-rotationgesture-c.md) |  |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): this
```

The Rotation gesture is successfully recognized and a callback is triggered when the touch cancel event is received.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-onActionCancel(event: Callback<GestureEvent>): this--><!--Device-RotationGesture-onActionCancel(event: Callback<GestureEvent>): this-End-->

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

The Rotation gesture is successfully recognized. When the finger is lifted, the callback is triggered.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-onActionEnd(event: Callback<GestureEvent>): this--><!--Device-RotationGesture-onActionEnd(event: Callback<GestureEvent>): this-End-->

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

Rotation gesture recognition success callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-onActionStart(event: Callback<GestureEvent>): this--><!--Device-RotationGesture-onActionStart(event: Callback<GestureEvent>): this-End-->

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

Callback when the Rotation gesture is moving.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-onActionUpdate(event: Callback<GestureEvent>): this--><!--Device-RotationGesture-onActionUpdate(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

