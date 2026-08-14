# getPastCpuTime

## Modules to Import

```TypeScript
import { process } from 'process';
```

## getPastCpuTime

```TypeScript
function getPastCpuTime(): number
```

Obtains the CPU time (in milliseconds) from the time the process starts to the current time.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function getPastCpuTime(): number--><!--Device-process-function getPastCpuTime(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| number | CPU time obtained, in milliseconds. |

## Examples

```TypeScript
let result = process.getPastCpuTime();
```

