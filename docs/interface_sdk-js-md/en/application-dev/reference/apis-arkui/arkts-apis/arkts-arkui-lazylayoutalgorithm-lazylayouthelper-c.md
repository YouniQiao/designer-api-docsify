# LazyLayoutHelper

Helper class for lazy layout algorithm.Provides layout direction and view position information for lazy layout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class LazyLayoutHelper--><!--Device-unnamed-export declare class LazyLayoutHelper-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLazyLayoutDirection

```TypeScript
getLazyLayoutDirection(): LazyLayoutDirection
```

Get the lazy layout direction.

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

Get the end position of the visible view.

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

Get the start position of the visible view.

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

Set the adjusted offset for the lazy layout.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyLayoutHelper-setAdjustedOffset(offset: int): void--><!--Device-LazyLayoutHelper-setAdjustedOffset(offset: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | int | Yes | The adjusted offset value to set. &lt;br&gt;Unit: px. |

## setChildrenInactive

```TypeScript
setChildrenInactive(children: int[]): void
```

Set children inactive.

If child components are generated via ForEach or Repeat without virtualScroll,they will not be displayed after being set to inactive.If child components are generated via LazyForEach or Repeat with virtualScroll,they will be destroyed or recycled after being set to inactive.LazyForEach and Repeat with virtualScroll only support consecutive active child components;setting a child component to inactive between two active child components will not take effect.Child components laid out outside the display area will be automatically set to inactive.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyLayoutHelper-setChildrenInactive(children: int[]): void--><!--Device-LazyLayoutHelper-setChildrenInactive(children: int[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| children | int[] | Yes | The indices of child components to set inactive. |

