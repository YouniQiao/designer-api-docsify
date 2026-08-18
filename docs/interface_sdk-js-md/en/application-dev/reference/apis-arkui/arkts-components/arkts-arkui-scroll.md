# Scroll

Defines Scroll Component.

## Scroll

```TypeScript
Scroll(scroller?: Scroller)
```

Called when a scrollable container is set.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollInterface-(scroller?: Scroller): ScrollAttribute--><!--Device-ScrollInterface-(scroller?: Scroller): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](arkts-arkui-scroller-c.md) | No |  |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [OffsetOptions](arkts-arkui-offsetoptions-i.md) | Provides parameters for setting the initial scrolling offset. |
| [OffsetResult](arkts-arkui-offsetresult-i.md) | Represents the offset values resulting from a scroll operation. |
| [OnScrollFrameBeginHandlerResult](arkts-arkui-onscrollframebeginhandlerresult-i.md) | The data returned by the event handler when onScrollFrameBegin. |
| [ScrollAnimationOptions](arkts-arkui-scrollanimationoptions-i.md) | Provides parameters for customizing scroll animations. |
| [ScrollEdgeOptions](arkts-arkui-scrolledgeoptions-i.md) | Provides parameters for scrolling to the edge of a scrollable container. |
| [ScrollOptions](arkts-arkui-scrolloptions-i.md) | Provides parameters for scrolling to a specific position in a scrollable container. |
| [ScrollPageOptions](arkts-arkui-scrollpageoptions-i.md) | Provides parameters for page scrolling behavior. |
| [ScrollSnapOptions](arkts-arkui-scrollsnapoptions-i.md) | Defines a scroll snapping mode object. |
| [ScrollToIndexOptions](arkts-arkui-scrolltoindexoptions-i.md) | Provides parameters for scrolling to a specific index. |
| [UIScrollEvent](arkts-arkui-uiscrollevent-i.md) | Defines a UIScrollableCommonEvent which is used to set different common event to target component. |

### Types

| Name | Description |
| --- | --- |
| [OnScrollEdgeCallback](arkts-arkui-onscrolledgecallback-t.md) | Represents the callback triggered when scrolling reaches an edge. |
| [OnScrollFrameBeginCallback](arkts-arkui-onscrollframebegincallback-t.md) | Represents the callback triggered before each frame scrolling starts. |
| [ScrollOnDidZoomCallback](arkts-arkui-scrollondidzoomcallback-t.md) | callback of Scroll, using in onDidZoom. |
| [ScrollOnScrollCallback](arkts-arkui-scrollonscrollcallback-t.md) | Represents the callback triggered when the &lt;em&gt;Scroll&lt;/em&gt; component scrolls. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>If the &lt;em&gt;onScrollFrameBegin&lt;/em&gt; event and &lt;em&gt;scrollBy&lt;/em&gt; method are used to implement nested scrolling, set the &lt;em&gt;edgeEffect&lt;/em&gt; attribute of the scrollable child component to &lt;em&gt;None&lt;/em&gt;. For example, if a &lt;em&gt;List&lt;/em&gt; is nested in the &lt;em&gt;Scroll&lt;/em&gt; component, &lt;em&gt;edgeEffect&lt;/em&gt; of the &lt;em&gt;List&lt;/em&gt; must be set to &lt;em&gt;EdgeEffect.None&lt;/em&gt;. &lt;/p&gt; |
| [ScrollOnWillScrollCallback](arkts-arkui-scrollonwillscrollcallback-t.md) | Called before scroll to allow developer to control real offset the Scroll can scroll. |

### Enums

| Name | Description |
| --- | --- |
| [ScrollAlign](arkts-arkui-scrollalign-e.md) | Enumerates alignment modes. |
| [ScrollDirection](arkts-arkui-scrolldirection-e.md) | Enumerates the scrolling directions. |

