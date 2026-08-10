# OnTabsGestureSwipeCallback

```TypeScript
declare type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void
```

在页面跟手滑动过程中，逐帧触发的回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void--><!--Device-unnamed-declare type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 当前显示元素的索引，索引从0开始。 <br/>取值范围：[0, 页签总数-1] |
| extraInfo | [TabsAnimationEvent](../arkts-apis/arkts-arkui-tabs-tabsanimationevent-i.md) | Yes | 动画相关信息，只返回主轴方向上当前显示元素相对于Tabs起始位置的位移。 |

