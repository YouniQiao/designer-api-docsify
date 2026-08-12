# SwipeGestureHandler

Defines the SwipeGesture handler.

**Inheritance/Implementation:** SwipeGestureHandler extends [GestureHandler](arkts-arkui-gesture-gesturehandler-c.md#GestureHandler)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class SwipeGestureHandler extends GestureHandler--><!--Device-unnamed-export declare class SwipeGestureHandler extends GestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: SwipeGestureHandlerOptions)
```

Constructor parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandler-constructor(options?: SwipeGestureHandlerOptions)--><!--Device-SwipeGestureHandler-constructor(options?: SwipeGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SwipeGestureHandlerOptions](arkts-arkui-gesture-swipegesturehandleroptions-i.md) | No |  |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): this
```

Swipe gesture recognition success callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGestureHandler-onAction(event: Callback<GestureEvent>): this--><!--Device-SwipeGestureHandler-onAction(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

