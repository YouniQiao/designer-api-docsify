# setId

## Modules to Import

```TypeScript
```

## setId

```TypeScript
function setId(id: HiTraceId): void
```

Sets a trace ID. This API returns the result synchronously. Sets the given HiTrace ID to the TLS of the current thread. If the given HiTrace ID is invalid, no operation is performed.

**Since:** 23

<!--Device-hiTraceChain-function setId(id: HiTraceId): void--><!--Device-hiTraceChain-function setId(id: HiTraceId): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) | Yes |

**Examples**

```TypeScript
// Obtain the trace ID of the current call chain.
let traceId = hiTraceChain.getId();
// Set traceId to the obtained trace ID.
hiTraceChain.setId(traceId);
```
