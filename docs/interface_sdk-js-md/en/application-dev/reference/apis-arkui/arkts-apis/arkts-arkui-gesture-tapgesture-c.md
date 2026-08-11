# TapGesture

Defines TapGesture.

**Inheritance/Implementation:** TapGesture extends [Gesture](arkts-arkui-gesture-gesture-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TapGesture extends Gesture--><!--Device-unnamed-export declare class TapGesture extends Gesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => TapGesture, value?: TapGestureParameters): TapGesture
```

Set the value.TapGestureParameters: The parameters of the tapGesture.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGesture-static $_instantiate(factory: () => TapGesture, value?: TapGestureParameters): TapGesture--><!--Device-TapGesture-static $_instantiate(factory: () => TapGesture, value?: TapGestureParameters): TapGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; TapGesture | Yes |  |
| value | [TapGestureParameters](arkts-arkui-gesture-tapgestureparameters-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [TapGesture](arkts-arkui-gesture-tapgesture-c.md) |  |

## onAction

```TypeScript
onAction(event: Callback<GestureEvent>): this
```

Tap gesture recognition success callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGesture-onAction(event: Callback<GestureEvent>): this--><!--Device-TapGesture-onAction(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

