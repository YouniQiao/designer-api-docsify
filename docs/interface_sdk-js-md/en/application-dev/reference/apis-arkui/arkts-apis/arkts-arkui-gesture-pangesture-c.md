# PanGesture

Defines PanGesture.

@extends Gesture

**Inheritance/Implementation:** PanGesture extends [Gesture](arkts-arkui-gesture-gesture-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class PanGesture--><!--Device-unnamed-export declare class PanGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => PanGesture, value?: PanGestureHandlerOptions | PanGestureOptions): PanGesture
```

Set the value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGesture-static $_instantiate(factory: () => PanGesture, value?: PanGestureHandlerOptions | PanGestureOptions): PanGesture--><!--Device-PanGesture-static $_instantiate(factory: () => PanGesture, value?: PanGestureHandlerOptions | PanGestureOptions): PanGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; PanGesture | Yes |  |
| value | [PanGestureHandlerOptions](arkts-arkui-gesture-pangesturehandleroptions-i.md) \| [PanGestureOptions](arkts-arkui-gesture-pangestureoptions-c.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGesture](arkts-arkui-gesture-pangesture-c.md) |  |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): this
```

The Pan gesture is successfully recognized and a callback is triggered when the touch cancel event is received.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGesture-onActionCancel(event: Callback<GestureEvent>): this--><!--Device-PanGesture-onActionCancel(event: Callback<GestureEvent>): this-End-->

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

The Pan gesture is successfully recognized. When the finger is lifted, the callback is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGesture-onActionEnd(event: Callback<GestureEvent>): this--><!--Device-PanGesture-onActionEnd(event: Callback<GestureEvent>): this-End-->

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

Pan gesture recognition success callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGesture-onActionStart(event: Callback<GestureEvent>): this--><!--Device-PanGesture-onActionStart(event: Callback<GestureEvent>): this-End-->

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

Callback when the Pan gesture is moving.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGesture-onActionUpdate(event: Callback<GestureEvent>): this--><!--Device-PanGesture-onActionUpdate(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

