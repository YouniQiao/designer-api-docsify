# Scroller

Defines a controller for scrollable container components. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;1. The binding of a &lt;em&gt;Scroller&lt;/em&gt; instance to a scrollable container component occurs during the component creation phase. &lt;br&gt;2. &lt;em&gt;Scroller&lt;/em&gt; APIs can only be effectively called after the &lt;em&gt;Scroller&lt;/em&gt; instance is bound to a scrollable container component. Otherwise, depending on the API called, it may have no effect or throw an exception. &lt;br&gt;3. For example, with aboutToAppear, this callback is executed after a new instance of a custom component is created and before its &lt;em&gt;build()&lt;/em&gt; method is called. Therefore, if a scrollable component is defined within the &lt;em&gt;build&lt;/em&gt; method of a custom component, the internal scrollable component has not yet been created during the &lt;em&gt;aboutToAppear&lt;/em&gt; callback of that custom component, and therefore the &lt;em&gt;Scroller&lt;/em&gt; APIs cannot be called effectively. &lt;/p&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

<!--Device-unnamed-declare class Scroller--><!--Device-unnamed-declare class Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

A constructor used to create a &lt;em&gt;Scroller&lt;/em&gt; object.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-constructor()--><!--Device-Scroller-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentSize

```TypeScript
contentSize(): SizeResult
```

Obtains the content size.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Scroller-contentSize(): SizeResult--><!--Device-Scroller-contentSize(): SizeResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| SizeResult | Total size of the scrollable component's content, including the content width and height. &lt;br&gt;Unit: vp |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100004](../errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## currentOffset

```TypeScript
currentOffset() : OffsetResult
```

Obtains the current scrolling offset. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;1. If &lt;em&gt;Scroller&lt;/em&gt; is not bound to a component, this API returns &lt;em&gt;undefined&lt;/em&gt;, which is not declared in the API. You are advised to use the &lt;em&gt;offset&lt;/em&gt; function. &lt;br&gt;2. The &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components use a lazy loading mechanism. Before all content is fully loaded and laid out, the total content offset is estimated, and this estimation may be inaccurate. For the &lt;em&gt;List&lt;/em&gt; component, the &lt;em&gt;childrenMainSize&lt;/em&gt; attribute can be used to mitigate such inaccuracies. Currently, there is no solution to inaccurate estimation of the &lt;em&gt;Grid&lt;/em&gt; and &lt;em&gt;WaterFlow&lt;/em&gt; components. &lt;/p&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-currentOffset() : OffsetResult--><!--Device-Scroller-currentOffset() : OffsetResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OffsetResult](arkts-arkui-offsetresult-i.md) | Returns the current scrolling offset. If the scroller not bound to a component, the return value is void. |

## fling

```TypeScript
fling(velocity: number): void
```

Performs inertial scrolling based on the initial velocity passed in.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Scroller-fling(velocity: number): void--><!--Device-Scroller-fling(velocity: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | number | Yes | Initial velocity of inertial scrolling. Unit: vp/s &lt;br&gt;&lt;em&gt;NOTE&lt;/em&gt; &lt;br&gt;If the value specified is 0, it is considered as invalid, and the scrolling for this instance will not take effect. A positive value indicates scrolling towards the top, while a negative value indicates scrolling towards the bottom. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [100004](../errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## getFrameNode

```TypeScript
getFrameNode(): FrameNode | undefined
```

Obtains the FrameNode corresponding to this scroller.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Scroller-getFrameNode(): FrameNode | undefined--><!--Device-Scroller-getFrameNode(): FrameNode | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| FrameNode | Returns the FrameNode bound to this scroller. If the scroller is not bound to a component, the return value is undefined. |

## getItemIndex

```TypeScript
getItemIndex(x: number, y: number): number
```

Obtains the index of a child component based on coordinates. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;The returned index is &lt;em&gt;-1&lt;/em&gt; for invalid coordinates. &lt;/p&gt;

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Scroller-getItemIndex(x: number, y: number): number--><!--Device-Scroller-getItemIndex(x: number, y: number): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | X-coordinate, in vp. |
| y | number | Yes | Y-coordinate, in vp. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Index of the item. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [100004](../errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## getItemRect

```TypeScript
getItemRect(index: number): RectResult
```

Obtains the size and position of a child component relative to its container. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area. Otherwise, the value is considered invalid. &lt;br&gt;- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area. Otherwise, the value is considered invalid. &lt;/p&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Scroller-getItemRect(index: number): RectResult--><!--Device-Scroller-getItemRect(index: number): RectResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the target child component. |

**Return value:**

| Type | Description |
| --- | --- |
| RectResult | Size and position of the child component relative to the component.&lt;br&gt;Unit: vp |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [100004](../errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## isAtEnd

```TypeScript
isAtEnd(): boolean
```

Checks whether the component has scrolled to the bottom. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;This API is available for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components. &lt;/p&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-isAtEnd(): boolean--><!--Device-Scroller-isAtEnd(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the component scrolls to the end position. |

## offset

```TypeScript
offset() : OffsetResult | undefined
```

Obtains the current scrolling offset.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Scroller-offset() : OffsetResult | undefined--><!--Device-Scroller-offset() : OffsetResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OffsetResult](arkts-arkui-offsetresult-i.md) | Returns the current scrolling offset. If the scroller not bound to a component, the return value is undefined. |

## scrollBy

```TypeScript
scrollBy(dx: Length, dy: Length)
```

Scrolls by the specified amount. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;This API is available for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components. &lt;/p&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollBy(dx: Length, dy: Length)--><!--Device-Scroller-scrollBy(dx: Length, dy: Length)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | Length | Yes | Amount to scroll by in the horizontal direction. The percentage format is not supported. |
| dy | Length | Yes | Amount to scroll by in the vertical direction. The percentage format is not supported. |

## scrollEdge

```TypeScript
scrollEdge(value: Edge, options?: ScrollEdgeOptions)
```

Scrolls to the edge of the container, regardless of the scroll axis direction. By default, the &lt;em&gt;Scroll&lt;/em&gt; component comes with an animation, while the &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components do not.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollEdge(value: Edge, options?: ScrollEdgeOptions)--><!--Device-Scroller-scrollEdge(value: Edge, options?: ScrollEdgeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Edge | Yes | Edge position to scroll to. &lt;br&gt;&lt;em&gt;Atomic service API&lt;/em&gt;: This API can be used in atomic services since API version 11. |
| options | [ScrollEdgeOptions](arkts-arkui-scrolledgeoptions-i.md) | No | Mode of scrolling to the edge position. &lt;br&gt;&lt;em&gt;Atomic service API&lt;/em&gt;: This API can be used in atomic services since API version 12.<br>**Since:** 12 |

## scrollPage

```TypeScript
scrollPage(value: ScrollPageOptions)
```

Scrolls to the next or previous page.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollPage(value: ScrollPageOptions)--><!--Device-Scroller-scrollPage(value: ScrollPageOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollPageOptions](arkts-arkui-scrollpageoptions-i.md) | Yes | Page turning mode.<br>**Since:** 14 |

## scrollPage

```TypeScript
scrollPage(value: { next: boolean; direction?: Axis })
```

Scrolls to the next or previous page.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [scrollPage](#scrollPage)

<!--Device-Scroller-scrollPage(value: { next: boolean; direction?: Axis })--><!--Device-Scroller-scrollPage(value: { next: boolean; direction?: Axis })-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { next: boolean; direction?: Axis } | Yes | next: Whether to turn to the next page. The value &lt;em&gt;true&lt;/em&gt; means to scroll to the next page, and &lt;em&gt;false&lt;/em&gt; means to scroll to the previous page. direction: Scrolling direction: horizontal or vertical. |

## scrollTo

```TypeScript
scrollTo(options: ScrollOptions)
```

Scrolls to the specified position. Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;If the scrolling speed of the &lt;em&gt;scrollTo&lt;/em&gt; animation exceeds 200 vp/s, the components within the scrollable area will not respond to click events. &lt;/p&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollTo(options: ScrollOptions)--><!--Device-Scroller-scrollTo(options: ScrollOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ScrollOptions](arkts-arkui-scrolloptions-i.md) | Yes | Parameters for scrolling to the specified position.<br>**Since:** 18 |

## scrollToIndex

```TypeScript
scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)
```

Scrolls to a specified index, with support for setting an extra offset for the scroll. When smooth scrolling is enabled, all items encountered during the scroll are loaded and their layout is calculated. Loading a large number of items may cause performance issues. It is recommended that you first call &lt;em&gt;scrollToIndex&lt;/em&gt; without animation to jump to a position near the target, then call it again with animation to smoothly scroll to the final target position. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;This API only works for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components. &lt;br&gt;When refreshing the data source using &lt;em&gt;LazyForEach&lt;/em&gt;, &lt;em&gt;ForEach&lt;/em&gt;, or &lt;em&gt;Repeat&lt;/em&gt;, ensure this API is called after the data refresh is complete. &lt;br&gt;Starting from API version 11, the &lt;em&gt;List&lt;/em&gt; component supports &lt;em&gt;contentStartOffset&lt;/em&gt; and &lt;em&gt;contentEndOffset&lt;/em&gt;. Starting from API version 22, the &lt;em&gt;Grid&lt;/em&gt; and &lt;em&gt;WaterFlow&lt;/em&gt; components also support setting &lt;em&gt;contentStartOffset&lt;/em&gt; and &lt;em&gt;contentEndOffset&lt;/em&gt;. &lt;br&gt;- If the scrollable container has &lt;em&gt;contentStartOffset&lt;/em&gt; set and &lt;em&gt;ScrollAlign&lt;/em&gt; is &lt;em&gt;START&lt;/em&gt;, after scrolling, the start of the specified item will align with the &lt;em&gt;contentStartOffset&lt;/em&gt; of the container. &lt;br&gt;- If the scrollable container has &lt;em&gt;contentEndOffset&lt;/em&gt; set and &lt;em&gt;ScrollAlign&lt;/em&gt; is &lt;em&gt;END&lt;/em&gt;, after scrolling, the end of the specified item will align with the &lt;em&gt;contentEndOffset&lt;/em&gt; of the container. &lt;br&gt;- If the scrollable container has &lt;em&gt;contentStartOffset&lt;/em&gt; or &lt;em&gt;contentEndOffset&lt;/em&gt; set and &lt;em&gt;ScrollAlign&lt;/em&gt; is &lt;em&gt;AUTO&lt;/em&gt;: When the specified item is completely within the visible area, no adjustment is made. Otherwise, following the shortest-scroll-distance principle, the start of the item will align with the container's &lt;em&gt;contentStartOffset&lt;/em&gt;, or the end will align with the container's &lt;em&gt;contentEndOffset&lt;/em&gt;, ensuring the item is fully displayed. &lt;/p&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)--><!--Device-Scroller-scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | Index of the item to be scrolled to in the container. &lt;br&gt;&lt;em&gt;NOTE&lt;/em&gt; &lt;br&gt;If the value set is a negative value or greater than the maximum index of the items in the container, the value is deemed abnormal, and no scrolling will be performed. |
| smooth | boolean | No | Whether to enable the smooth animation for scrolling to the item with the specified index. The value &lt;em&gt;true&lt;/em&gt; means to enable that the smooth animation, and &lt;em&gt;false&lt;/em&gt; means the opposite.&lt;br&gt; Default value: &lt;em&gt;false&lt;/em&gt;<br>**Since:** 12 |
| align | [ScrollAlign](arkts-arkui-scrollalign-e.md) | No | How the list item to scroll to is aligned with the container. &lt;br&gt; Default value when the container is &lt;em&gt;List&lt;/em&gt;: &lt;em&gt;ScrollAlign.START&lt;/em&gt; &lt;br&gt; Default value when the container is &lt;em&gt;Grid&lt;/em&gt;: &lt;em&gt;ScrollAlign.AUTO&lt;/em&gt; &lt;br&gt; Default value when the container is &lt;em&gt;WaterFlow&lt;/em&gt;: &lt;em&gt;ScrollAlign.START&lt;/em&gt; &lt;br&gt;&lt;em&gt;NOTE&lt;/em&gt; &lt;br&gt;This parameter is only available for the &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components.<br>**Since:** 12 |
| options | [ScrollToIndexOptions](arkts-arkui-scrolltoindexoptions-i.md) | No | Options for scrolling to a specified index, for example, an extra offset for the scroll.&lt;br&gt;Default value: &lt;em&gt;0&lt;/em&gt;, in vp<br>**Since:** 12 |

