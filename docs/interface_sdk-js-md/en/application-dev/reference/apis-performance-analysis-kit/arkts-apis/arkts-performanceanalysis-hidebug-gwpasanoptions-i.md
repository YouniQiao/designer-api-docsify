# GwpAsanOptions

GwpAsan Options.

**Since:** 20

<!--Device-hidebug-interface GwpAsanOptions--><!--Device-hidebug-interface GwpAsanOptions-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## alwaysEnabled

```TypeScript
alwaysEnabled?: boolean
```

Control whether to enable GWP-ASan every time

**Type:** boolean

**Since:** 20

<!--Device-GwpAsanOptions-alwaysEnabled?: boolean--><!--Device-GwpAsanOptions-alwaysEnabled?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## isRecover

```TypeScript
isRecover?: boolean
```

the Recoverable mode of GWP-ASAN.

**Type:** boolean

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-GwpAsanOptions-isRecover?: boolean--><!--Device-GwpAsanOptions-isRecover?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## maxSimutaneousAllocations

```TypeScript
maxSimutaneousAllocations?: number
```

the max simutaneous allocations of GWP-ASAN

**Type:** number

**Since:** 20

<!--Device-GwpAsanOptions-maxSimutaneousAllocations?: int--><!--Device-GwpAsanOptions-maxSimutaneousAllocations?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## sampleRate

```TypeScript
sampleRate?: number
```

sample rate of GWP-ASAN

**Type:** number

**Since:** 20

<!--Device-GwpAsanOptions-sampleRate?: int--><!--Device-GwpAsanOptions-sampleRate?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

