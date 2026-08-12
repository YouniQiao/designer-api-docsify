# @ohos.hiTraceMeter(性能打点)

本模块提供了跟踪进程轨迹，度量程序执行性能的打点能力，支持异步耗时任务跟踪、同步耗时任务跟踪、整数变量跟踪等多种性能分析场景。本模块打点的数据供HiTraceMeter工具分析使用，能够帮助开发者快速定位性能瓶颈，优化应用性能。

详细开发流程请参考：[使用HiTraceMeter跟踪性能（ArkTS）](../../../dfx/hitracemeter-guidelines-arkts.md)。

建议使用API version 19的性能打点接口，后续性能打点接口[startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md#startTrace)、  
[finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishTrace)、[traceByValue()](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#traceByValue)将逐步废弃。

性能打点接口[startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md#startTrace)、[finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishTrace)、  
[traceByValue()](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#traceByValue)固定使用COMMERCIAL级别。

[用户态trace格式](../../../dfx/hitracemeter-view.md#用户态trace格式说明)使用竖线 `|` 作为分隔符，所以通过性能打点接口传递的字符串类型参数应避免包含该字符，防止trace解析异常。

[用户态trace](../../../dfx/hitracemeter-view.md#用户态trace格式说明)总长度限制512字符，超过的部分将会被截断。

**起始版本：** 8

<!--Device-unnamed-declare namespace hiTraceMeter--><!--Device-unnamed-declare namespace hiTraceMeter-End-->

**系统能力：** SystemCapability.HiviewDFX.HiTrace

## 汇总

### 函数

| 名称 |
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

### 枚举

| 名称 |
| --- |
| [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) |

### 类型

| 名称 |
| --- |
| [TraceEventListener](arkts-performanceanalysis-hitracemeter-traceeventlistener-t.md) |
