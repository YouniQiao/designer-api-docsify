# getVss

## getVss

```TypeScript
function getVss(): bigint
```

Obtains the virtual set size used by the application process. This API is implemented by multiplying the value of  
**size** (number of memory pages) in the **\/proc/{pid}/statm** node by the page size (4 KB per page).

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-hidebug-function getVss(): bigint--><!--Device-hidebug-function getVss(): bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | Virtual set size used by the application process, in KB. |

**Example**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let vss: bigint = hidebug.getVss();
```

