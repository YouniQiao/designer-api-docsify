# getPastCpuTime

## Modules to Import

```TypeScript
```

## getPastCpuTime

```TypeScript
function getPastCpuTime(): number
```

Obtains the CPU time (in milliseconds) from the time the process starts to the current time.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function getPastCpuTime(): number--><!--Device-process-function getPastCpuTime(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
let result = process.getPastCpuTime();
```
