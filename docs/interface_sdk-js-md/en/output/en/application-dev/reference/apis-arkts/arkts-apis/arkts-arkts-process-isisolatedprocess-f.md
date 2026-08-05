# isIsolatedProcess

## isIsolatedProcess

```TypeScript
function isIsolatedProcess(): boolean
```

Checks whether this process is isolated.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function isIsolatedProcess(): boolean--><!--Device-process-function isIsolatedProcess(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** is returned if the process is isolated; otherwise, |

**Example**

```TypeScript
let result = process.isIsolatedProcess();
```

