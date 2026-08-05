# TapGestureInterface

TapGesture is used to trigger a tap gesture with one, two, or more taps. > **NOTE** > > When both double-tap and single-tap gestures are bound to a component with the double-tap gesture bound first, the > single-tap gesture will have a 300 ms delay.

**Inheritance/Implementation:** TapGestureInterface extends [GestureInterface<TapGestureInterface>](GestureInterface<TapGestureInterface>)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>--><!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
(value?: TapGestureParameters): TapGestureInterface
```

Creates a tap gesture. Inherits from [GestureInterface\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. When triggered by keyboard or gamepad input, the gesture event's [SourceTool]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ is **Unknown**, and [SourceType]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ is **KEY** or **JOYSTICK**.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface--><!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters for the tap gesture.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

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
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

