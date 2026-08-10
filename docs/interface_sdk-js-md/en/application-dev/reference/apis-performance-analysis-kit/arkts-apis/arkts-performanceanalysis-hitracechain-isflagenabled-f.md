# isFlagEnabled

## Modules to Import

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## isFlagEnabled

```TypeScript
function isFlagEnabled(id: HiTraceId, flag: HiTraceFlag): boolean
```

判断HiTraceId是否启用了跟踪标志flag，同步接口。用于在业务逻辑中根据跟踪标志进行不同处理，例如检查是否启用了INCLUDE_ASYNC标志以决定是否等待异步操作完成、检查是否启用了TP_INFO标志以决定是否打印调试信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hiTraceChain-function isFlagEnabled(id: HiTraceId, flag: HiTraceFlag): boolean--><!--Device-hiTraceChain-function isFlagEnabled(id: HiTraceId, flag: HiTraceFlag): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) | Yes | 需要判断指定跟踪标志是否启用的HiTraceId实例。 |
| flag | [HiTraceFlag](arkts-performanceanalysis-hitracechain-hitraceflag-e.md) | Yes | 指定的跟踪标志。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：HiTraceId已启用flag；false：HiTraceId未启用flag。 |

## Examples

```TypeScript
// Start tracing. The tracing flag is INCLUDE_ASYNC.
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
// Set the value of enabledIncludeAsyncFlag to true.
let enabledIncludeAsyncFlag = hiTraceChain.isFlagEnabled(traceId, hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
if (enabledIncludeAsyncFlag) {
// Processing logic for the scenario where the INCLUDE_ASYNC trace flag has been set.
}
// Stop tracing after the service is complete.
hiTraceChain.end(traceId);
```

