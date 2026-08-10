# scroll

## Summary

### Classes

| Name | Description |
| --- | --- |
| [Scroller](arkts-arkui-scroll-scroller-c.md) | 可滚动容器组件的控制器，可以将此组件绑定至容器组件，然后通过它控制容器组件的滚动。同一个控制器不可以控制多个容器组件，目前支持绑定到[ArcList](arkts-arkui-arclist.md)、  [ArcScrollBar](arkts-arkui-arcscrollbar.md)、[List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md/arkts-arkts-util-list-list-c.md)、Scroll、[ScrollBar](scroll_bar)、  [Grid](arkts-arkui-grid-grid-f.md#grid)、[WaterFlow](water_flow)上。 |

### Interfaces

| Name | Description |
| --- | --- |
| [OffsetOptions](arkts-arkui-scroll-offsetoptions-i.md) | 初始滚动偏移量的参数选项。 |
| [OffsetResult](arkts-arkui-scroll-offsetresult-i.md) | 滑动偏移量对象。 |
| [OnScrollFrameBeginHandlerResult](arkts-arkui-scroll-onscrollframebeginhandlerresult-i.md) | [OnScrollFrameBeginCallback]返回的实际相对上一帧滚动偏移量。 |
| [ScrollAnimationOptions](arkts-arkui-scroll-scrollanimationoptions-i.md) | 自定义滚动动效的参数选项。 |
| [ScrollEdgeOptions](arkts-arkui-scroll-scrolledgeoptions-i.md) | 滚动到边缘位置的参数选项。 |
| [ScrollOptions](arkts-arkui-scroll-scrolloptions-i.md) | 滚动到指定位置的参数选项。 |
| [ScrollPageOptions](arkts-arkui-scroll-scrollpageoptions-i.md) | 翻页模式的参数选项。 |
| [ScrollSnapOptions](arkts-arkui-scroll-scrollsnapoptions-i.md) | 限位滚动模式对象。 |
| [ScrollToIndexOptions](arkts-arkui-scroll-scrolltoindexoptions-i.md) | 滑动到指定Index的参数选项。 |
| [UIScrollEvent](arkts-arkui-scroll-uiscrollevent-i.md) | frameNode中[getEvent('Scroll')](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#geteventscroll19)方法的返回值，可用于给Scroll节点设置滚动事件。  UIScrollEvent继承于[UIScrollableCommonEvent](arkts-arkui-common-uiscrollablecommonevent-i.md)。 |

### Enums

| Name | Description |
| --- | --- |
| [ScrollAlign](arkts-arkui-scroll-scrollalign-e.md) | 对齐方式枚举。 |
| [ScrollDirection](arkts-arkui-scroll-scrolldirection-e.md) | 滚动方向枚举。 |

### Types

| Name | Description |
| --- | --- |
| [OnScrollEdgeCallback](arkts-arkui-onscrolledgecallback-t.md) | 滚动到边缘时触发的回调。 |
| [OnScrollFrameBeginCallback](arkts-arkui-onscrollframebegincallback-t.md) | Scroll每帧滚动前触发的回调。 |
| [ScrollOnDidZoomCallback](arkts-arkui-scrollondidzoomcallback-t.md) | Scroll每帧缩放完成时触发的回调。 |
| [ScrollOnScrollCallback](arkts-arkui-scrollonscrollcallback-t.md) | Scroll滚动时触发的回调。 |
| [ScrollOnWillScrollCallback](arkts-arkui-scrollonwillscrollcallback-t.md) | Scroll滚动前触发的回调。 |

