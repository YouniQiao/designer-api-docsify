# getGwpAsanGrayscaleState

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getGwpAsanGrayscaleState

```TypeScript
function getGwpAsanGrayscaleState(): number
```

Obtains the number of remaining days for enabling GWP-ASan.

> **NOTE：**&gt;
> This API involves cross-process communication and takes a number time. To avoid performance problems, you are
> advised not to call this API in the main thread. You can use [@ohos.taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md) or
> [@ohos.worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md) to enable asynchronous threads to avoid application frame freezing.

**Since:** 20

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
