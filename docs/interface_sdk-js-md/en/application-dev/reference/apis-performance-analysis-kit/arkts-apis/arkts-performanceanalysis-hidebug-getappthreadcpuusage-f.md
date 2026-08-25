# getAppThreadCpuUsage

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getAppThreadCpuUsage

```TypeScript
function getAppThreadCpuUsage(): ThreadCpuUsage[]
```

Obtains the CPU usage of application threads.

> **NOTE：**&gt;
> This API involves cross-process communication and takes a number time. To avoid performance problems, you are
> advised not to call this API in the main thread.

**Since:** 12

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ThreadCpuUsage](arkts-performanceanalysis-hidebug-threadcpuusage-i.md)[] |
