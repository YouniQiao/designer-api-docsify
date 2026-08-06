# getPss

## getPss

```TypeScript
function getPss() : bigint
```

Obtains the size of the physical memory actually used by the application process. This API is implemented by summing up the values of **Pss** and **SwapPss** in the **\/proc/{pid}/smaps\_rollup** node.
    **NOTE**  
    
    Reading the **\/proc/{pid}/smaps\_rollup** node is time-consuming. Therefore, you are advised not to use this API  
    in the main thread. You can use this API in the asynchronous thread started by calling  
    [@ohos.taskpool]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [@ohos.worker]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to avoid frame freezing.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hidebug-function getPss() : bigint--><!--Device-hidebug-function getPss() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | Size of the physical memory actually used by the application process, in KB. |

**Example**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let pss: bigint = hidebug.getPss();
```

