# getSystemCpuUsage

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getSystemCpuUsage

```TypeScript
function getSystemCpuUsage(): number
```

Obtains the CPU usage of the system.

> **NOTE：**&gt;
> This API involves cross-process communication and takes a number time. To avoid performance problems, you are
> advised not to call this API in the main thread.

**Since:** 12

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) |
