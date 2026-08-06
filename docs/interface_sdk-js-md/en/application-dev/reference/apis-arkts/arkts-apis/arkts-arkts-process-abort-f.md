# abort

## abort

```TypeScript
function abort(): void
```

Aborts a process and generates a core file. This method will cause a process to exit immediately. Exercise caution when using this method.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function abort(): void--><!--Device-process-function abort(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Example**

```TypeScript
process.abort();
```

