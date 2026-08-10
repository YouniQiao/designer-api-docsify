# VisibleAreaChangeCallback

```TypeScript
declare type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: number) => void
```

组件可见区域变化事件的回调类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: number) => void--><!--Device-unnamed-declare type VisibleAreaChangeCallback = (isExpanding: boolean, currentRatio: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isExpanding | boolean | Yes | 视组件的可见面积与自身面积的比值与上一次回调相比的情况而定，比值变大为true，比值变小为false。 |
| currentRatio | number | Yes | 触发回调时，组件可见面积与自身面积的比值。 |

