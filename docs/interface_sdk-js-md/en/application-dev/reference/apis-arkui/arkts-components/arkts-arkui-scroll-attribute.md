# Scroll properties/events

Defines the scroll attribute functions.

**Inheritance/Implementation:** ScrollAttribute extends ScrollableCommonMethod<ScrollAttribute>

**Since:** 7

<!--Device-unnamed-declare class ScrollAttribute--><!--Device-unnamed-declare class ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## edgeEffect

```TypeScript
edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions)
```

Sets the effect used when the scroll boundary is reached.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): ScrollAttribute--><!--Device-ScrollAttribute-edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| edgeEffect | EdgeEffect | Yes | Effect used when the scroll boundary is reached. The spring and shadow effects are supported. <br>Default value: &lt;em&gt;EdgeEffect.None&lt;/em&gt; |
| options | EdgeEffectOptions | No | Whether to enable the scroll effect when the component content is smaller than the component itself. The value &lt;em&gt;{ alwaysEnabled: true }&lt;/em&gt; means to enable the scroll effect, and &lt;em&gt;{ alwaysEnabled: false } &lt;/em&gt; means the opposite. <br>Default value: &lt;em&gt;{ alwaysEnabled: true }&lt;/em&gt;<br>**Since:** 11 |

## enableBouncesZoom

```TypeScript
enableBouncesZoom(enable: boolean)
```

Enable bounces zoom scale.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollAttribute-enableBouncesZoom(enable: boolean): ScrollAttribute--><!--Device-ScrollAttribute-enableBouncesZoom(enable: boolean): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Enable bounces zoom scale. <br>Default value: true. |

## enablePaging

```TypeScript
enablePaging(value: boolean)
```

Sets whether to enable the swipe-to-turn-pages feature. If both &lt;em&gt;enablePaging&lt;/em&gt; and &lt;em&gt;scrollSnap&lt;/em&gt; are set, &lt;em&gt;scrollSnap&lt;/em&gt; takes effect, but &lt;em&gt;enablePaging&lt;/em&gt; does not.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollAttribute-enablePaging(value: boolean): ScrollAttribute--><!--Device-ScrollAttribute-enablePaging(value: boolean): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to enable the swipe-to-turn-pages feature. Default value: false. The value &lt;em&gt;true&lt;/em&gt; means to enable the swipe-to-turn-pages feature, and &lt;em&gt;false&lt;/em&gt; means the opposite. |

## enableScrollInteraction

```TypeScript
enableScrollInteraction(value: boolean)
```

Sets whether to support scroll gestures. When this attribute is set to &lt;em&gt;false&lt;/em&gt;, scrolling by finger or mouse is not supported, but the scroll controller API is not affected. The component cannot be scrolled by dragging the mouse.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-enableScrollInteraction(value: boolean): ScrollAttribute--><!--Device-ScrollAttribute-enableScrollInteraction(value: boolean): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to support scroll gestures.<br>Default value: &lt;em&gt;true&lt;/em&gt; |

## friction

```TypeScript
friction(value: number | Resource)
```

Sets the friction coefficient. It applies only to gestures in the scrolling area, and it affects only indirectly the scroll chaining during the inertial scrolling process. If this attribute is set to a value less than or equal to 0, the default value is used.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-friction(value: number | Resource): ScrollAttribute--><!--Device-ScrollAttribute-friction(value: number | Resource): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| Resource | Yes | Friction coefficient. <br>Default value: &lt;em&gt;0.9&lt;/em&gt; for wearable devices and &lt;em&gt;0.6&lt;/em&gt; for non-wearable devices <br>Since API version 11, the default value for non-wearable devices is &lt;em&gt;0.7&lt;/em&gt;. <br>Since API version 12, the default value for non-wearable devices is &lt;em&gt;0.75&lt;/em&gt;. |

## initialOffset

```TypeScript
initialOffset(value: OffsetOptions)
```

Sets the initial scrolling offset. This attribute takes effect only during the initial layout of the component. After the initial layout, dynamically changing the value of this attribute does not have any effect.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollAttribute-initialOffset(value: OffsetOptions): ScrollAttribute--><!--Device-ScrollAttribute-initialOffset(value: OffsetOptions): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [OffsetOptions](arkts-arkui-offsetoptions-i.md) | Yes | Initial scrolling offset. When the value specified is a percentage, the initial scrolling offset is calculated as the product of the &lt;em&gt;Scroll&lt;/em&gt; component's size in the main axis direction and the percentage value. |

## maxZoomScale

```TypeScript
maxZoomScale(scale: number)
```

Set maximum zoom scale.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollAttribute-maxZoomScale(scale: number): ScrollAttribute--><!--Device-ScrollAttribute-maxZoomScale(scale: number): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | number | Yes | Set maximum zoom scale. <br>Default value: 1. <br>Value range: (0, +∞). If this parameter is set to a value less than or equal to 0, the default value is used. |

## minZoomScale

```TypeScript
minZoomScale(scale: number)
```

Set minimum zoom scale. Setting either &lt;em&gt;maxZoomScale&lt;/em&gt; and &lt;em&gt;minZoomScale&lt;/em&gt; to a value other than 1 automatically enables the zoom gesture.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollAttribute-minZoomScale(scale: number): ScrollAttribute--><!--Device-ScrollAttribute-minZoomScale(scale: number): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | number | Yes | Set minimum zoom scale. <br>Default value: 1. <br>Value range: (0, maxZoomScale]. If the value is greater than &lt;em&gt;maxZoomScale&lt;/em&gt;, &lt;em&gt;maxZoomScale&lt;/em&gt; is used. |

## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions)
```

Sets the nested scrolling options. You can set the nested scrolling mode in the forward and backward directions to implement scrolling linkage with the parent component. Nested scrolling will not take effect when both of the following conditions are met: (1) The child &lt;em&gt;Scroll&lt;/em&gt; component has &lt;em&gt;enablePaging&lt;/em&gt; or &lt;em&gt;scrollSnap&lt;/em&gt; enabled. (2) The parent component is configured to have scrolling priority.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-nestedScroll(value: NestedScrollOptions): ScrollAttribute--><!--Device-ScrollAttribute-nestedScroll(value: NestedScrollOptions): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | NestedScrollOptions | Yes | Nested scrolling options. <br>Default value: &lt;em&gt;{ scrollForward: NestedScrollMode.SELF_ONLY, scrollBackward: NestedScrollMode.SELF_ONLY }&lt;/em&gt; |

## onDidScroll

```TypeScript
onDidScroll(handler: ScrollOnScrollCallback)
```

Triggered when the Scroll component scrolls.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. This event is triggered when scrolling is started by the &lt;em&gt;Scroll&lt;/em&gt; component or other input settings, such as keyboard and mouse operations. <br>2. This event is triggered when the controller API is called. <br>3. This event supports the out-of-bounds bounce effect. &lt;/p&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollAttribute-onDidScroll(handler: ScrollOnScrollCallback): ScrollAttribute--><!--Device-ScrollAttribute-onDidScroll(handler: ScrollOnScrollCallback): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [ScrollOnScrollCallback](arkts-arkui-scrollonscrollcallback-t.md) | Yes | Callback triggered when the &lt;em&gt;Scroll&lt;/em&gt; component scrolls. |

## onDidZoom

```TypeScript
onDidZoom(event: ScrollOnDidZoomCallback)
```

Called when the Scroll did zoom.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollAttribute-onDidZoom(event: ScrollOnDidZoomCallback): ScrollAttribute--><!--Device-ScrollAttribute-onDidZoom(event: ScrollOnDidZoomCallback): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [ScrollOnDidZoomCallback](arkts-arkui-scrollondidzoomcallback-t.md) | Yes | callback of zoom. |

## onScroll

```TypeScript
onScroll(event: (xOffset: number, yOffset: number) => void)
```

Triggered to return the horizontal and vertical offsets, in vp, during scrolling when the specified scroll event occurs.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. This event is triggered when scrolling is started by the &lt;em&gt;Scroll&lt;/em&gt; component or other input settings, such as keyboard and mouse operations. <br>2. This event is triggered when the controller API is called. <br>3. This event supports the out-of-bounds bounce effect. &lt;/p&gt;

**Since:** 7

**Deprecated since:** 12

**Substitutes:** onWillScroll

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-onScroll(event: (xOffset: number, yOffset: number) => void): ScrollAttribute--><!--Device-ScrollAttribute-onScroll(event: (xOffset: number, yOffset: number) => void): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (xOffset: number, yOffset: number) =&gt; void | Yes | callback when scroll, xOffset: Actual scroll offset relative to the previous frame.<br>Unit: vp yOffset: Vertical offset relative to the previous frame. A positive offset indicates scrolling upward, and a negative offset indicates scrolling downward.<br>Unit: vp |

## onScrollEdge

```TypeScript
onScrollEdge(event: OnScrollEdgeCallback)
```

Triggered when scrolling reaches the edge. Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. This event is triggered when scrolling reaches the edge after being started by the &lt;em&gt;Scroll&lt;/em&gt; component or other input settings, such as keyboard and mouse operations. <br>2. This event is triggered when the controller API is called. <br>3. This event supports the out-of-bounds bounce effect. &lt;/p&gt;

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-onScrollEdge(event: OnScrollEdgeCallback): ScrollAttribute--><!--Device-ScrollAttribute-onScrollEdge(event: OnScrollEdgeCallback): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [OnScrollEdgeCallback](arkts-arkui-onscrolledgecallback-t.md) | Yes | Edge position to scroll to.<br>**Since:** 18 |

## onScrollEnd

```TypeScript
onScrollEnd(event: () => void)
```

Triggered when scrolling stops.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. This event is triggered when scrolling is stopped by the &lt;em&gt;Scroll&lt;/em&gt; component or other input settings, such as keyboard and mouse operations. <br>2. This event is triggered when the controller API is called, accompanied by a transition animation. &lt;/p&gt;

**Since:** 7

**Deprecated since:** 9

**Substitutes:** onScrollStop

<!--Device-ScrollAttribute-onScrollEnd(event: () => void): ScrollAttribute--><!--Device-ScrollAttribute-onScrollEnd(event: () => void): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | () =&gt; void | Yes |  |

## onScrollFrameBegin

```TypeScript
onScrollFrameBegin(event: OnScrollFrameBeginCallback)
```

Triggered when each frame scrolling starts. Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>This event is triggered when any of the following conditions is met: <br>1. Scrolling is initiated by user interaction (for example, finger swipe, keyboard, or mouse operation). <br>2. The &lt;em&gt;Scroll&lt;/em&gt; component scrolls by inertia. <br>3. Scrolling is triggered by calling the &lt;em&gt;fling&lt;/em&gt; API. <br>This event is not triggered when any of the following conditions is met: <br>1. A scroll control API other than &lt;em&gt;fling&lt;/em&gt; is called. <br>2. The out-of-bounds bounce effect is active. <br>3. The scrollbar is dragged. &lt;/p&gt;

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback): ScrollAttribute--><!--Device-ScrollAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](arkts-arkui-onscrollframebegincallback-t.md) | Yes | Callback triggered when each frame scrolling starts.<br>**Since:** 18 |

## onScrollStart

```TypeScript
onScrollStart(event: VoidCallback)
```

Called when scrolling start. Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. This event is triggered when scrolling is started by the &lt;em&gt;Scroll&lt;/em&gt; component or other input settings, such as keyboard and mouse operations. <br>2. This event is triggered when the controller API is called, accompanied by a transition animation. &lt;/p&gt;

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-onScrollStart(event: VoidCallback): ScrollAttribute--><!--Device-ScrollAttribute-onScrollStart(event: VoidCallback): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | VoidCallback | Yes | Callback triggered when scrolling starts.<br>**Since:** 18 |

## onScrollStop

```TypeScript
onScrollStop(event: VoidCallback)
```

Called when scrolling has stopped. Anonymous Object Rectification.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. This event is triggered when scrolling is stopped by the &lt;em&gt;Scroll&lt;/em&gt; component or other input settings, such as keyboard and mouse operations. <br>2. This event is triggered when the controller API is called, accompanied by a transition animation. &lt;/p&gt;

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-onScrollStop(event: VoidCallback): ScrollAttribute--><!--Device-ScrollAttribute-onScrollStop(event: VoidCallback): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | VoidCallback | Yes | Callback triggered when scrolling stops.<br>**Since:** 18 |

## onWillScroll

```TypeScript
onWillScroll(handler: ScrollOnWillScrollCallback)
```

Triggered before scrolling.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. This event is triggered when scrolling is started by the &lt;em&gt;Scroll&lt;/em&gt; component or other input settings, such as keyboard and mouse operations. <br>2. This event is triggered when the controller API is called. <br>3. This event supports the out-of-bounds bounce effect. &lt;/p&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollAttribute-onWillScroll(handler: ScrollOnWillScrollCallback): ScrollAttribute--><!--Device-ScrollAttribute-onWillScroll(handler: ScrollOnWillScrollCallback): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [ScrollOnWillScrollCallback](arkts-arkui-scrollonwillscrollcallback-t.md) | Yes | Callback triggered before scrolling. |

## onZoomStart

```TypeScript
onZoomStart(event: VoidCallback)
```

Called when zooming has stated.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollAttribute-onZoomStart(event: VoidCallback): ScrollAttribute--><!--Device-ScrollAttribute-onZoomStart(event: VoidCallback): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | VoidCallback | Yes | Zoom start callback. |

## onZoomStop

```TypeScript
onZoomStop(event: VoidCallback)
```

Called when zooming has stopped.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollAttribute-onZoomStop(event: VoidCallback): ScrollAttribute--><!--Device-ScrollAttribute-onZoomStop(event: VoidCallback): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | VoidCallback | Yes | Zoom stop callback. |

## scrollBar

```TypeScript
scrollBar(barState: BarState)
```

Sets the scrollbar state. If the container component cannot be scrolled, the scrollbar is not displayed. If the size of a child component of a container component is infinite, the scrollbar cannot be dragged or scrolled with the child component. Since API version 10, when the scrollable component has rounded corners, to prevent the scrollbar from being cut off by the corners, the scrollbar will automatically calculate the clearance distance from the top and bottom.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-scrollBar(barState: BarState): ScrollAttribute--><!--Device-ScrollAttribute-scrollBar(barState: BarState): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| barState | BarState | Yes | Scrollbar state.<br>Default value: &lt;em&gt;BarState.Auto&lt;/em&gt; |

## scrollBarColor

```TypeScript
scrollBarColor(color: Color | number | string)
```

Sets the scrollbar color.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-scrollBarColor(color: Color | number | string): ScrollAttribute--><!--Device-ScrollAttribute-scrollBarColor(color: Color | number | string): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Color \| number \| string | Yes | Scrollbar color.<br>Default value: &lt;em&gt;'\#182431'&lt;/em&gt; (40% opacity) |

## scrollBarColor

```TypeScript
scrollBarColor(color: Color | number | string | Resource)
```

Sets the scrollbar color.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ScrollAttribute-scrollBarColor(color: Color | number | string | Resource): ScrollAttribute--><!--Device-ScrollAttribute-scrollBarColor(color: Color | number | string | Resource): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Color \| number \| string \| Resource | Yes | Scrollbar color. <br>Default value: &lt;em&gt;'\#182431'&lt;/em&gt; (40% opacity) <br>A number value indicates a HEX color in RGB or ARGB format, for example, &lt;em&gt;0xffffff&lt;/em&gt;. A string value indicates a color in RGB or ARGB format, for example, &lt;em&gt;'#ffffff'&lt;/em&gt;. |

## scrollBarWidth

```TypeScript
scrollBarWidth(value: number | string)
```

Sets the scrollbar width.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-scrollBarWidth(value: number | string): ScrollAttribute--><!--Device-ScrollAttribute-scrollBarWidth(value: number | string): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string | Yes | Scrollbar width.<br>Default value: &lt;em&gt;4&lt;/em&gt; <br>Unit: vp <br>Values less than 0 are treated as the default value. The value &lt;em&gt;0&lt;/em&gt; means not to show the scrollbar. |

## scrollBarWidth

```TypeScript
scrollBarWidth(value: number | string | Resource)
```

Sets the scrollbar width.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollAttribute-scrollBarWidth(value: number | string | Resource): ScrollAttribute--><!--Device-ScrollAttribute-scrollBarWidth(value: number | string | Resource): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string \| Resource | Yes | Scrollbar width. <br>Unit: vp <br>Default value: &lt;em&gt;4&lt;/em&gt; <br>If this parameter is set to a value less than or equal to 0, the default value is used. The value &lt;em&gt;0&lt;/em&gt; means not to show the scrollbar. |

## scrollSnap

```TypeScript
scrollSnap(value: ScrollSnapOptions)
```

Sets the scroll snapping mode. During the snap animation, the scroll operation source type reported by the &lt;em&gt;onWillScroll&lt;/em&gt; event is &lt;em&gt;ScrollSource.FLING&lt;/em&gt;.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-scrollSnap(value: ScrollSnapOptions): ScrollAttribute--><!--Device-ScrollAttribute-scrollSnap(value: ScrollSnapOptions): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollSnapOptions](arkts-arkui-scrollsnapoptions-i.md) | Yes | Scroll snapping mode. |

## scrollable

```TypeScript
scrollable(value: ScrollDirection)
```

Sets the scrolling direction. The scroll offset is reset when this value is changed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollAttribute-scrollable(value: ScrollDirection): ScrollAttribute--><!--Device-ScrollAttribute-scrollable(value: ScrollDirection): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollDirection](arkts-arkui-scrolldirection-e.md) | Yes | Scrolling direction.<br>Default value: &lt;em&gt;ScrollDirection.Vertical&lt;/em&gt; |

## zoomScale

```TypeScript
zoomScale(scale: number)
```

Current zoom scale. This parameter supports !! for two-way binding of variables.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollAttribute-zoomScale(scale: number): ScrollAttribute--><!--Device-ScrollAttribute-zoomScale(scale: number): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | number | Yes | Current zoom scale. <br>Default value: 1. <br>Value range: (0, +∞). |

