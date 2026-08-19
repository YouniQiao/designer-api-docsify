# @ohos.bytrace(Performance Tracing)

The **bytrace** module implements performance tracing for processes. &gt; **NOTE：**&gt; &gt; - The APIs provided by this module are deprecated since API version 8. You are advised to use the new APIs &gt; [@ohos.hiTraceMeter](arkts-hitracemeter.md) instead.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** [hiTraceMeter](arkts-hitracemeter.md)

<!--Device-unnamed-declare namespace bytrace--><!--Device-unnamed-declare namespace bytrace-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [finishTrace(Performance Tracing)](arkts-performanceanalysis-bytrace-finishtrace-f.md) | Marks the end of a timeslice trace task. &gt; **NOTE：**&gt; &gt; To stop a trace task, the values of name and task ID in **finishTrace** must be the same as those in &gt; **startTrace**. |
| [startTrace(Performance Tracing)](arkts-performanceanalysis-bytrace-starttrace-f.md) | Marks the start of a timeslice trace task. &gt; **NOTE：**&gt; &gt; If multiple trace tasks with the same name need to be performed at the same time or a trace task needs to be &gt; performed multiple times concurrently, different task IDs must be specified in **startTrace**. If the trace tasks &gt; with the same name are not performed at the same time, the same task ID can be used. For details, see the &gt; bytrace.finishTrace example. |
| [traceByValue(Performance Tracing)](arkts-performanceanalysis-bytrace-tracebyvalue-f.md) | Defines a numeric variable that indicates the number of timeslice trace tasks. |

