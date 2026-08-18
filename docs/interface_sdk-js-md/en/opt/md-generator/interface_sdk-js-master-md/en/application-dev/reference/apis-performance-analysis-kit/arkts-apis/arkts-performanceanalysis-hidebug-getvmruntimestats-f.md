# getVMRuntimeStats

## Modules to Import

```TypeScript
```

## getVMRuntimeStats

```TypeScript
function getVMRuntimeStats(): GcStats
```

Obtains the system GC statistics.

**Since:** 23

<!--Device-hidebug-function getVMRuntimeStats(): GcStats--><!--Device-hidebug-function getVMRuntimeStats(): GcStats-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GcStats](arkts-performanceanalysis-hidebug-gcstats-t.md) |

**Examples**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let vMRuntimeStats: hidebug.GcStats = hidebug.getVMRuntimeStats();
console.info(`gc-count: ${vMRuntimeStats['ark.gc.gc-count']}`);
console.info(`gc-time: ${vMRuntimeStats['ark.gc.gc-time']}`);
console.info(`gc-bytes-allocated: ${vMRuntimeStats['ark.gc.gc-bytes-allocated']}`);
console.info(`gc-bytes-freed: ${vMRuntimeStats['ark.gc.gc-bytes-freed']}`);
console.info(`fullgc-longtime-count: ${vMRuntimeStats['ark.gc.fullgc-longtime-count']}`);
```
