# @ohos.hiTraceChain(Distributed Tracing)

/*
 Copyright (c) 2021 Huawei Device Co., Ltd.
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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace hiTraceChain--><!--Device-unnamed-declare namespace hiTraceChain-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## Modules to Import

```TypeScript
import { hiTraceChain } from '@kit.PerformanceAnalysisKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [begin](arkts-performanceanalysis-hitracechain-begin-f.md#begin) | Starts call chain trace. This API returns the result synchronously. If the current thread's TLS does not contain a valid HiTrace ID, this function generates one, stores it in TLS, and returns it. If the current thread's TLS already contains a valid HiTrace ID, this function does not start tracing and returns an invalid HiTrace ID with all property values being 0. |
| [clearId](arkts-performanceanalysis-hitracechain-clearid-f.md#clearId) | Clears the trace ID. This API returns the result synchronously. Clears the HiTrace ID in the current thread's TLS. |
| [createSpan](arkts-performanceanalysis-hitracechain-createspan-f.md#createSpan) | Creates a trace span. This API works in synchronous manner. Specifically, create a **HiTraceId**, use the **chainId** and **spanId** in the TLS of the current thread to initialize the **chainId** and **parentSpanId** of the **HiTraceId**, generate a new **spanId** for the **HiTraceId**, and return the **HiTraceId**. |
| [enableFlag](arkts-performanceanalysis-hitracechain-enableflag-f.md#enableFlag) | Enables the trace flag specified in HiTraceId. This API returns the result synchronously. |
| [end](arkts-performanceanalysis-hitracechain-end-f.md#end) | Stops call chain trace. This API works in synchronous manner. If the given HiTrace ID is valid and is the same as the HiTrace ID in the current thread's TLS, the tracing is stopped and the HiTrace ID in the current thread's TLS is set to invalid. If the given HiTrace ID is invalid or is not the same as the HiTrace ID in the current thread's TLS, the tracing fails to be stopped, and a tracing stop failure log is printed. |
| [getId](arkts-performanceanalysis-hitracechain-getid-f.md#getId) | Obtains the trace ID. This API returns the result synchronously. Obtains the HiTrace ID in the TLS of the current thread. |
| [isFlagEnabled](arkts-performanceanalysis-hitracechain-isflagenabled-f.md#isFlagEnabled) | Checks whether the trace flag is enabled for **HiTraceId**. This API returns the result synchronously. |
| [isValid](arkts-performanceanalysis-hitracechain-isvalid-f.md#isValid) | Checks whether a **HiTraceId** instance is valid. This API returns the result synchronously. |
| [setId](arkts-performanceanalysis-hitracechain-setid-f.md#setId) | Sets a trace ID. This API returns the result synchronously. Sets the given HiTrace ID to the TLS of the current thread. If the given HiTrace ID is invalid, no operation is performed. |
| [tracepoint](arkts-performanceanalysis-hitracechain-tracepoint-f.md#tracepoint) | Adds a trace point for the [@ohos.hiTraceMeter (Performance Tracing)](arkts-hitracemeter.md#@ohos.hiTraceMeter(Performance-Tracing)) logging, which is synchronous. When type is set to **CS** and **SR**, the HiTraceMeter tracing starts. When type is set to **CR** and **SS**, the HiTraceMeter tracing ends. When type is set to **GENERAL**, the HiTraceMeter tracing does not start. The trace points for **CS** and **CR** types must be used as a pair; likewise, trace points for **SR** and **SS** types must also be used together. Otherwise, the start and end trace points of HiTraceMeter cannot match each other. |

### Interfaces

| Name | Description |
| --- | --- |
| [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) | Defines a **HiTraceId** object. |

### Enums

| Name | Description |
| --- | --- |
| [HiTraceCommunicationMode](arkts-performanceanalysis-hitracechain-hitracecommunicationmode-e.md) | Enumerates communication modes. |
| [HiTraceFlag](arkts-performanceanalysis-hitracechain-hitraceflag-e.md) | Enumerates trace flag types. |
| [HiTraceTracepointType](arkts-performanceanalysis-hitracechain-hitracetracepointtype-e.md) | Enumerates trace point types. |

