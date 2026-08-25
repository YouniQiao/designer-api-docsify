# TapGestureInterface

TapGesture is used to trigger a tap gesture with one, two, or more taps.

> **NOTE：**&gt;
> When both number-tap and single-tap gestures are bound to a component with the number-tap gesture bound first, the
> single-tap gesture will have a 300 ms delay.

**Inheritance/Implementation:** TapGestureInterface extends GestureInterface<TapGestureInterface>

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## [[Call]]

```TypeScript
(value?: TapGestureParameters): TapGestureInterface
```

Creates a tap gesture. Inherits from [GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md).When triggered by keyboard or gamepad input, the gesture event's [SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md) is **Unknown**, and SourceType is **KEY** or **JOYSTICK**.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

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

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TapGestureInterface](arkts-arkui-tapgestureinterface-i.md) |
