# TapGestureInterface

TapGesture is used to trigger a tap gesture with one, two, or more taps.

> **NOTE：**
> 
> When both double-tap and single-tap gestures are bound to a component with the double-tap gesture bound first, the
> single-tap gesture will have a 300 ms delay.

**Inheritance/Implementation:** TapGestureInterface extends [GestureInterface<TapGestureInterface>](GestureInterface<TapGestureInterface>)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>--><!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(value?: TapGestureParameters): TapGestureInterface
```

Creates a tap gesture. Inherits from [GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md#GestureInterface).

When triggered by keyboard or gamepad input, the gesture event's [SourceTool](SourceTool) is **Unknown**, and   
[SourceType](SourceType) is **KEY** or **JOYSTICK**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface--><!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TapGestureParameters](arkts-arkui-tapgestureparameters-i.md) | No | Parameters for the tap gesture.<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) |  |

## onAction

```TypeScript
onAction(event: (event: GestureEvent) => void): TapGestureInterface
```

Triggered when the tap gesture is recognized.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TapGestureInterface-onAction(event: (event: GestureEvent) => void): TapGestureInterface--><!--Device-TapGestureInterface-onAction(event: (event: GestureEvent) => void): TapGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | Callback for the tap event. |

**Return value:**

| Type | Description |
| --- | --- |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) |  |

