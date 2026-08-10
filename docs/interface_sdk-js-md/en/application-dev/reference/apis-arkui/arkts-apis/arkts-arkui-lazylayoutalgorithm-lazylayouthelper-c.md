# LazyLayoutHelper

懒布局算法的帮助器类，为懒布局提供布局方向和视图位置信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class LazyLayoutHelper--><!--Device-unnamed-export declare class LazyLayoutHelper-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLazyLayoutDirection

```TypeScript
getLazyLayoutDirection(): LazyLayoutDirection
```

获取懒加载布局方向。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyLayoutHelper-getLazyLayoutDirection(): LazyLayoutDirection--><!--Device-LazyLayoutHelper-getLazyLayoutDirection(): LazyLayoutDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [LazyLayoutDirection](arkts-arkui-lazylayoutalgorithm-lazylayoutdirection-e.md) | The lazy layout direction. |

## getViewEnd

```TypeScript
getViewEnd(): int
```

获取可见视图的结束位置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyLayoutHelper-getViewEnd(): int--><!--Device-LazyLayoutHelper-getViewEnd(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | The end position of the visible view. &lt;br&gt;Unit: px. |

## getViewStart

```TypeScript
getViewStart(): int
```

获取可见视图的起始位置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyLayoutHelper-getViewStart(): int--><!--Device-LazyLayoutHelper-getViewStart(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | The start position of the visible view. &lt;br&gt;Unit: px. |

## setAdjustedOffset

```TypeScript
setAdjustedOffset(offset: int): void
```

设置懒加载布局调整偏移量。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyLayoutHelper-setAdjustedOffset(offset: int): void--><!--Device-LazyLayoutHelper-setAdjustedOffset(offset: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | 设置要的调整偏移值。 &lt;br&gt;单位:单位：px。 |

## setChildrenInactive

```TypeScript
setChildrenInactive(children: int[]): void
```

设置子项不活动。

如果子组件是通过ForEach或不带virtualScroll的Repeat生成的，将其设置为inactive后，将不会显示。如果子组件是通过LazyForEach或者通过带virtualScroll的Repeat来生成的，将其设置为非活动状态后将被销毁或回收。带有virtualScroll的LazyForEach和Repeat只支持连续活动的子组件，在两个活动的子组件之间设置子组件为inactive不会生效。布局在显示区域之外的子组件将自动设置为非活动状态。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyLayoutHelper-setChildrenInactive(children: int[]): void--><!--Device-LazyLayoutHelper-setChildrenInactive(children: int[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| children | int[] | Yes | 要设置非活动状态的子组件的索引。 |

