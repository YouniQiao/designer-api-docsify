# RequestTraceConfig

Describes the trace request configuration.

**Since:** 24

<!--Device-hidebug-interface RequestTraceConfig--><!--Device-hidebug-interface RequestTraceConfig-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## bufferSizeKb

```TypeScript
bufferSizeKb: number
```

Buffer size of the trace file, in KB.

**Type:** number

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RequestTraceConfig-bufferSizeKb: int--><!--Device-RequestTraceConfig-bufferSizeKb: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## durationMs

```TypeScript
durationMs: number
```

Duration of the trace, in ms.

**Type:** number

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RequestTraceConfig-durationMs: int--><!--Device-RequestTraceConfig-durationMs: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## identifier

```TypeScript
identifier: string
```

Identifier used as the prefix of the output trace file name.

**Type:** string

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RequestTraceConfig-identifier: string--><!--Device-RequestTraceConfig-identifier: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## reserved

```TypeScript
reserved: number
```

Reserved field for future use. Set to 0.

**Type:** number

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RequestTraceConfig-reserved: int--><!--Device-RequestTraceConfig-reserved: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

