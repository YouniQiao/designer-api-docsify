# @ohos.bytrace(Performance Tracing)

The **bytrace** module implements performance tracing for processes.

> **NOTE：**
> 
> - The APIs provided by this module are deprecated since API version 8. You are advised to use the new APIs
> [@ohos.hiTraceMeter](arkts-hitracemeter.md#hiTraceMeter) instead.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** [hiTraceMeter](arkts-hitracemeter.md#hiTraceMeter)

<!--Device-unnamed-declare namespace bytrace--><!--Device-unnamed-declare namespace bytrace-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## Summary

### Functions

| Name | Description |
| --- | --- |
| [finishTrace](arkts-performanceanalysis-bytrace-finishtrace-f.md#finishtrace) | Marks the end of a timeslice trace task.  > **NOTE：** >  > To stop a trace task, the values of name and task ID in **finishTrace** must be the same as those in > **startTrace**. |
| [startTrace](arkts-performanceanalysis-bytrace-starttrace-f.md#starttrace) | Marks the start of a timeslice trace task.  > **NOTE：** >  > If multiple trace tasks with the same name need to be performed at the same time or a trace task needs to be > performed multiple times concurrently, different task IDs must be specified in **startTrace**. If the trace tasks > with the same name are not performed at the same time, the same task ID can be used. For details, see the > bytrace.finishTrace example. |
| [traceByValue](arkts-performanceanalysis-bytrace-tracebyvalue-f.md#tracebyvalue) | Defines a numeric variable that indicates the number of timeslice trace tasks. |

