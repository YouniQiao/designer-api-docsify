# getCpuUsage

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getCpuUsage

```TypeScript
function getCpuUsage() : double
```

Obtains the CPU usage of a process. > **NOTE：**> > This API involves cross-process communication and takes a long time. To avoid performance problems, you are > advised not to call this API in the main thread.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-hidebug-function getCpuUsage() : double--><!--Device-hidebug-function getCpuUsage() : double-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| double | CPU usage of a process. For example, if the CPU usage is **50%**, **0.5** is returned. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let cpuUsage: number = hidebug.getCpuUsage();
```

