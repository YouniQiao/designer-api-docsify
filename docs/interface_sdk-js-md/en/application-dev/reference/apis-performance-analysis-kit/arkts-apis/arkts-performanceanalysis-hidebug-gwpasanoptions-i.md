# GwpAsanOptions

GwpAsan Options.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-hidebug-interface GwpAsanOptions--><!--Device-hidebug-interface GwpAsanOptions-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## alwaysEnabled

```TypeScript
alwaysEnabled?: boolean
```

Control whether to enable GWP-ASan every time

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-GwpAsanOptions-alwaysEnabled?: boolean--><!--Device-GwpAsanOptions-alwaysEnabled?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## isRecover

```TypeScript
isRecover?: boolean
```

the Recoverable mode of GWP-ASAN.

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GwpAsanOptions-isRecover?: boolean--><!--Device-GwpAsanOptions-isRecover?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## maxSimutaneousAllocations

```TypeScript
maxSimutaneousAllocations?: int
```

the max simutaneous allocations of GWP-ASAN

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-GwpAsanOptions-maxSimutaneousAllocations?: int--><!--Device-GwpAsanOptions-maxSimutaneousAllocations?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## sampleRate

```TypeScript
sampleRate?: int
```

sample rate of GWP-ASAN

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-GwpAsanOptions-sampleRate?: int--><!--Device-GwpAsanOptions-sampleRate?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

