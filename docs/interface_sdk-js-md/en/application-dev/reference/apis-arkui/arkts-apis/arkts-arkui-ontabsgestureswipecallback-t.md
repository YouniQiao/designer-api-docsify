# OnTabsGestureSwipeCallback

```TypeScript
export type OnTabsGestureSwipeCallback = (index: int, extraInfo: TabsAnimationEvent) => void
```

在页面跟手滑动过程中，逐帧触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTabsGestureSwipeCallback = (index: int, extraInfo: TabsAnimationEvent) => void--><!--Device-unnamed-export type OnTabsGestureSwipeCallback = (index: int, extraInfo: TabsAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 当前显示元素的索引，索引从0开始。 <br/> 取值范围为全体整数 取值限定为整数。 取值范围：[0, 索引值-1] |
| extraInfo | [TabsAnimationEvent](arkts-arkui-tabs-tabsanimationevent-i.md) | Yes | 动画相关信息，只返回主轴方向上当前显示元素相对于Tabs起始位置的位移。 |

