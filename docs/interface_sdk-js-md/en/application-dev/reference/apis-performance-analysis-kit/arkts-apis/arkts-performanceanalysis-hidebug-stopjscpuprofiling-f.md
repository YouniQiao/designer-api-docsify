# stopJsCpuProfiling

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## stopJsCpuProfiling

```TypeScript
function stopJsCpuProfiling() : void
```

Stops the VM profiling method. **stopJsCpuProfiling()** and **startJsCpuProfiling(filename: string)** are called in pairs. **startJsCpuProfiling()** always occurs before **stopJsCpuProfiling()**. You are advised not to call either of these methods repeatedly. Otherwise, an exception may occur.

**Since:** 9

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug
