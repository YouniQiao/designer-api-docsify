# GraphicsMemorySummary

Describes the GPU memory data of an application, including the GL and Graph parts.@interface GraphicsMemorySummary

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## gl

```TypeScript
gl: int
```

GL memory

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## graph

```TypeScript
graph: int
```

Graph memory

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug
