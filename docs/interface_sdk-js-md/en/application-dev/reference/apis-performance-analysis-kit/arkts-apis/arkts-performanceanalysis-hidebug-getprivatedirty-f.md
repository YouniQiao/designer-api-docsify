# getPrivateDirty

## getPrivateDirty

```TypeScript
function getPrivateDirty() : bigint
```

Obtains the size of the private dirty memory of a process. This API is implemented by reading the value of  
**Private\_Dirty** in the **\/proc/{pid}/smaps\_rollup** node.
    **NOTE**  
    
    Reading the **\/proc/{pid}/smaps\_rollup** node is time-consuming. Therefore, you are advised not to use this API  
    in the main thread. You can use this API in the asynchronous thread started by calling  
    [@ohos.taskpool]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [@ohos.worker]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to avoid frame freezing.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hidebug-function getPrivateDirty() : bigint--><!--Device-hidebug-function getPrivateDirty() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | Size of the private dirty memory of the process, in KB. |

**Example**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let privateDirty: bigint = hidebug.getPrivateDirty();
```

