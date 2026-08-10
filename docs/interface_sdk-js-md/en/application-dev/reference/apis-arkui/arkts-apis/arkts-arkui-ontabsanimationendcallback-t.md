# OnTabsAnimationEndCallback

```TypeScript
export type OnTabsAnimationEndCallback = (index: int, extraInfo: TabsAnimationEvent) => void
```

切换动画结束时触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTabsAnimationEndCallback = (index: int, extraInfo: TabsAnimationEvent) => void--><!--Device-unnamed-export type OnTabsAnimationEndCallback = (index: int, extraInfo: TabsAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 当前显示元素的索引，索引从0开始。 取值范围为全体整数 取值限定为整数。 |
| extraInfo | [TabsAnimationEvent](arkts-arkui-tabs-tabsanimationevent-i.md) | Yes | 动画相关信息，只返回主轴方向上当前显示元素相对于Tabs起始位置的位移。 |

