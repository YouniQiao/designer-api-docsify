# getStartRealtime

## getStartRealtime

```TypeScript
function getStartRealtime(): number
```

Obtains the duration (excluding the system sleep time), in milliseconds, from the time the system starts to the time the process starts.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function getStartRealtime(): number--><!--Device-process-function getStartRealtime(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | Duration obtained, in milliseconds. |

**Example**

```TypeScript
let realtime = process.getStartRealtime();
```

