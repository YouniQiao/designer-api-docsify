# ParallelStrategy

ParallelStrategy作为[Options](arkts-basicservices-zlib-options-i.md)的一个属性，用于指定压缩或解压时的串行或并行策略。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-zlib-export enum ParallelStrategy--><!--Device-zlib-export enum ParallelStrategy-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## PARALLEL_STRATEGY_SEQUENTIAL

```TypeScript
PARALLEL_STRATEGY_SEQUENTIAL = 0
```

默认值，串行压缩/解压策略。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ParallelStrategy-PARALLEL_STRATEGY_SEQUENTIAL = 0--><!--Device-ParallelStrategy-PARALLEL_STRATEGY_SEQUENTIAL = 0-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION

```TypeScript
PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION = 1
```

并行解压策略。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ParallelStrategy-PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION = 1--><!--Device-ParallelStrategy-PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION = 1-End-->

**System capability:** SystemCapability.BundleManager.Zlib

