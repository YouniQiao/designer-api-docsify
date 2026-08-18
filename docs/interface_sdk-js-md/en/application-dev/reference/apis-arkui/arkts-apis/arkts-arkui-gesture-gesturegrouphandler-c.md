# GestureGroupHandler

Defines the GestureGroup handler.

**Inheritance/Implementation:** GestureGroupHandler extends [GestureHandler](arkts-arkui-gesture-gesturehandler-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class GestureGroupHandler--><!--Device-unnamed-export declare class GestureGroupHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: GestureGroupGestureHandlerOptions)
```

Constructor parameters.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroupHandler-constructor(options?: GestureGroupGestureHandlerOptions)--><!--Device-GestureGroupHandler-constructor(options?: GestureGroupGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GestureGroupGestureHandlerOptions](arkts-arkui-gesture-gesturegroupgesturehandleroptions-i.md) | No |  |

## onCancel

```TypeScript
onCancel(event: VoidCallback): this
```

The GestureGroup gesture is successfully recognized and a callback is triggered when the touch cancel event is received.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroupHandler-onCancel(event: VoidCallback): this--><!--Device-GestureGroupHandler-onCancel(event: VoidCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

