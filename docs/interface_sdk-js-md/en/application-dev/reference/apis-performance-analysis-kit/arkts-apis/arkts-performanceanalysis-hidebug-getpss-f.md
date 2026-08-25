# getPss

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getPss

```TypeScript
function getPss() : bigint
```

Obtains the size of the physical memory actually used by the application process. This API is implemented by summing up the values of **Pss** and **SwapPss** in the **\/proc/{pid}/smaps_rollup** node.

> **NOTE：**&gt;
> Reading the **\/proc/{pid}/smaps_rollup** node is time-consuming. Therefore, you are advised not to use this API
> in the main thread. You can use this API in the asynchronous thread started by calling
> [@ohos.taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md) or [@ohos.worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md) to avoid frame freezing.

**Since:** 8

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |
