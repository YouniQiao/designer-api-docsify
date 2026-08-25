# Scroller

Defines a controller for scrollable container components.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. The binding of a &lt;em&gt;Scroller&lt;/em&gt; instance to a scrollable container component occurs during the component creation phase. <br>2. &lt;em&gt;Scroller&lt;/em&gt; APIs can only be effectively called after the &lt;em&gt;Scroller&lt;/em&gt; instance is bound to a scrollable container component. Otherwise, depending on the API called, it may have no effect or throw an exception. <br>3. For example, with aboutToAppear, this callback is executed after a new instance of a custom component is created and before its &lt;em&gt;build()&lt;/em&gt; method is called. Therefore, if a scrollable component is defined within the &lt;em&gt;build&lt;/em&gt; method of a custom component, the internal scrollable component has not yet been created during the &lt;em&gt;aboutToAppear&lt;/em&gt; callback of that custom component, and therefore the &lt;em&gt;Scroller&lt;/em&gt; APIs cannot be called effectively. </p>

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a &lt;em&gt;Scroller&lt;/em&gt; object.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentSize

```TypeScript
contentSize(): SizeResult
```

Obtains the content size.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SizeResult](../arkts-apis/arkts-arkui-common-sizeresult-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## currentOffset

```TypeScript
currentOffset() : OffsetResult
```

Obtains the current scrolling offset.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. If &lt;em&gt;Scroller&lt;/em&gt; is not bound to a component, this API returns &lt;em&gt;undefined&lt;/em&gt;, which is not declared in the API. You are advised to use the &lt;em&gt;offset&lt;/em&gt; function. <br>2. The &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components use a lazy loading mechanism. Before all content is fully loaded and laid out, the total content offset is estimated, and this estimation may be inaccurate. For the &lt;em&gt;List&lt;/em&gt; component, the &lt;em&gt;childrenMainSize&lt;/em&gt; attribute can be used to mitigate such inaccuracies. Currently, there is no solution to inaccurate estimation of the &lt;em&gt;Grid&lt;/em&gt; and &lt;em&gt;WaterFlow&lt;/em&gt; components. </p>

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OffsetResult](arkts-arkui-offsetresult-i.md) |

## fling

```TypeScript
fling(velocity: number): void
```

Performs inertial scrolling based on the initial velocity passed in.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| velocity | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## getFrameNode

```TypeScript
getFrameNode(): FrameNode | undefined
```

Obtains the FrameNode corresponding to this scroller.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| FrameNode \| undefined |

## getItemIndex

```TypeScript
getItemIndex(x: number, y: number): number
```

Obtains the index of a child component based on coordinates.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>The returned index is &lt;em&gt;-1&lt;/em&gt; for invalid coordinates. </p>

**Since:** 14

**ArkTS mode:** Supports only ArkTS-Dyn, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## getItemRect

```TypeScript
getItemRect(index: number): RectResult
```

Obtains the size and position of a child component relative to its container.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area. Otherwise, the value is considered invalid. <br>- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area. Otherwise, the value is considered invalid. </p>

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RectResult](../arkts-apis/arkts-arkui-common-rectresult-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## isAtEnd

```TypeScript
isAtEnd(): boolean
```

Checks whether the component has scrolled to the bottom.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>This API is available for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components. </p>

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## offset

```TypeScript
offset() : OffsetResult | undefined
```

Obtains the current scrolling offset.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OffsetResult](arkts-arkui-offsetresult-i.md) \| undefined |

## scrollBy

```TypeScript
scrollBy(dx: Length, dy: Length)
```

Scrolls by the specified amount.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>This API is available for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components. </p>

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dx | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |
| dy | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## scrollEdge

```TypeScript
scrollEdge(value: Edge, options?: ScrollEdgeOptions)
```

Scrolls to the edge of the container, regardless of the scroll axis direction. By default, the &lt;em&gt;Scroll&lt;/em&gt; component comes with an animation, while the &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components do not.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Edge](../arkts-apis/arkts-arkui-edge-e.md) | Yes |
| options | [ScrollEdgeOptions](arkts-arkui-scrolledgeoptions-i.md) | No |

## scrollPage

```TypeScript
scrollPage(value: ScrollPageOptions)
```

Scrolls to the next or previous page.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ScrollPageOptions](arkts-arkui-scrollpageoptions-i.md) | Yes |

## scrollPage

```TypeScript
scrollPage(value: { next: boolean; direction?: Axis })
```

Scrolls to the next or previous page.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [scrollPage](#scrollpage)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | { next: boolean; direction?: Axis } | Yes |

## scrollTo

```TypeScript
scrollTo(options: ScrollOptions)
```

Scrolls to the specified position. Anonymous Object Rectification.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>If the scrolling speed of the &lt;em&gt;scrollTo&lt;/em&gt; animation exceeds 200 vp/s, the components within the scrollable area will not respond to click events. </p>

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ScrollOptions](arkts-arkui-scrolloptions-i.md) | Yes |

## scrollToIndex

```TypeScript
scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)
```

Scrolls to a specified index, with support for setting an extra offset for the scroll. When smooth scrolling is enabled, all items encountered during the scroll are loaded and their layout is calculated. Loading a large number of items may cause performance issues. It is recommended that you first call &lt;em&gt;scrollToIndex&lt;/em&gt; without animation to jump to a position near the target, then call it again with animation to smoothly scroll to the final target position.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>This API only works for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components. <br>When refreshing the data source using &lt;em&gt;LazyForEach&lt;/em&gt;, &lt;em&gt;ForEach&lt;/em&gt;, or &lt;em&gt;Repeat&lt;/em&gt;, ensure this API is called after the data refresh is complete. <br>Starting from API version 11, the &lt;em&gt;List&lt;/em&gt; component supports &lt;em&gt;contentStartOffset&lt;/em&gt; and &lt;em&gt;contentEndOffset&lt;/em&gt;. Starting from API version 22, the &lt;em&gt;Grid&lt;/em&gt; and &lt;em&gt;WaterFlow&lt;/em&gt; components also support setting &lt;em&gt;contentStartOffset&lt;/em&gt; and &lt;em&gt;contentEndOffset&lt;/em&gt;. <br>- If the scrollable container has &lt;em&gt;contentStartOffset&lt;/em&gt; set and &lt;em&gt;ScrollAlign&lt;/em&gt; is &lt;em&gt;START&lt;/em&gt;, after scrolling, the start of the specified item will align with the &lt;em&gt;contentStartOffset&lt;/em&gt; of the container. <br>- If the scrollable container has &lt;em&gt;contentEndOffset&lt;/em&gt; set and &lt;em&gt;ScrollAlign&lt;/em&gt; is &lt;em&gt;END&lt;/em&gt;, after scrolling, the end of the specified item will align with the &lt;em&gt;contentEndOffset&lt;/em&gt; of the container. <br>- If the scrollable container has &lt;em&gt;contentStartOffset&lt;/em&gt; or &lt;em&gt;contentEndOffset&lt;/em&gt; set and &lt;em&gt;ScrollAlign&lt;/em&gt; is &lt;em&gt;AUTO&lt;/em&gt;: When the specified item is completely within the visible area, no adjustment is made. Otherwise, following the shortest-scroll-distance principle, the start of the item will align with the container's &lt;em&gt;contentStartOffset&lt;/em&gt;, or the end will align with the container's &lt;em&gt;contentEndOffset&lt;/em&gt;, ensuring the item is fully displayed. </p>

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| [smooth](../arkts-apis/arkts-arkui-viewmodel-scrollparam-i.md) | boolean | No |
| align | [ScrollAlign](arkts-arkui-scrollalign-e.md) | No |
| options | [ScrollToIndexOptions](arkts-arkui-scrolltoindexoptions-i.md) | No |
