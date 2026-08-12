# SwipeGesture

Defines SwipeGesture.

**Inheritance/Implementation:** SwipeGesture extends [Gesture](arkts-arkui-gesture-gesture-c.md#Gesture)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class SwipeGesture extends Gesture--><!--Device-unnamed-export declare class SwipeGesture extends Gesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => SwipeGesture, value?: SwipeGestureHandlerOptions): SwipeGesture
```

Set the value.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGesture-static $_instantiate(factory: () => SwipeGesture, value?: SwipeGestureHandlerOptions): SwipeGesture--><!--Device-SwipeGesture-static $_instantiate(factory: () => SwipeGesture, value?: SwipeGestureHandlerOptions): SwipeGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; SwipeGesture | Yes |  |
| value | [SwipeGestureHandlerOptions](arkts-arkui-gesture-swipegesturehandleroptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [SwipeGesture](arkts-arkui-gesture-swipegesture-c.md) |  |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): this
```

Slide gesture recognition success callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwipeGesture-onAction(event: Callback<GestureEvent>): this--><!--Device-SwipeGesture-onAction(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

