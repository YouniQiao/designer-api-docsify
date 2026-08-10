# isValid

## Modules to Import

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## isValid

```TypeScript
function isValid(id: HiTraceId): boolean
```

判断HiTraceId是否有效，同步接口。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hiTraceChain-function isValid(id: HiTraceId): boolean--><!--Device-hiTraceChain-function isValid(id: HiTraceId): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) | Yes | 需要判断是否有效的HiTraceId实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true：HiTraceId有效；false：HiTraceId无效。 |

## Examples

```TypeScript
// Start tracing. The tracing flag is DEFAULT.
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// Set the value of traceIdIsvalid to true.
let traceIdIsvalid = hiTraceChain.isValid(traceId);
if (traceIdIsvalid) {
// Processing logic for the scenario where the validity check on the trace ID is successful.
}
// Stop tracing after the service is complete.
hiTraceChain.end(traceId);
```

