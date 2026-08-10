# ScrollOnScrollCallback

```TypeScript
export type ScrollOnScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState) => void
```

Scroll滚动时触发的回调。  
> **说明：**
> 若通过[onScrollFrameBegin](onScrollFrameBegin)事件和[scrollBy](../arkts-components/arkts-arkui-scroller-c.md/arkts-arkui-scroller-c.md#scrollby)方法实现容器嵌套滚动，需设置子滚动节点的
> EdgeEffect为None。如Scroll嵌套List滚动时，List组件的[edgeEffect](../../../reference/apis-arkui/arkui-ts/ts-container-list.md#edgeeffect)
> 属性需设置为EdgeEffect.None。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ScrollOnScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState) => void--><!--Device-unnamed-export type ScrollOnScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xOffset | double | Yes | 相对于上一帧水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。<br/>单位vp。 <br>单位:vp。 <br>单位:vp。 |
| yOffset | double | Yes | 相对于上一帧竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。<br/>单位vp。 <br>单位:vp。 <br>单位:vp。 |
| scrollState | [ScrollState](../arkts-components/arkts-arkui-scrollstate-e.md) | Yes | 当前滚动状态。 |

