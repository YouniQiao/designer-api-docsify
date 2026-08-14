# getSystemMemInfo

## Modules to Import

```TypeScript
import { hidebug } from 'hidebug';
```

## getSystemMemInfo

```TypeScript
function getSystemMemInfo(): SystemMemInfo
```

Obtains system memory information. This API is implemented by reading data from the **\/proc/meminfo** node.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-hidebug-function getSystemMemInfo(): SystemMemInfo--><!--Device-hidebug-function getSystemMemInfo(): SystemMemInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| [SystemMemInfo](arkts-performanceanalysis-hidebug-systemmeminfo-i.md) | System memory information. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let systemMemInfo: hidebug.SystemMemInfo = hidebug.getSystemMemInfo();

console.info(`totalMem: ${systemMemInfo.totalMem}, freeMem: ${systemMemInfo.freeMem}, ` +
  `availableMem: ${systemMemInfo.availableMem}`);
```

