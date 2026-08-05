# isValid

## isValid

```TypeScript
function isValid(id: HiTraceId): boolean
```

Checks whether a **HiTraceId** instance is valid. This API returns the result synchronously.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hiTraceChain-function isValid(id: HiTraceId): boolean--><!--Device-hiTraceChain-function isValid(id: HiTraceId): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | **HiTraceId** instance. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** indicates that **HiTraceId** is valid, and **false** indicates the |

**Example**

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

