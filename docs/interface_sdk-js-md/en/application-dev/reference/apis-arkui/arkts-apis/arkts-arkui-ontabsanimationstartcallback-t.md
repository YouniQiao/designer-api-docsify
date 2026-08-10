# OnTabsAnimationStartCallback

```TypeScript
export type OnTabsAnimationStartCallback = (index: int, targetIndex: int, extraInfo: TabsAnimationEvent) => void
```

切换动画开始时触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTabsAnimationStartCallback = (index: int, targetIndex: int, extraInfo: TabsAnimationEvent) => void--><!--Device-unnamed-export type OnTabsAnimationStartCallback = (index: int, targetIndex: int, extraInfo: TabsAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 当前显示元素的索引，索引从0开始。 取值范围为全体整数 取值限定为整数。 |
| targetIndex | int | Yes | 当前显示元素的索引，索引从0开始。 取值范围为全体整数 取值限定为整数。 |
| extraInfo | [TabsAnimationEvent](arkts-arkui-tabs-tabsanimationevent-i.md) | Yes | 动画相关信息，包括主轴方向上当前显示元素和目标元素相对Tabs起始位置的位移，以及离手速度。 |

