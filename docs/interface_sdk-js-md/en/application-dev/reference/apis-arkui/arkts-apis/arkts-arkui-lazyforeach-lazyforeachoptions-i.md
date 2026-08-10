# LazyForEachOptions

配置LazyForEach的参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export interface LazyForEachOptions--><!--Device-unnamed-export interface LazyForEachOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## customComponentFreezeMode

```TypeScript
customComponentFreezeMode?: LazyForEachCustomComponentFreezeMode
```

已移出组件树的缓存自定义节点的冻结模式。默认值：LazyForEachCustomComponentFreezeMode.AUTO。

**Type:** [LazyForEachCustomComponentFreezeMode](../arkts-components/arkts-arkui-lazyforeachcustomcomponentfreezemode-e.md)

**Default:** LazyForEachCustomComponentFreezeMode.AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachOptions-customComponentFreezeMode?: LazyForEachCustomComponentFreezeMode--><!--Device-LazyForEachOptions-customComponentFreezeMode?: LazyForEachCustomComponentFreezeMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## memoryOptimizationStrategy

```TypeScript
memoryOptimizationStrategy?: LazyForEachMemOptStrategy
```

LazyForEach的内存优化策略。该参数在创建LazyForEach时设定，不支持动态修改。默认值：[DEFAULT]。

**Type:** [LazyForEachMemOptStrategy](../arkts-components/arkts-arkui-lazyforeachmemoptstrategy-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachOptions-memoryOptimizationStrategy?: LazyForEachMemOptStrategy--><!--Device-LazyForEachOptions-memoryOptimizationStrategy?: LazyForEachMemOptStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## releaseStrategy

```TypeScript
releaseStrategy?: LazyForEachReleaseStrategy
```

LazyForEach缓存节点的资源释放策略。默认值：LazyForEachReleaseStrategy.BATCH。&lt;br&gt;默认值:默认值：LazyForEachReleaseStrategy.BATCH。

**Type:** [LazyForEachReleaseStrategy](../arkts-components/arkts-arkui-lazyforeachreleasestrategy-e.md)

**Default:** LazyForEachReleaseStrategy.BATCH

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyForEachOptions-releaseStrategy?: LazyForEachReleaseStrategy--><!--Device-LazyForEachOptions-releaseStrategy?: LazyForEachReleaseStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

