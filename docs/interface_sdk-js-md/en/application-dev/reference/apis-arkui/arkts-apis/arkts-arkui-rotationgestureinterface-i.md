# RotationGestureInterface

**RotationGesture** is used to trigger a rotation gesture, which recognizes rotational movements using two to five fingers, with a minimum angular change of 1 degree. This gesture cannot be triggered using a two-finger rotation operation on a trackpad.

**Inheritance/Implementation:** RotationGestureInterface extends GestureInterface<RotationGestureInterface>

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## [[Call]]

```TypeScript
(value?: { fingers?: number; angle?: number }): RotationGestureInterface
```

Sets the parameters for the rotation gesture. Inherits from [GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md).

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | { fingers?: number; angle?: number } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## [[Call]]

```TypeScript
(options?: RotationGestureHandlerOptions): RotationGestureInterface
```

Sets the parameters for the rotation gesture. Compared with RotationGesture)}, this API adds the **isFingerCountLimited** parameter to **options**, which determines whether to enforce the exact number of fingers touching the screen.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RotationGestureHandlerOptions](arkts-arkui-rotationgesturehandleroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: () => void): RotationGestureInterface
```

Triggered when a tap cancellation event is received after the rotation gesture is recognized. This callback does not return gesture event information.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): RotationGestureInterface
```

Triggered when a tap cancellation event is received after the rotation gesture is recognized. Compared with onActionCancel, this callback returns gesture event information.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionEnd

```TypeScript
onActionEnd(event: (event: GestureEvent) => void): RotationGestureInterface
```

Triggered when the last finger used for the rotation gesture is lifted.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionStart

```TypeScript
onActionStart(event: (event: GestureEvent) => void): RotationGestureInterface
```

Triggered when the rotation gesture is recognized successfully.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |

## onActionUpdate

```TypeScript
onActionUpdate(event: (event: GestureEvent) => void): RotationGestureInterface
```

Triggered during the movement of the rotation gesture.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RotationGestureInterface](arkts-arkui-rotationgestureinterface-i.md) |
