# @ohos.hiTraceMeter(Performance Tracing)

/*
 Copyright (C) 2021 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 23

<!--Device-unnamed-declare namespace hiTraceMeter--><!--Device-unnamed-declare namespace hiTraceMeter-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'hiTraceMeter';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [finishAsyncTrace](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace) | Stops an asynchronous trace with the trace output level specified. The **level**, **name**, and **taskId** used in **finishAsyncTrace()** must be the same as those of [startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace). |
| [finishSyncTrace](arkts-performanceanalysis-hitracemeter-finishsynctrace-f.md#finishsynctrace) | Stops a synchronous trace with the trace output level specified. The **level** used in **finishSyncTrace** must be the same as that of [startSyncTrace()](arkts-performanceanalysis-hitracemeter-startsynctrace-f.md#startsynctrace). |
| [finishTrace](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishtrace) | Stops an asynchronous trace. To stop a trace, the values of name and task ID in **finishTrace** must be the same as those in [startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md#starttrace). Since API version 19, you are advised to use [finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace), which must be used together with [startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace). |
| [isTraceEnabled](arkts-performanceanalysis-hitracemeter-istraceenabled-f.md#istraceenabled) | Checks whether application trace capture is enabled. |
| [registerTraceListener](arkts-performanceanalysis-hitracemeter-registertracelistener-f.md#registertracelistener) | Registers a callback to notify whether the application trace capture is enabled. This API uses a synchronous callback to return the result. After the registration is successful, the callback is executed immediately. Subsequent callbacks are executed when the application trace capture status changes. Callbacks are stored in the application process. A maximum of 10 callbacks can be registered in a process. > **NOTE：**> > If the callback contains time-consuming operations, the registration or deregistration will be blocked (waiting > for the callback execution to complete) when the callback is executed. > > Therefore, you are advised not to register or deregister callbacks containing time-consuming operations in the > main thread of the application to avoid application freeze. |
| [startAsyncTrace](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace) | Starts an asynchronous trace with the trace output level specified. If multiple trace tasks with the same name need to be performed at the same time or a trace needs to be performed multiple times concurrently, different task IDs must be specified in **startAsyncTrace**. If the trace tasks with the same name are not performed at the same time, the same taskId can be used. For details, see [finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace). |
| [startSyncTrace](arkts-performanceanalysis-hitracemeter-startsynctrace-f.md#startsynctrace) | Starts a synchronous trace with the trace output level specified. For details, see [finishSyncTrace()](arkts-performanceanalysis-hitracemeter-finishsynctrace-f.md#finishsynctrace). |
| [startTrace](arkts-performanceanalysis-hitracemeter-starttrace-f.md#starttrace) | Starts an asynchronous trace. If multiple trace tasks with the same name need to be performed at the same time or a trace needs to be performed multiple times concurrently, different task IDs must be specified in **startTrace**. If the trace tasks with the same name are not performed at the same time, the same taskId can be used. For a specific example, see [finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishtrace). Since API version 19, you are advised to use [startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace), which must be used together with [finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace). In this way, you can specify the trace output level and category. |
| [traceByValue](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#tracebyvalue) | Traces the value changes of an integer variable. Since API version 19, you are advised to use the [traceByValue](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#tracebyvalue) API to specify the trace output level. |
| [traceByValue](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#tracebyvalue) | Traces an integer with the trace output level specified. It is used to mark the name and value of a predefined integer variable to be traced. |
| [unregisterTraceListener](arkts-performanceanalysis-hitracemeter-unregistertracelistener-f.md#unregistertracelistener) | Unregisters the callback function used to notify whether the trace capture is enabled, which is registered using **registerTraceListener()**. |

### Enums

| Name | Description |
| --- | --- |
| [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | Enumerates trace output levels. The trace output level lower than the threshold does not take effect. The log version threshold is **INFO**, and the nolog version threshold is **COMMERCIAL**. |

### Types

| Name | Description |
| --- | --- |
| [TraceEventListener](arkts-performanceanalysis-hitracemeter-traceeventlistener-t.md) | Defines a callback to listen for whether the trace capture is enabled. |

