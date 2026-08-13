# getAppVMMemoryInfo

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getAppVMMemoryInfo

```TypeScript
function getAppVMMemoryInfo(): VMMemoryInfo
```

Obtains VM memory information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-hidebug-function getAppVMMemoryInfo(): VMMemoryInfo--><!--Device-hidebug-function getAppVMMemoryInfo(): VMMemoryInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| [VMMemoryInfo](arkts-performanceanalysis-hidebug-vmmemoryinfo-i.md) | VM memory information. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let vmMemory: hidebug.VMMemoryInfo = hidebug.getAppVMMemoryInfo();
console.info(`totalHeap = ${vmMemory.totalHeap}, heapUsed = ${vmMemory.heapUsed},` +
  `allArraySize = ${vmMemory.allArraySize}` );
```

