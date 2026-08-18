# PinchGestureInterface

**PinchGesture** is used to trigger a pinch gesture, which requires two to five fingers with a minimum 5 vp distance between the fingers. > **NOTE：**> > To trigger the pinch gesture again after successful recognition, all fingers must be lifted and then make > contact again to satisfy the recognition criteria.

**Inheritance/Implementation:** PinchGestureInterface extends GestureInterface<PinchGestureInterface>

**Since:** 7

<!--Device-unnamed-interface PinchGestureInterface--><!--Device-unnamed-interface PinchGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
(value?: { fingers?: number; distance?: number }): PinchGestureInterface
```

Sets the parameters for the pinch gesture. Inherits from [GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md#gestureinterface).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PinchGestureInterface-(value?: { fingers?: number; distance?: number }): PinchGestureInterface--><!--Device-PinchGestureInterface-(value?: { fingers?: number; distance?: number }): PinchGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | { fingers?: number; distance?: number } | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## constructor

```TypeScript
(options?: PinchGestureHandlerOptions): PinchGestureInterface
```

Sets the parameters for the pinch gesture. Compared with PinchGesture)}, this API adds the **isFingerCountLimited** parameter to **options**, which determines whether to enforce the exact number of fingers touching the screen.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PinchGestureInterface-(options?: PinchGestureHandlerOptions): PinchGestureInterface--><!--Device-PinchGestureInterface-(options?: PinchGestureHandlerOptions): PinchGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [PinchGestureHandlerOptions](arkts-arkui-pinchgesturehandleroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: () => void): PinchGestureInterface
```

Triggered when a touch cancellation event occurs after successful pinch gesture recognition. No gesture event information is returned.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PinchGestureInterface-onActionCancel(event: () => void): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionCancel(event: () => void): PinchGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): PinchGestureInterface
```

Triggered when a touch cancellation event occurs after successful pinch gesture recognition. Compared with onActionCancel, this callback returns gesture event information.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PinchGestureInterface-onActionCancel(event: Callback<GestureEvent>): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionCancel(event: Callback<GestureEvent>): PinchGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionEnd

```TypeScript
onActionEnd(event: (event: GestureEvent) => void): PinchGestureInterface
```

Triggered when all fingers are lifted after successful pinch gesture recognition.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PinchGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PinchGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionStart

```TypeScript
onActionStart(event: (event: GestureEvent) => void): PinchGestureInterface
```

Triggered after the pinch gesture is recognized.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PinchGestureInterface-onActionStart(event: (event: GestureEvent) => void): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionStart(event: (event: GestureEvent) => void): PinchGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |

## onActionUpdate

```TypeScript
onActionUpdate(event: (event: GestureEvent) => void): PinchGestureInterface
```

Triggered when the user moves the finger in the pinch gesture on the screen.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PinchGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PinchGestureInterface--><!--Device-PinchGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PinchGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PinchGestureInterface](arkts-arkui-pinchgestureinterface-i.md) |
