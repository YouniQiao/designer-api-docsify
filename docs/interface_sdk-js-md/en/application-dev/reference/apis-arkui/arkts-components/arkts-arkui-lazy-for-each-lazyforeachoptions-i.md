# LazyForEachOptions

Defines the options for LazyForEach.

**Since:** 26.0.0

<!--Device-unnamed-declare interface LazyForEachOptions--><!--Device-unnamed-declare interface LazyForEachOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## customComponentFreezeMode

```TypeScript
customComponentFreezeMode?: LazyForEachCustomComponentFreezeMode
```

Freeze mode for cached custom nodes that have been removed from the component tree. Default value: LazyForEachCustomComponentFreezeMode.AUTO.

**Type:** LazyForEachCustomComponentFreezeMode

**Default:** LazyForEachCustomComponentFreezeMode.AUTO

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyForEachOptions-customComponentFreezeMode?: LazyForEachCustomComponentFreezeMode--><!--Device-LazyForEachOptions-customComponentFreezeMode?: LazyForEachCustomComponentFreezeMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## memoryOptimizationStrategy

```TypeScript
memoryOptimizationStrategy?: LazyForEachMemOptStrategy
```

Memory optimization strategy for LazyForEach.

**Type:** LazyForEachMemOptStrategy

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyForEachOptions-memoryOptimizationStrategy?: LazyForEachMemOptStrategy--><!--Device-LazyForEachOptions-memoryOptimizationStrategy?: LazyForEachMemOptStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## releaseStrategy

```TypeScript
releaseStrategy?: LazyForEachReleaseStrategy
```

Resource release strategy for LazyForEach discarded nodes.Default value: LazyForEachReleaseStrategy.BATCH.

**Type:** LazyForEachReleaseStrategy

**Default:** LazyForEachReleaseStrategy.BATCH

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyForEachOptions-releaseStrategy?: LazyForEachReleaseStrategy--><!--Device-LazyForEachOptions-releaseStrategy?: LazyForEachReleaseStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

