# ArcListAttribute

In addition to the universal attributes, the following attributes are supported.

**Inheritance/Implementation:** ArcListAttribute extends CommonMethod<ArcListAttribute>

**Since:** 18

**Deprecated since:** -1

<!--Device-unnamed-export declare class ArcListAttribute--><!--Device-unnamed-export declare class ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcListItemAttribute, ArcList, ArcListItem, ArcListAttribute } from '@kit.ArkUI';
```

## cachedCount

```TypeScript
cachedCount(count: Optional<number>): ArcListAttribute
```

Sets the number of arc list items to be preloaded (cached). In a lazy loading scenario, only the content equivalent to **cachedCount** outside the visible area of the arc list is preloaded. In a non-lazy loading scenario, all items are loaded at once. For both lazy and non-lazy loading, only the content within the visible area of the arc list plus the content equivalent to **cachedCount** outside the visible area is laid out. When **cachedCount** is set for the arc list, the system preloads and lays out the **cachedCount**-specified number of rows of arc list items both above and below the currently visible area of the arc list.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-cachedCount(count: Optional<number>): ArcListAttribute--><!--Device-ArcListAttribute-cachedCount(count: Optional<number>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## chainAnimation

```TypeScript
chainAnimation(enable: Optional<boolean>): ArcListAttribute
```

Sets whether to enable chained animations, which provide a visually connected, or "chained," effect when the **ArcList** component is scrolled or its top or bottom edge is dragged. The list items are separated with even space, and one item animation starts after the previous animation during basic sliding interactions. The chained animation effect is similar with spring physics. For chained animations to work properly, the edge scrolling effect of the **ArcList** component must be set to **EdgeEffect.Spring**.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-chainAnimation(enable: Optional<boolean>): ArcListAttribute--><!--Device-ArcListAttribute-chainAnimation(enable: Optional<boolean>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## childrenMainSize

```TypeScript
childrenMainSize(size: Optional<ChildrenMainSize>): ArcListAttribute
```

Sets the size information of the child components of the **ArcList** component along the main axis.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-childrenMainSize(size: Optional<ChildrenMainSize>): ArcListAttribute--><!--Device-ArcListAttribute-childrenMainSize(size: Optional<ChildrenMainSize>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ChildrenMainSize](../arkts-components/arkts-arkui-childrenmainsize-c.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): ArcListAttribute
```

Sets the sensitivity of the digital crown's event response.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): ArcListAttribute--><!--Device-ArcListAttribute-digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sensitivity | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[CrownSensitivity](arkts-arkui-crownsensitivity-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## enableScrollInteraction

```TypeScript
enableScrollInteraction(enable: Optional<boolean>): ArcListAttribute
```

Sets whether to enable scroll gestures.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-enableScrollInteraction(enable: Optional<boolean>): ArcListAttribute--><!--Device-ArcListAttribute-enableScrollInteraction(enable: Optional<boolean>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## fadingEdge

```TypeScript
fadingEdge(enable: Optional<boolean>): ArcListAttribute
```

Sets whether to enable the edge fading effect.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-fadingEdge(enable: Optional<boolean>): ArcListAttribute--><!--Device-ArcListAttribute-fadingEdge(enable: Optional<boolean>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## flingSpeedLimit

```TypeScript
flingSpeedLimit(speed: Optional<number>): ArcListAttribute
```

Sets the maximum initial speed for inertial scrolling after a fling gesture. If this attribute is set to a value less than or equal to 0, the default value is used.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-flingSpeedLimit(speed: Optional<number>): ArcListAttribute--><!--Device-ArcListAttribute-flingSpeedLimit(speed: Optional<number>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| speed | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## friction

```TypeScript
friction(friction: Optional<number>): ArcListAttribute
```

Sets the friction coefficient. It applies only to gestures in the scrolling area, and it affects only the inertial scrolling process. If this attribute is set to a value less than or equal to 0, the default value is used.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-friction(friction: Optional<number>): ArcListAttribute--><!--Device-ArcListAttribute-friction(friction: Optional<number>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [friction](#friction) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onDidScroll

```TypeScript
onDidScroll(handler: Optional<OnScrollCallback>): ArcListAttribute
```

Triggered when the list scrolls. The return value is the offset amount by which the list has scrolled and the current scroll state.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-onDidScroll(handler: Optional<OnScrollCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onDidScroll(handler: Optional<OnScrollCallback>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[OnScrollCallback](../arkts-components/arkts-arkui-onscrollcallback-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onReachEnd

```TypeScript
onReachEnd(handler: Optional<VoidCallback>): ArcListAttribute
```

Triggered when the list reaches the end position. If the edge scrolling effect is set to spring, this event is triggered when scrolling past the end position and again when bouncing back to it.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-onReachEnd(handler: Optional<VoidCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onReachEnd(handler: Optional<VoidCallback>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[VoidCallback](arkts-arkui-voidcallback-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onReachStart

```TypeScript
onReachStart(handler: Optional<VoidCallback>): ArcListAttribute
```

Triggered when the list reaches the start position. This event is triggered during initialization of the **ArcList** component if **initialIndex** is set to **0**, and whenever the list scrolls to the start position. If the edge scrolling effect is set to spring, this event is triggered when scrolling past the start position and again when bouncing back to it.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-onReachStart(handler: Optional<VoidCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onReachStart(handler: Optional<VoidCallback>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[VoidCallback](arkts-arkui-voidcallback-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onScrollIndex

```TypeScript
onScrollIndex(handler: Optional<ArcScrollIndexHandler>): ArcListAttribute
```

Triggered when a child component enters or leaves the visible area of the **ArcList** component. This event is triggered during initialization of the **ArcList** component and when the index of the first or last child component in the visible area changes, or when the center child component changes. If the edge scrolling effect of the **ArcList** component is set to spring, this event is not triggered during continued scrolling at the edge or during the bounce-back process.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-onScrollIndex(handler: Optional<ArcScrollIndexHandler>): ArcListAttribute--><!--Device-ArcListAttribute-onScrollIndex(handler: Optional<ArcScrollIndexHandler>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ArcScrollIndexHandler](arkts-arkui-arcscrollindexhandler-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onScrollStart

```TypeScript
onScrollStart(handler: Optional<VoidCallback>): ArcListAttribute
```

Triggered when the list starts scrolling initiated by the user's finger dragging the list or its scrollbar. This event is also triggered when the animation contained in the scrolling triggered by **Scroller** starts.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-onScrollStart(handler: Optional<VoidCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onScrollStart(handler: Optional<VoidCallback>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[VoidCallback](arkts-arkui-voidcallback-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onScrollStop

```TypeScript
onScrollStop(handler: Optional<VoidCallback>): ArcListAttribute
```

Triggered when the list stops scrolling after the user's finger leaves the screen. This event is also triggered when the animation contained in the scrolling triggered by **Scroller** stops.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-onScrollStop(handler: Optional<VoidCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onScrollStop(handler: Optional<VoidCallback>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[VoidCallback](arkts-arkui-voidcallback-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onWillScroll

```TypeScript
onWillScroll(handler: Optional<OnWillScrollCallback>): ArcListAttribute
```

Triggered before each frame during list scrolling. The callback returns the offset amount by which the list will scroll and the current scroll state. The returned offset is a calculated value, not the actual offset.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-onWillScroll(handler: Optional<OnWillScrollCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onWillScroll(handler: Optional<OnWillScrollCallback>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[OnWillScrollCallback](../arkts-components/arkts-arkui-onwillscrollcallback-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## scrollBar

```TypeScript
scrollBar(status: Optional<BarState>): ArcListAttribute
```

Sets the state of the scrollbar.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-scrollBar(status: Optional<BarState>): ArcListAttribute--><!--Device-ArcListAttribute-scrollBar(status: Optional<BarState>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[BarState](arkts-arkui-barstate-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## scrollBarColor

```TypeScript
scrollBarColor(color: Optional<ColorMetrics>): ArcListAttribute
```

Sets the color of the scrollbar.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-scrollBarColor(color: Optional<ColorMetrics>): ArcListAttribute--><!--Device-ArcListAttribute-scrollBarColor(color: Optional<ColorMetrics>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;ColorMetrics&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## scrollBarWidth

```TypeScript
scrollBarWidth(width: Optional<LengthMetrics>): ArcListAttribute
```

Sets the width of the scrollbar. Once the width is set, the scrollbar will use this width in its pressed state.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-scrollBarWidth(width: Optional<LengthMetrics>): ArcListAttribute--><!--Device-ArcListAttribute-scrollBarWidth(width: Optional<LengthMetrics>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;LengthMetrics&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## space

```TypeScript
space(space: Optional<LengthMetrics>): ArcListAttribute
```

Sets the spacing between list items.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcListAttribute-space(space: Optional<LengthMetrics>): ArcListAttribute--><!--Device-ArcListAttribute-space(space: Optional<LengthMetrics>): ArcListAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [space](#space) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;LengthMetrics&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |
