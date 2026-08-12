# getPss

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getPss

```TypeScript
function getPss() : bigint
```

Obtains the size of the physical memory actually used by the application process. This API is implemented by summing up the values of **Pss** and **SwapPss** in the **\/proc/{pid}/smaps_rollup** node.

> **NOTE：**
> 
> Reading the **\/proc/{pid}/smaps_rollup** node is time-consuming. Therefore, you are advised not to use this API
> in the main thread. You can use this API in the asynchronous thread started by calling
> [@ohos.taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md#taskpool) or [@ohos.worker](@ohos.worker) to avoid frame freezing.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-hidebug-function getPss() : bigint--><!--Device-hidebug-function getPss() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| bigint | Size of the physical memory actually used by the application process, in KB. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let pss: bigint = hidebug.getPss();
```

