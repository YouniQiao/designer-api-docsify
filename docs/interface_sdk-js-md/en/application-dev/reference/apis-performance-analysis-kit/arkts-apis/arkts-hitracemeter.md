# @ohos.hiTraceMeter(Performance Tracing)

The **HiTraceMeter** module provides the functions of tracing service processes and monitoring the system performance. It provides the data needed for HiTraceMeter to carry out performance analysis.

For details about the development process, see [Using HiTraceMeter (ArkTS)](../../../dfx/hitracemeter-guidelines-arkts.md).

> **NOTE：**
> 
> You are advised to use the performance tracing APIs of API version 19. The
> [startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md), [finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md), and
> [traceByValue()](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md) APIs will be deprecated.
> 
> The trace output level cannot be specified in the [startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md),
> [finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md) and [traceByValue()](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md) APIs. By
> default, the trace output level is **COMMERCIAL**.
> 
> The vertical bar (|) is used as the separator in
> [user-mode trace format](../../../dfx/hitracemeter-view.md#user-mode-trace-format). Therefore, the string
> parameters passed by the performance tracing APIs must exclude this character to avoid trace parsing exceptions.
> 
> The maximum length of a [user-mode trace](../../../dfx/hitracemeter-view.md#user-mode-trace-format) is 512
> characters. Excess characters will be truncated.

**Since:** 23

<!--Device-unnamed-declare namespace hiTraceMeter--><!--Device-unnamed-declare namespace hiTraceMeter-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [finishAsyncTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md) | Stops an asynchronous trace with the trace output level specified. |
| [finishSyncTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-finishsynctrace-f.md) | Stops a synchronous trace with the trace output level specified. |
| [finishTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-finishtrace-f.md) | Stops an asynchronous trace. |
| [isTraceEnabled(Performance Tracing)](arkts-performanceanalysis-hitracemeter-istraceenabled-f.md) | Checks whether application trace capture is enabled. |
| [registerTraceListener(Performance Tracing)](arkts-performanceanalysis-hitracemeter-registertracelistener-f.md) | Registers a callback to notify whether the application trace capture is enabled. This API uses a synchronous callback to return the result. |
| [startAsyncTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md) | Starts an asynchronous trace with the trace output level specified. |
| [startSyncTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-startsynctrace-f.md) | Starts a synchronous trace with the trace output level specified. For details, see [finishSyncTrace()](arkts-performanceanalysis-hitracemeter-finishsynctrace-f.md). |
| [startTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-starttrace-f.md) | Starts an asynchronous trace. |
| [traceByValue(Performance Tracing)](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md) | Traces the value changes of an integer variable. |
| [traceByValue(Performance Tracing)](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md) | Traces an integer with the trace output level specified. It is used to mark the name and value of a predefined integer variable to be traced. |
| [unregisterTraceListener(Performance Tracing)](arkts-performanceanalysis-hitracemeter-unregistertracelistener-f.md) | Unregisters the callback function used to notify whether the trace capture is enabled, which is registered using **registerTraceListener()**. |

### Enums

| Name | Description |
| --- | --- |
| [HiTraceOutputLevel(Performance Tracing)](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | Enumerates trace output levels. |

### Types

| Name | Description |
| --- | --- |
| [TraceEventListener(Performance Tracing)](arkts-performanceanalysis-hitracemeter-traceeventlistener-t.md) | Defines a callback to listen for whether the trace capture is enabled. |

