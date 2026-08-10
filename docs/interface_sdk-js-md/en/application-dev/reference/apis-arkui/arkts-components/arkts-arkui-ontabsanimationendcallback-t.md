# OnTabsAnimationEndCallback

```TypeScript
declare type OnTabsAnimationEndCallback = (index: number, extraInfo: TabsAnimationEvent) => void
```

切换动画结束时触发的回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnTabsAnimationEndCallback = (index: number, extraInfo: TabsAnimationEvent) => void--><!--Device-unnamed-declare type OnTabsAnimationEndCallback = (index: number, extraInfo: TabsAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 当前显示元素的索引，索引从0开始。 |
| extraInfo | [TabsAnimationEvent](../arkts-apis/arkts-arkui-tabs-tabsanimationevent-i.md) | Yes | 动画相关信息，只返回主轴方向上当前显示元素相对于Tabs起始位置的位移。 |

