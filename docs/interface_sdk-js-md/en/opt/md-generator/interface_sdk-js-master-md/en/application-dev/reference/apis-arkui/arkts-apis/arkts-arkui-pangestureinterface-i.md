# PanGestureInterface

PanGesture is used to trigger a pan gesture when the movement distance of a finger on the screen reaches the minimum value.

**Inheritance/Implementation:** PanGestureInterface extends [GestureInterface<PanGestureInterface>](GestureInterface<PanGestureInterface>)

**Since:** 7

<!--Device-unnamed-interface PanGestureInterface extends GestureInterface<PanGestureInterface>--><!--Device-unnamed-interface PanGestureInterface extends GestureInterface<PanGestureInterface>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions): PanGestureInterface
```

Creates a pan gesture. Inherits from [GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md#GestureInterface).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions): PanGestureInterface--><!--Device-PanGestureInterface-(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | { fingers?: number; direction?: PanDirection; distance?: number } \| [PanGestureOptions](arkts-arkui-pangestureoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |

## [[Call]]

```TypeScript
(options?: PanGestureHandlerOptions): PanGestureInterface
```

Creates a pan gesture. Compared with [PanGesture](PanGestureInterface(value?: { fingers?: number; direction?: PanDirection; distance?: number) | PanGestureOptions)}, this API adds the **isFingerCountLimited** and **distanceMap** parameters to **options**, which control whether to enforce the exact number of fingers touching the screen and specify the minimum pan distance required to trigger the gesture for different input sources, respectively.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PanGestureInterface-(options?: PanGestureHandlerOptions): PanGestureInterface--><!--Device-PanGestureInterface-(options?: PanGestureHandlerOptions): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [PanGestureHandlerOptions](arkts-arkui-pangesturehandleroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: () => void): PanGestureInterface
```

Registers the callback for pan gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful pan gesture recognition. No gesture event information is returned.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionCancel(event: () => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionCancel(event: () => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): PanGestureInterface
```

Registers the callback for pan gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful pan gesture recognition. Gesture event information is returned.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PanGestureInterface-onActionCancel(event: Callback<GestureEvent>): PanGestureInterface--><!--Device-PanGestureInterface-onActionCancel(event: Callback<GestureEvent>): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |

## onActionEnd

```TypeScript
onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface
```

Registers the callback for pan gesture completion. This callback is triggered when all fingers are lifted after successful pan gesture recognition.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |

## onActionStart

```TypeScript
onActionStart(event: (event: GestureEvent) => void): PanGestureInterface
```

Registers the callback for successful pan gesture recognition.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionStart(event: (event: GestureEvent) => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionStart(event: (event: GestureEvent) => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |

## onActionUpdate

```TypeScript
onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface
```

Registers the callback for pan gesture updates. If **fingerList** contains multiple fingers, this callback updates the location information of only one finger each time.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: GestureEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanGestureInterface](arkts-arkui-pangestureinterface-i.md) |
