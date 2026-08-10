# ScrollOnWillScrollCallback

```TypeScript
export type ScrollOnWillScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | OffsetResult)
```

Scroll滚动前触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ScrollOnWillScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | OffsetResult)--><!--Device-unnamed-export type ScrollOnWillScrollCallback = (xOffset: double, yOffset: double, scrollState: ScrollState, scrollSource: ScrollSource) => (undefined | OffsetResult)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xOffset | double | Yes | 相对于上一帧水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。<br/>单位vp。 |
| yOffset | double | Yes | 相对于上一帧竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。<br/>单位vp。 |
| scrollState | [ScrollState](../arkts-components/arkts-arkui-scrollstate-e.md) | Yes | 当前滚动状态。 |
| scrollSource | [ScrollSource](arkts-arkui-scrollsource-e.md) | Yes | 当前滚动操作的来源。 |

**Return value:**

| Type | Description |
| --- | --- |
| (undefined \| OffsetResult) | the remain offset for the Scroll, same as (xOffset, yOffset) when no OffsetResult is returned. |

