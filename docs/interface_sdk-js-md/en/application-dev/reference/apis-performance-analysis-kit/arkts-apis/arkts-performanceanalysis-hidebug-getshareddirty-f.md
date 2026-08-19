# getSharedDirty

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getSharedDirty

```TypeScript
function getSharedDirty() : bigint
```

Obtains the size of the shared dirty memory of a process. This API is implemented by reading the value of **Shared_Dirty** in the **\/proc/{pid}/smaps_rollup** node. &gt; **NOTE：**&gt; &gt; Reading the **\/proc/{pid}/smaps_rollup** node is time-consuming. Therefore, you are advised not to use this API &gt; in the main thread. You can use this API in the asynchronous thread started by calling &gt; [@ohos.taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md) or [@ohos.worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md) to avoid frame freezing.

**Since:** 23

<!--Device-hidebug-function getSharedDirty() : bigint--><!--Device-hidebug-function getSharedDirty() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | Size of the shared dirty memory of the process, in KB. |

**Examples**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let sharedDirty: bigint = hidebug.getSharedDirty();
```

