# getCpuUsage

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getCpuUsage

```TypeScript
function getCpuUsage() : number
```

Obtains the CPU usage of a process.

> **NOTE：**
> 
> This API involves cross-process communication and takes a long time. To avoid performance problems, you are
> advised not to call this API in the main thread.

**Since:** 9

<!--Device-hidebug-function getCpuUsage() : double--><!--Device-hidebug-function getCpuUsage() : double-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let cpuUsage: number = hidebug.getCpuUsage();
console.info(`cpuUsage = ${cpuUsage}`);
```
