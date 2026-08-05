# PanGestureInterface

PanGesture is used to trigger a pan gesture when the movement distance of a finger on the screen reaches the minimum value.

**Inheritance/Implementation:** PanGestureInterface extends [GestureInterface<PanGestureInterface>](GestureInterface<PanGestureInterface>)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-interface PanGestureInterface extends GestureInterface<PanGestureInterface>--><!--Device-unnamed-interface PanGestureInterface extends GestureInterface<PanGestureInterface>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions): PanGestureInterface
```

Creates a pan gesture. Inherits from [GestureInterface\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions): PanGestureInterface--><!--Device-PanGestureInterface-(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { fingers?: number; direction?: PanDirection; distance?: number } \| PanGestureOptions | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## constructor

```TypeScript
(options?: PanGestureHandlerOptions): PanGestureInterface
```

Creates a pan gesture. Compared with [PanGesture]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ | PanGestureOptions)}, this API adds the **isFingerCountLimited** and **distanceMap** parameters to **options**, which control whether to enforce the exact number of fingers touching the screen and specify the minimum pan distance required to trigger the gesture for different input sources, respectively.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-PanGestureInterface-(options?: PanGestureHandlerOptions): PanGestureInterface--><!--Device-PanGestureInterface-(options?: PanGestureHandlerOptions): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters of the swipe gesture handler. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## onActionCancel

```TypeScript
onActionCancel(event: () => void): PanGestureInterface
```

Registers the callback for pan gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful pan gesture recognition. No gesture event information is returned.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionCancel(event: () => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionCancel(event: () => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | () =&gt; void | Yes | Callback for pan gesture cancellation. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): PanGestureInterface
```

Registers the callback for pan gesture cancellation. This callback is triggered when a touch cancellation event occurs after successful pan gesture recognition. Gesture event information is returned.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PanGestureInterface-onActionCancel(event: Callback<GestureEvent>): PanGestureInterface--><!--Device-PanGestureInterface-onActionCancel(event: Callback<GestureEvent>): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;GestureEvent&gt; | Yes | Callback for pan gesture cancellation. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## onActionEnd

```TypeScript
onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface
```

Registers the callback for pan gesture completion. This callback is triggered when all fingers are lifted after successful pan gesture recognition.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | Callback for pan gesture completion. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## onActionStart

```TypeScript
onActionStart(event: (event: GestureEvent) => void): PanGestureInterface
```

Registers the callback for successful pan gesture recognition.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionStart(event: (event: GestureEvent) => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionStart(event: (event: GestureEvent) => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | Callback for successful pan gesture recognition. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## onActionUpdate

```TypeScript
onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface
```

Registers the callback for pan gesture updates. If **fingerList** contains multiple fingers, this callback updates the location information of only one finger each time.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface--><!--Device-PanGestureInterface-onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | Callback for pan gesture updates. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

