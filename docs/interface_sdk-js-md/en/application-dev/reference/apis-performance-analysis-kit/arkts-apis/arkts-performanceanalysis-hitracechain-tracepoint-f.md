# tracepoint

## Modules to Import

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## tracepoint

```TypeScript
function tracepoint(mode: HiTraceCommunicationMode, type: HiTraceTracepointType, id: HiTraceId, msg?: string): void
```

[@ohos.hiTraceMeter (性能打点)](arkts-hitracemeter.md)跟踪信息埋点，同步接口。

本接口与HiTraceMeter模块协同工作，HiTraceChain负责跟踪链的管理，HiTraceMeter负责性能数据的采集和统计。当type为客户端发送CS且服务端接收到SR时，进行同步HiTraceMeter开始打点；当type为服务端发送SS且客户端接收到CR时，进行同步HiTraceMeter结束打点；CS和CR以及SR和SS的信息埋点需配套使用。否则，HiTraceMeter开始与结束打点无法正常匹配；当type为通用类型GENERAL时，不会进行HiTraceMeter打点。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hiTraceChain-function tracepoint(mode: HiTraceCommunicationMode, type: HiTraceTracepointType, id: HiTraceId, msg?: string): void--><!--Device-hiTraceChain-function tracepoint(mode: HiTraceCommunicationMode, type: HiTraceTracepointType, id: HiTraceId, msg?: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [HiTraceCommunicationMode](arkts-performanceanalysis-hitracechain-hitracecommunicationmode-e.md) | Yes | Communication mode for the trace point. |
| type | [HiTraceTracepointType](arkts-performanceanalysis-hitracechain-hitracetracepointtype-e.md) | Yes | 信息埋点需要指定的跟踪埋点类型。 |
| id | [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) | Yes | 实施信息埋点操作的HiTraceId实例。 |
| msg | string | No | HiTraceMeter打点操作传入的trace说明信息，用于在性能分析时标识打点位置。当需要在HiTraceMeter报告中区分不同 打点位置时传入有意义的描述信息（如函数名、操作步骤等），不传入时使用空字符串，不影响基本打点功能。该参数的长度不超过63Byte，超出部分将被截断。 |

## Examples

```TypeScript
// Start tracing. The trace flag is the union of INCLUDE_ASYNC and DONOT_CREATE_SPAN.
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC | hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// Trigger the trace point after the service logic is executed for several times.
hiTraceChain.tracepoint(hiTraceChain.HiTraceCommunicationMode.THREAD, hiTraceChain.HiTraceTracepointType.SS, traceId, "Just an example");
// Stop tracing after the service is complete.
hiTraceChain.end(traceId);
```

