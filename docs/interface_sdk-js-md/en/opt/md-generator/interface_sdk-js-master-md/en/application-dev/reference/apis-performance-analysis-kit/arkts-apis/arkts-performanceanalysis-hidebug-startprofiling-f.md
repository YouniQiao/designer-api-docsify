# startProfiling

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## startProfiling

```TypeScript
function startProfiling(filename: string): void
```

Starts the VM profiling method. **startProfiling(filename: string)** and **stopProfiling()** are called in pairs.  
**startProfiling(filename: string)** always occurs before **stopProfiling()**. You are advised not to call either of these methods repeatedly. Otherwise, an exception may occur.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [hidebug.startJsCpuProfiling](arkts-performanceanalysis-hidebug-startjscpuprofiling-f.md#startjscpuprofiling)

<!--Device-hidebug-function startProfiling(filename: string): void--><!--Device-hidebug-function startProfiling(filename: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filename | string | Yes |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.startProfiling("cpuprofiler-20220216");
// code block
// ...
// code block
hidebug.stopProfiling();
```
