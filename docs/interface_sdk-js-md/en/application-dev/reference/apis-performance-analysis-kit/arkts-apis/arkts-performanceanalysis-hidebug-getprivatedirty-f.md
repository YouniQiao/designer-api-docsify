# getPrivateDirty

## Modules to Import

```TypeScript
import { hidebug } from 'hidebug';
```

## getPrivateDirty

```TypeScript
function getPrivateDirty() : bigint
```

Obtains the size of the private dirty memory of a process. This API is implemented by reading the value of **Private_Dirty** in the **\/proc/{pid}/smaps_rollup** node. > **NOTE：**> > Reading the **\/proc/{pid}/smaps_rollup** node is time-consuming. Therefore, you are advised not to use this API > in the main thread. You can use this API in the asynchronous thread started by calling > [@ohos.taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#@ohos.taskpool) or [@ohos.worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md#worker) to avoid frame freezing.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-hidebug-function getPrivateDirty() : bigint--><!--Device-hidebug-function getPrivateDirty() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | Size of the private dirty memory of the process, in KB. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let privateDirty: bigint = hidebug.getPrivateDirty();
```

