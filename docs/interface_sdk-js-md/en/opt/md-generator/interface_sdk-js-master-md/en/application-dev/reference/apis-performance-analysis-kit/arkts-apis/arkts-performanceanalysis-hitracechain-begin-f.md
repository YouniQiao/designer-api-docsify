# begin

## Modules to Import

```TypeScript
import { hiTraceChain } from '@kit.PerformanceAnalysisKit';
```

## begin

```TypeScript
function begin(name: string, flags?: number): HiTraceId
```

Starts call chain trace. This API returns the result synchronously. If the current thread's TLS does not contain a valid HiTrace ID, this function generates one, stores it in TLS, and returns it. If the current thread's TLS already contains a valid HiTrace ID, this function does not start tracing and returns an invalid HiTrace ID with all property values being 0.

**Since:** 23

**Deprecated since:** -1

<!--Device-hiTraceChain-function begin(name: string, flags?: int): HiTraceId--><!--Device-hiTraceChain-function begin(name: string, flags?: int): HiTraceId-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| flags | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) |

## Examples

```TypeScript
// Start tracing. The trace flag is the union of INCLUDE_ASYNC and DONOT_CREATE_SPAN.
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC | hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// End the call chain trace after the service logic is executed for several times.
hiTraceChain.end(traceId);
```
