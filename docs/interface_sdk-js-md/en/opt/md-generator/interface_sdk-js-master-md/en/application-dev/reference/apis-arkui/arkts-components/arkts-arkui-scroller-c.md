# Scroller

Defines a controller for scrollable container components.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;1. The binding of a &lt;em&gt;Scroller&lt;/em&gt; instance to a scrollable container component occurs during the component creation phase.&lt;br&gt;2. &lt;em&gt;Scroller&lt;/em&gt; APIs can only be effectively called after the &lt;em&gt;Scroller&lt;/em&gt; instance is bound to a scrollable container component.Otherwise, depending on the API called, it may have no effect or throw an exception.&lt;br&gt;3. For example, with aboutToAppear, this callback is executed after a new instance of a custom component is created and before its &lt;em&gt;build()&lt;/em&gt; method is called.Therefore, if a scrollable component is defined within the &lt;em&gt;build&lt;/em&gt; method of a custom component,the internal scrollable component has not yet been created during the &lt;em&gt;aboutToAppear&lt;/em&gt; callback of that custom component, and therefore the &lt;em&gt;Scroller&lt;/em&gt; APIs cannot be called effectively.&lt;/p&gt;

**Since:** 7

<!--Device-unnamed-declare class Scroller--><!--Device-unnamed-declare class Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

A constructor used to create a &lt;em&gt;Scroller&lt;/em&gt; object.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-constructor()--><!--Device-Scroller-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentSize

```TypeScript
contentSize(): SizeResult
```

Obtains the content size.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Scroller-contentSize(): SizeResult--><!--Device-Scroller-contentSize(): SizeResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SizeResult](arkts-arkui-sizeresult-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [100004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100004-incorrect-route-name) |

## currentOffset

```TypeScript
currentOffset() : OffsetResult
```

Obtains the current scrolling offset.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;1. If &lt;em&gt;Scroller&lt;/em&gt; is not bound to a component, this API returns &lt;em&gt;undefined&lt;/em&gt;,which is not declared in the API. You are advised to use the &lt;em&gt;offset&lt;/em&gt; function.&lt;br&gt;2. The &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components use a lazy loading mechanism.Before all content is fully loaded and laid out, the total content offset is estimated, and this estimation may be inaccurate. For the &lt;em&gt;List&lt;/em&gt; component, the &lt;em&gt;childrenMainSize&lt;/em&gt; attribute can be used to mitigate such inaccuracies. Currently, there is no solution to inaccurate estimation of the&lt;em&gt;Grid&lt;/em&gt; and &lt;em&gt;WaterFlow&lt;/em&gt; components.&lt;/p&gt;

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-currentOffset() : OffsetResult--><!--Device-Scroller-currentOffset() : OffsetResult-End-->

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Scroller-fling(velocity: number): void--><!--Device-Scroller-fling(velocity: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| velocity | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100004-incorrect-route-name) |

## getFrameNode

```TypeScript
getFrameNode(): FrameNode | undefined
```

Obtains the FrameNode corresponding to this scroller.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Scroller-getFrameNode(): FrameNode | undefined--><!--Device-Scroller-getFrameNode(): FrameNode | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FrameNode](../arkts-apis/arkts-arkui-framenode-c.md) |

## getItemIndex

```TypeScript
getItemIndex(x: number, y: number): number
```

Obtains the index of a child component based on coordinates.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;The returned index is &lt;em&gt;-1&lt;/em&gt; for invalid coordinates.&lt;/p&gt;

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Scroller-getItemIndex(x: number, y: number): number--><!--Device-Scroller-getItemIndex(x: number, y: number): number-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100004-incorrect-route-name) |

## getItemRect

```TypeScript
getItemRect(index: number): RectResult
```

Obtains the size and position of a child component relative to its container.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area.Otherwise, the value is considered invalid.&lt;br&gt;- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area. Otherwise,the value is considered invalid.&lt;/p&gt;

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Scroller-getItemRect(index: number): RectResult--><!--Device-Scroller-getItemRect(index: number): RectResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RectResult](arkts-arkui-rectresult-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100004-incorrect-route-name) |

## isAtEnd

```TypeScript
isAtEnd(): boolean
```

Checks whether the component has scrolled to the bottom.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;This API is available for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;,and &lt;em&gt;WaterFlow&lt;/em&gt; components.&lt;/p&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-isAtEnd(): boolean--><!--Device-Scroller-isAtEnd(): boolean-End-->

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Scroller-offset() : OffsetResult | undefined--><!--Device-Scroller-offset() : OffsetResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OffsetResult](arkts-arkui-offsetresult-i.md) |

## scrollBy

```TypeScript
scrollBy(dx: Length, dy: Length)
```

Scrolls by the specified amount.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;This API is available for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;,and &lt;em&gt;WaterFlow&lt;/em&gt; components.&lt;/p&gt;

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollBy(dx: Length, dy: Length)--><!--Device-Scroller-scrollBy(dx: Length, dy: Length)-End-->

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

Scrolls to the edge of the container, regardless of the scroll axis direction.By default, the &lt;em&gt;Scroll&lt;/em&gt; component comes with an animation, while the &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;,and &lt;em&gt;WaterFlow&lt;/em&gt; components do not.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollEdge(value: Edge, options?: ScrollEdgeOptions)--><!--Device-Scroller-scrollEdge(value: Edge, options?: ScrollEdgeOptions)-End-->

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

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollPage(value: ScrollPageOptions)--><!--Device-Scroller-scrollPage(value: ScrollPageOptions)-End-->

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

**Deprecated since:** 9

**Substitutes:** [scrollPage](#scrollPage)

<!--Device-Scroller-scrollPage(value: { next: boolean; direction?: Axis })--><!--Device-Scroller-scrollPage(value: { next: boolean; direction?: Axis })-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | { next: boolean; direction?: Axis } | Yes |

## scrollTo

```TypeScript
scrollTo(options: ScrollOptions)
```

Scrolls to the specified position.Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;If the scrolling speed of the &lt;em&gt;scrollTo&lt;/em&gt; animation exceeds 200 vp/s, the components within the scrollable area will not respond to click events.&lt;/p&gt;

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollTo(options: ScrollOptions)--><!--Device-Scroller-scrollTo(options: ScrollOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ScrollOptions](arkts-arkui-scrolloptions-i.md) | Yes |

## scrollToIndex

```TypeScript
scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)
```

Scrolls to a specified index, with support for setting an extra offset for the scroll.When smooth scrolling is enabled, all items encountered during the scroll are loaded and their layout is calculated. Loading a large number of items may cause performance issues. It is recommended that you first call &lt;em&gt;scrollToIndex&lt;/em&gt; without animation to jump to a position near the target, then call it again with animation to smoothly scroll to the final target position.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;This API only works for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components.&lt;br&gt;When refreshing the data source using &lt;em&gt;LazyForEach&lt;/em&gt;, &lt;em&gt;ForEach&lt;/em&gt;, or &lt;em&gt;Repeat&lt;/em&gt;,ensure this API is called after the data refresh is complete.&lt;br&gt;Starting from API version 11, the &lt;em&gt;List&lt;/em&gt; component supports &lt;em&gt;contentStartOffset&lt;/em&gt;and &lt;em&gt;contentEndOffset&lt;/em&gt;. Starting from API version 22, the &lt;em&gt;Grid&lt;/em&gt; and &lt;em&gt;WaterFlow&lt;/em&gt;components also support setting &lt;em&gt;contentStartOffset&lt;/em&gt; and &lt;em&gt;contentEndOffset&lt;/em&gt;.&lt;br&gt;- If the scrollable container has &lt;em&gt;contentStartOffset&lt;/em&gt; set and &lt;em&gt;ScrollAlign&lt;/em&gt; is&lt;em&gt;START&lt;/em&gt;, after scrolling, the start of the specified item will align with the&lt;em&gt;contentStartOffset&lt;/em&gt; of the container.&lt;br&gt;- If the scrollable container has &lt;em&gt;contentEndOffset&lt;/em&gt; set and &lt;em&gt;ScrollAlign&lt;/em&gt; is&lt;em&gt;END&lt;/em&gt;, after scrolling, the end of the specified item will align with the&lt;em&gt;contentEndOffset&lt;/em&gt; of the container.&lt;br&gt;- If the scrollable container has &lt;em&gt;contentStartOffset&lt;/em&gt; or &lt;em&gt;contentEndOffset&lt;/em&gt; set and &lt;em&gt;ScrollAlign&lt;/em&gt; is &lt;em&gt;AUTO&lt;/em&gt;: When the specified item is completely within the visible area,no adjustment is made. Otherwise, following the shortest-scroll-distance principle, the start of the item will align with the container's &lt;em&gt;contentStartOffset&lt;/em&gt;, or the end will align with the container's&lt;em&gt;contentEndOffset&lt;/em&gt;, ensuring the item is fully displayed.&lt;/p&gt;

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)--><!--Device-Scroller-scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| [smooth](../arkts-apis/arkts-arkui-viewmodel-scrollparam-i.md) | boolean | No |
| align | [ScrollAlign](arkts-arkui-scrollalign-e.md) | No |
| options | [ScrollToIndexOptions](arkts-arkui-scrolltoindexoptions-i.md) | No |
