# scroll

## Summary

### Classes

| Name | Description |
| --- | --- |
| [Scroller](arkts-na-scroll-scroller-c.md) | Defines a controller for scrollable container components. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; <br>1. The binding of a &lt;em&gt;Scroller&lt;/em&gt; instance to a scrollable container component occurs during the component creation phase. <br>2. &lt;em&gt;Scroller&lt;/em&gt; APIs can only be effectively called after the &lt;em&gt;Scroller&lt;/em&gt; instance is bound to a scrollable container component. Otherwise, depending on the API called, it may have no effect or throw an exception. <br>3. For example, with aboutToAppear, this callback is executed after a new instance of a custom component is created and before its &lt;em&gt;build()&lt;/em&gt; method is called. Therefore, if a scrollable component is defined within the &lt;em&gt;build&lt;/em&gt; method of a custom component, the internal scrollable component has not yet been created during the &lt;em&gt;aboutToAppear&lt;/em&gt; callback of that custom component, and therefore the &lt;em&gt;Scroller&lt;/em&gt; APIs cannot be called effectively. &lt;/p&gt; |

### Interfaces

| Name | Description |
| --- | --- |
| [OffsetOptions](arkts-na-scroll-offsetoptions-i.md) | Provides parameters for setting the initial scrolling offset. |
| [OffsetResult](arkts-na-scroll-offsetresult-i.md) | Represents the offset values resulting from a scroll operation. |
| [OnScrollFrameBeginHandlerResult](arkts-na-scroll-onscrollframebeginhandlerresult-i.md) | The data returned by the event handler when onScrollFrameBegin. |
| [ScrollAnimationOptions](arkts-na-scroll-scrollanimationoptions-i.md) | Provides parameters for customizing scroll animations. |
| [ScrollEdgeOptions](arkts-na-scroll-scrolledgeoptions-i.md) | Provides parameters for scrolling to the edge of a scrollable container. |
| [ScrollOptions](arkts-na-scroll-scrolloptions-i.md) | Provides parameters for scrolling to a specific position in a scrollable container. |
| [ScrollPageOptions](arkts-na-scroll-scrollpageoptions-i.md) | Provides parameters for page scrolling behavior. |
| [ScrollSnapOptions](arkts-na-scroll-scrollsnapoptions-i.md) | Defines a scroll snapping mode object. |
| [ScrollToIndexOptions](arkts-na-scroll-scrolltoindexoptions-i.md) | Provides parameters for scrolling to a specific index. |
| [UIScrollEvent](arkts-na-scroll-uiscrollevent-i.md) | Defines a UIScrollableCommonEvent which is used to set different common event to target component. |

### Enums

| Name | Description |
| --- | --- |
| [ScrollAlign](arkts-na-scroll-scrollalign-e.md) | Enumerates alignment modes. |
| [ScrollDirection](arkts-na-scroll-scrolldirection-e.md) | Enumerates the scrolling directions. |

### Types

| Name | Description |
| --- | --- |
| [OnScrollEdgeCallback](arkts-na-onscrolledgecallback-t.md) | Represents the callback triggered when scrolling reaches an edge. |
| [OnScrollFrameBeginCallback](arkts-na-onscrollframebegincallback-t.md) | Represents the callback triggered before each frame scrolling starts. |
| [ScrollOnDidZoomCallback](arkts-na-scrollondidzoomcallback-t.md) | Called when the scaling of each frame is complete. |
| [ScrollOnScrollCallback](arkts-na-scrollonscrollcallback-t.md) | Represents the callback triggered when the &lt;em&gt;Scroll&lt;/em&gt; component scrolls. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;. <br>If the &lt;em&gt;onScrollFrameBegin&lt;/em&gt; event and &lt;em&gt;scrollBy&lt;/em&gt; method are used to implement nested scrolling, set the &lt;em&gt;edgeEffect&lt;/em&gt; attribute of the scrollable child component to &lt;em&gt;None&lt;/em&gt;. For example, if a &lt;em&gt;List&lt;/em&gt; is nested in the &lt;em&gt;Scroll&lt;/em&gt; component, &lt;em&gt;edgeEffect&lt;/em&gt; of the &lt;em&gt;List&lt;/em&gt; must be set to &lt;em&gt;EdgeEffect.None&lt;/em&gt;. &lt;/p&gt; |
| [ScrollOnWillScrollCallback](arkts-na-scrollonwillscrollcallback-t.md) | Called before scroll to allow developer to control real offset the Scroll can scroll. |

