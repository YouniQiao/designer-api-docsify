# TapGesture

Defines TapGesture.

**Inheritance/Implementation:** TapGesture extends [Gesture](gesture-gesture-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TapGesture extends Gesture--><!--Device-unnamed-export declare class TapGesture extends Gesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => TapGesture, value?: TapGestureParameters): TapGesture
```

Set the value. TapGestureParameters: The parameters of the tapGesture.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TapGesture-static $_instantiate(factory: () => TapGesture, value?: TapGestureParameters): TapGesture--><!--Device-TapGesture-static $_instantiate(factory: () => TapGesture, value?: TapGestureParameters): TapGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; TapGesture | Yes |  |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

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
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

