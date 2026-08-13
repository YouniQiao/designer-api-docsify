# VirtualScrollOptions

Defines the options of repeat virtualScroll to implement reuse and lazy loading.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface VirtualScrollOptions--><!--Device-unnamed-export interface VirtualScrollOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableVirtualScroll

```TypeScript
disableVirtualScroll?: boolean
```

Indicates whether to activate virtual scroll mode.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-disableVirtualScroll?: boolean--><!--Device-VirtualScrollOptions-disableVirtualScroll?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## memoryOptimizationStrategy

```TypeScript
memoryOptimizationStrategy?: RepeatMemOptStrategy
```

Memory optimization strategy for Repeat.

**Type:** [RepeatMemOptStrategy](arkts-na-repeat-repeatmemoptstrategy-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-memoryOptimizationStrategy?: RepeatMemOptStrategy--><!--Device-VirtualScrollOptions-memoryOptimizationStrategy?: RepeatMemOptStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLazyLoading

```TypeScript
onLazyLoading?: OnLazyLoadingFunc
```

Data lazy loading.

**Type:** [OnLazyLoadingFunc](arkts-na-onlazyloadingfunc-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-onLazyLoading?: OnLazyLoadingFunc--><!--Device-VirtualScrollOptions-onLazyLoading?: OnLazyLoadingFunc-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTotalCount

```TypeScript
onTotalCount?: OnTotalCountFunc
```

The function of total data count.

**Type:** [OnTotalCountFunc](arkts-na-ontotalcountfunc-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-onTotalCount?: OnTotalCountFunc--><!--Device-VirtualScrollOptions-onTotalCount?: OnTotalCountFunc-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reusable

```TypeScript
reusable?: boolean
```

Reuse or not.

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-reusable?: boolean--><!--Device-VirtualScrollOptions-reusable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## totalCount

```TypeScript
totalCount?: int
```

Total data count.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScrollOptions-totalCount?: int--><!--Device-VirtualScrollOptions-totalCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

