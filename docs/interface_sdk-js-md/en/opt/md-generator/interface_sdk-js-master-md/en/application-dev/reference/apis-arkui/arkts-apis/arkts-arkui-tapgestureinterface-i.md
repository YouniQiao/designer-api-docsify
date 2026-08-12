# TapGestureInterface

TapGesture is used to trigger a tap gesture with one, two, or more taps.

> **NOTE：**
> 
> When both double-tap and single-tap gestures are bound to a component with the double-tap gesture bound first, the
> single-tap gesture will have a 300 ms delay.

**Inheritance/Implementation:** TapGestureInterface extends [GestureInterface<TapGestureInterface>](GestureInterface<TapGestureInterface>)

**Since:** 7

<!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>--><!--Device-unnamed-interface TapGestureInterface extends GestureInterface<TapGestureInterface>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(value?: TapGestureParameters): TapGestureInterface
```

Creates a tap gesture. Inherits from [GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md#GestureInterface).

When triggered by keyboard or gamepad input, the gesture event's [SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md#SourceTool) is **Unknown**, and   
[SourceType](SourceType) is **KEY** or **JOYSTICK**.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface--><!--Device-TapGestureInterface-(value?: TapGestureParameters): TapGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TapGestureParameters](arkts-arkui-tapgestureparameters-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) |

## onAction

```TypeScript
onAction(event: (event: GestureEvent) => void): TapGestureInterface
```

Triggered when the tap gesture is recognized.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TapGestureInterface-onAction(event: (event: GestureEvent) => void): TapGestureInterface--><!--Device-TapGestureInterface-onAction(event: (event: GestureEvent) => void): TapGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) |
