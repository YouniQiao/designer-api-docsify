# Scroller

Defines a controller for scrollable container components. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. The binding of a &lt;em&gt;Scroller&lt;/em&gt; instance to a scrollable container component occurs during the component creation phase. <br>2. &lt;em&gt;Scroller&lt;/em&gt; APIs can only be effectively called after the &lt;em&gt;Scroller&lt;/em&gt; instance is bound to a scrollable container component. Otherwise, depending on the API called, it may have no effect or throw an exception. <br>3. For example, with aboutToAppear, this callback is executed after a new instance of a custom component is created and before its &lt;em&gt;build()&lt;/em&gt; method is called. Therefore, if a scrollable component is defined within the &lt;em&gt;build&lt;/em&gt; method of a custom component, the internal scrollable component has not yet been created during the &lt;em&gt;aboutToAppear&lt;/em&gt; callback of that custom component, and therefore the &lt;em&gt;Scroller&lt;/em&gt; APIs cannot be called effectively. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class Scroller--><!--Device-unnamed-export declare class Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

A constructor used to create a &lt;em&gt;Scroller&lt;/em&gt; object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-constructor()--><!--Device-Scroller-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentSize

```TypeScript
contentSize() : SizeResult
```

Obtains the content size.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-contentSize() : SizeResult--><!--Device-Scroller-contentSize() : SizeResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [SizeResult](../../apis-arkui/arkts-components/arkts-arkui-sizeresult-i.md) | Returns the content size. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100004](../../apis-arkui/errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## currentOffset

```TypeScript
currentOffset(): OffsetResult | undefined
```

Obtains the current scrolling offset.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-currentOffset(): OffsetResult | undefined--><!--Device-Scroller-currentOffset(): OffsetResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OffsetResult](arkts-na-scroll-offsetresult-i.md) | Returns the current scrolling offset. If the scroller not bound to a component, the return value is undefined. |

## fling

```TypeScript
fling(velocity: double): void
```

Performs inertial scrolling based on the initial velocity passed in.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-fling(velocity: double): void--><!--Device-Scroller-fling(velocity: double): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | double | Yes | Initial velocity of inertial scrolling. <br>Unit: vp/s. <br>&lt;em&gt;NOTE&lt;/em&gt; <br>If the value specified is 0, it is considered as invalid, and the scrolling for this instance will not take effect. A positive value indicates scrolling towards the top, while a negative value indicates scrolling towards the bottom. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100004](../../apis-arkui/errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## getFrameNode

```TypeScript
getFrameNode(): FrameNode | undefined
```

Obtains the FrameNode corresponding to this scroller.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-getFrameNode(): FrameNode | undefined--><!--Device-Scroller-getFrameNode(): FrameNode | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| FrameNode | Returns the FrameNode bound to this scroller. If the scroller is not bound to a component, the return value is undefined. |

## getItemIndex

```TypeScript
getItemIndex(x: double, y: double): int
```

Obtains the index of a child component based on coordinates. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>The returned index is &lt;em&gt;-1&lt;/em&gt; for invalid coordinates. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-getItemIndex(x: double, y: double): int--><!--Device-Scroller-getItemIndex(x: double, y: double): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X-coordinate, in vp. |
| y | double | Yes | Y-coordinate, in vp. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Index of the item. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100004](../../apis-arkui/errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## getItemRect

```TypeScript
getItemRect(index: int): RectResult
```

Obtains the size and position of a child component relative to its container. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area. Otherwise, the value is considered invalid. <br>- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area. Otherwise, the value is considered invalid. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-getItemRect(index: int): RectResult--><!--Device-Scroller-getItemRect(index: int): RectResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the target child component. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [RectResult](../../apis-arkui/arkts-components/arkts-arkui-rectresult-i.md) | Returns the size and position. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100004](../../apis-arkui/errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## isAtEnd

```TypeScript
isAtEnd(): boolean
```

Checks whether the component has scrolled to the bottom. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>This API is available for the &lt;em&gt;ArcList&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-isAtEnd(): boolean--><!--Device-Scroller-isAtEnd(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns whether the component scrolls to the end position. |

## offset

```TypeScript
offset(): OffsetResult | undefined
```

Obtains the current scrolling offset.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-offset(): OffsetResult | undefined--><!--Device-Scroller-offset(): OffsetResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OffsetResult](arkts-na-scroll-offsetresult-i.md) | Returns the current scrolling offset. If the scroller not bound to a component, the return value is undefined. |

## scrollBy

```TypeScript
scrollBy(dx: Length, dy: Length): void
```

Called when the setting slides by offset.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-scrollBy(dx: Length, dy: Length): void--><!--Device-Scroller-scrollBy(dx: Length, dy: Length): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) | Yes |  |
| dy | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) | Yes |  |

## scrollEdge

```TypeScript
scrollEdge(value: Edge, options?: ScrollEdgeOptions): void
```

Called when scrolling to the edge of the container.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-scrollEdge(value: Edge, options?: ScrollEdgeOptions): void--><!--Device-Scroller-scrollEdge(value: Edge, options?: ScrollEdgeOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Edge](../../apis-arkui/arkts-apis/arkts-arkui-edge-e.md) | Yes | Edge type of the container. |
| options | [ScrollEdgeOptions](arkts-na-scroll-scrolledgeoptions-i.md) | No | Options of scrolling to edge. |

## scrollPage

```TypeScript
scrollPage(value: ScrollPageOptions): void
```

Called when page turning mode is set.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-scrollPage(value: ScrollPageOptions): void--><!--Device-Scroller-scrollPage(value: ScrollPageOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollPageOptions](arkts-na-scroll-scrollpageoptions-i.md) | Yes |  |

## scrollTo

```TypeScript
scrollTo(options: ScrollOptions): void
```

Called when the setting slides to the specified position.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-scrollTo(options: ScrollOptions): void--><!--Device-Scroller-scrollTo(options: ScrollOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ScrollOptions](arkts-na-scroll-scrolloptions-i.md) | Yes | scroll options |

## scrollToIndex

```TypeScript
scrollToIndex(value: int, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions): void
```

Scroll to the specified index.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Scroller-scrollToIndex(value: int, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions): void--><!--Device-Scroller-scrollToIndex(value: int, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | Index to jump to. <br>The value should be an integer. |
| smooth | boolean | No | If true, scroll to index item with animation. If false, scroll to index item without animation. |
| align | [ScrollAlign](arkts-na-scroll-scrollalign-e.md) | No | Sets the alignment mode of a specified index. |
| options | [ScrollToIndexOptions](arkts-na-scroll-scrolltoindexoptions-i.md) | No | Sets the options of a specified index, such as extra offset. <br>Unit: vp. Default value: 0 (unit:vp). |

