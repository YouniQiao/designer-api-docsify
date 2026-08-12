# TapGestureHandler

Defines the TapGesture handler.

**Inheritance/Implementation:** TapGestureHandler extends [GestureHandler](arkts-arkui-gesture-gesturehandler-c.md#GestureHandler)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TapGestureHandler extends GestureHandler--><!--Device-unnamed-export declare class TapGestureHandler extends GestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: TapGestureHandlerOptions)
```

Constructor parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandler-constructor(options?: TapGestureHandlerOptions)--><!--Device-TapGestureHandler-constructor(options?: TapGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TapGestureHandlerOptions](arkts-arkui-gesture-tapgesturehandleroptions-i.md) | No |  |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): this
```

Tap gesture recognition success callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGestureHandler-onAction(event: Callback<GestureEvent>): this--><!--Device-TapGestureHandler-onAction(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gesture-gestureevent-i.md)&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

