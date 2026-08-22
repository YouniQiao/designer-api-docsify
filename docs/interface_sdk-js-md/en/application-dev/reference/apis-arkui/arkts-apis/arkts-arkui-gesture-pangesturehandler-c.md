# PanGestureHandler

Defines the PanGesture handler.

@extends GestureHandler

**Inheritance/Implementation:** PanGestureHandler extends [GestureHandler](arkts-arkui-gesture-gesturehandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class PanGestureHandler--><!--Device-unnamed-export declare class PanGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: PanGestureHandlerOptions)
```

Constructor parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandler-constructor(options?: PanGestureHandlerOptions)--><!--Device-PanGestureHandler-constructor(options?: PanGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PanGestureHandlerOptions](arkts-arkui-gesture-pangesturehandleroptions-i.md) | No |  |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): this
```

The Pan gesture is successfully recognized and a callback is triggered when the touch cancel event is received.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandler-onActionCancel(event: Callback<GestureEvent>): this--><!--Device-PanGestureHandler-onActionCancel(event: Callback<GestureEvent>): this-End-->

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

<!--Device-PanGestureHandler-onActionEnd(event: Callback<GestureEvent>): this--><!--Device-PanGestureHandler-onActionEnd(event: Callback<GestureEvent>): this-End-->

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

<!--Device-PanGestureHandler-onActionStart(event: Callback<GestureEvent>): this--><!--Device-PanGestureHandler-onActionStart(event: Callback<GestureEvent>): this-End-->

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

<!--Device-PanGestureHandler-onActionUpdate(event: Callback<GestureEvent>): this--><!--Device-PanGestureHandler-onActionUpdate(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

