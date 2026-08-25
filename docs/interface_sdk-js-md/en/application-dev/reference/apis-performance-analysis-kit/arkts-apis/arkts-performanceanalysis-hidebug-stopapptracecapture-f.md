# stopAppTraceCapture

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## stopAppTraceCapture

```TypeScript
function stopAppTraceCapture(): void
```

Stops application trace collection. Use [startAppTraceCapture()](arkts-performanceanalysis-hidebug-startapptracecapture-f.md) to start collection before calling this API. If this API is called before trace collection or it is repeatedly called, an exception will occur.If **startAppTraceCapture ()** is called without a properly specified **limitSize**, the size of the generated trace may exceed the **limitSize** value, causing the system to automatically call **stopAppTraceCapture()**. In this case, if **stopAppTraceCapture()** is called again, an error code 11400105 will be displayed.

**Since:** 12

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Error codes:**

| Error Code ID |
| --- |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) |
| [11400105](../errorcode-hiviewdfx-hidebug-trace.md#11400105-trace-capture-disabled) |
