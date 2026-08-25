# @ohos.hiTraceMeter(Performance Tracing)

The **HiTraceMeter** module provides the functions of tracing service processes and monitoring the system performance. It provides the data needed for HiTraceMeter to carry out performance analysis.For details about the development process, see [Using HiTraceMeter (ArkTS)](../../../dfx/hitracemeter-guidelines-arkts.md).

> **NOTE：**&gt;
> You are advised to use the performance tracing APIs of API version 19. The
> [startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md), [finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md), and
> [traceByValue()](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md) APIs will be deprecated.&gt;
> The trace output level cannot be specified in the [startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md),
> [finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md) and [traceByValue()](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md) APIs. By
> default, the trace output level is **COMMERCIAL**.&gt;
> The vertical bar (|) is used as the separator in
> [user-mode trace format](../../../dfx/hitracemeter-view.md#user-mode-trace-format). Therefore, the string
> parameters passed by the performance tracing APIs must exclude this character to avoid trace parsing exceptions.&gt;
> The maximum length of a [user-mode trace](../../../dfx/hitracemeter-view.md#user-mode-trace-format) is 512
> characters. Excess characters will be truncated.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.HiviewDFX.HiTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [finishAsyncTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md) |
| [finishSyncTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-finishsynctrace-f.md) |
| [finishTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-finishtrace-f.md) |
| [isTraceEnabled(Performance Tracing)](arkts-performanceanalysis-hitracemeter-istraceenabled-f.md) |
| [registerTraceListener(Performance Tracing)](arkts-performanceanalysis-hitracemeter-registertracelistener-f.md) |
| [startAsyncTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md) |
| [startSyncTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-startsynctrace-f.md) |
| [startTrace(Performance Tracing)](arkts-performanceanalysis-hitracemeter-starttrace-f.md) |
| [traceByValue(Performance Tracing)](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md) |
| [traceByValue(Performance Tracing)](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md) |
| [unregisterTraceListener(Performance Tracing)](arkts-performanceanalysis-hitracemeter-unregistertracelistener-f.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HiTraceOutputLevel(Performance Tracing)](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TraceEventListener(Performance Tracing)](arkts-performanceanalysis-hitracemeter-traceeventlistener-t.md) |
