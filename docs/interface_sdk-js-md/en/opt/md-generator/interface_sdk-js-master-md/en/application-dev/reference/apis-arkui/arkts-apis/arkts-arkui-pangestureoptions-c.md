# PanGestureOptions

Defines the PanGesture options.

**Since:** 7

**Deprecated since:** -1

<!--Device-unnamed-declare class PanGestureOptions--><!--Device-unnamed-declare class PanGestureOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })
```

Creates a pan gesture configuration object. The **PanGestureOptions** API enables dynamic updates to pan gesture properties without requiring state variable modifications that would trigger UI re-renders.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureOptions-constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })--><!--Device-PanGestureOptions-constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | { fingers?: number; direction?: PanDirection; distance?: number } | No | Pan gesture configuration. & lt;br & gt;**fingers**: minimum number of fingers required. The value ranges from 1 to 10. & lt;br & gt;Default value: **1** & lt;br & gt;**direction**: pan direction. The value supports the AND ( & ) and OR (\ |

## getDirection

```TypeScript
getDirection(): PanDirection
```

Obtains the pan direction.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PanGestureOptions-getDirection(): PanDirection--><!--Device-PanGestureOptions-getDirection(): PanDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanDirection](arkts-arkui-pandirection-e.md) |

## getDistance

```TypeScript
getDistance(): number
```

Obtains the minimum pan distance to trigger the gesture. The unit is vp.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PanGestureOptions-getDistance(): number--><!--Device-PanGestureOptions-getDistance(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## setDirection

```TypeScript
setDirection(value: PanDirection)
```

Sets the pan direction.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureOptions-setDirection(value: PanDirection)--><!--Device-PanGestureOptions-setDirection(value: PanDirection)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PanDirection](arkts-arkui-pandirection-e.md) | Yes | Pan direction. The value supports the AND ( & ) and OR (\ |

## setDistance

```TypeScript
setDistance(value: number)
```

Sets the minimum pan distance to trigger the gesture, in vp. To avoid performance degradation due to excessive response delays or accidental releases, avoid excessively large values. For best practices, see [Reducing the Pan Distance for Gesture Recognition](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-application-latency-optimization-cases#section1116134115286).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureOptions-setDistance(value: number)--><!--Device-PanGestureOptions-setDistance(value: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## setFingers

```TypeScript
setFingers(value: number)
```

Sets the minimum number of fingers to trigger the gesture.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PanGestureOptions-setFingers(value: number)--><!--Device-PanGestureOptions-setFingers(value: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
