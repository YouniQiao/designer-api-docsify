# @ohos.hiTraceMeter(Performance Tracing)

The **HiTraceMeter** module provides the functions of tracing service processes and monitoring the system performance. It provides the data needed for HiTraceMeter to carry out performance analysis.

For details about the development process, see  
[Using HiTraceMeter (ArkTS)](../../../dfx/hitracemeter-guidelines-arkts.md).

> **NOTE：**
> 
> You are advised to use the performance tracing APIs of API version 19. The
> [startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md#starttrace), [finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishtrace), and
> [traceByValue()](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#tracebyvalue) APIs will be deprecated.
> 
> The trace output level cannot be specified in the [startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md#starttrace),
> [finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishtrace) and [traceByValue()](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#tracebyvalue) APIs. By
> default, the trace output level is **COMMERCIAL**.
> 
> The vertical bar (|) is used as the separator in
> [user-mode trace format](../../../dfx/hitracemeter-view.md#user-mode-trace-format). Therefore, the string
> parameters passed by the performance tracing APIs must exclude this character to avoid trace parsing exceptions.
> 
> The maximum length of a [user-mode trace](../../../dfx/hitracemeter-view.md#user-mode-trace-format) is 512
> characters. Excess characters will be truncated.

**Since:** 8

<!--Device-unnamed-declare namespace hiTraceMeter--><!--Device-unnamed-declare namespace hiTraceMeter-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [finishAsyncTrace](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace) |
| [finishSyncTrace](arkts-performanceanalysis-hitracemeter-finishsynctrace-f.md#finishsynctrace) |
| [finishTrace](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishtrace) |
| [isTraceEnabled](arkts-performanceanalysis-hitracemeter-istraceenabled-f.md#istraceenabled) |
| [registerTraceListener](arkts-performanceanalysis-hitracemeter-registertracelistener-f.md#registertracelistener) |
| [startAsyncTrace](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace) |
| [startSyncTrace](arkts-performanceanalysis-hitracemeter-startsynctrace-f.md#startsynctrace) |
| [startTrace](arkts-performanceanalysis-hitracemeter-starttrace-f.md#starttrace) |
| [traceByValue](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#tracebyvalue) |
| [traceByValue](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#tracebyvalue-1) |
| [unregisterTraceListener](arkts-performanceanalysis-hitracemeter-unregistertracelistener-f.md#unregistertracelistener) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TraceEventListener](arkts-performanceanalysis-hitracemeter-traceeventlistener-t.md) |
