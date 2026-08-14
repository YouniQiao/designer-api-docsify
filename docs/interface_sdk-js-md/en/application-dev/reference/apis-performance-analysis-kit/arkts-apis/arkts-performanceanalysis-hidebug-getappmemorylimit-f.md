# getAppMemoryLimit

## Modules to Import

```TypeScript
import { hidebug } from 'hidebug';
```

## getAppMemoryLimit

```TypeScript
function getAppMemoryLimit(): MemoryLimit
```

Obtains the memory limit of an application process.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-hidebug-function getAppMemoryLimit(): MemoryLimit--><!--Device-hidebug-function getAppMemoryLimit(): MemoryLimit-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| [MemoryLimit](arkts-performanceanalysis-hidebug-memorylimit-i.md) | Memory limit of the application process. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let appMemoryLimit:hidebug.MemoryLimit = hidebug.getAppMemoryLimit();
```

