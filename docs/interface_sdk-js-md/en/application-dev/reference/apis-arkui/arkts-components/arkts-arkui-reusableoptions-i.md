# ReusableOptions

可复用自定义组件的参数，用于配置内存优化策略，适用于需要降低可复用自定义组件内存使用量的场景。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare interface ReusableOptions--><!--Device-unnamed-declare interface ReusableOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## memoryOptimizationStrategy

```TypeScript
memoryOptimizationStrategy?: ReusableMemOptStrategy
```

可复用自定义组件的内存优化策略。该参数在创建可复用自定义组件时设定，不支持动态修改。传入[ENABLE_AUTO_CACHE_OPTIMIZATION](arkts-arkui-reusablememoptstrategy-e.md)时可启用自动内存优化，在应用退后台、组件不可见或整机低内存等场景下自动释放复用池中的组件；不传入时使用默认值[DEFAULT](arkts-arkui-reusablememoptstrategy-e.md)（无内存优化策略）。

**Type:** [ReusableMemOptStrategy](arkts-arkui-reusablememoptstrategy-e.md)

**Default:** ReusableMemOptStrategy.DEFAULT

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ReusableOptions-memoryOptimizationStrategy?: ReusableMemOptStrategy--><!--Device-ReusableOptions-memoryOptimizationStrategy?: ReusableMemOptStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

