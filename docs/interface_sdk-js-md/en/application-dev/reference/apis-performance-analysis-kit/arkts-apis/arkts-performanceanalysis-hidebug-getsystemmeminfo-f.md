# getSystemMemInfo

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getSystemMemInfo

```TypeScript
function getSystemMemInfo(): SystemMemInfo
```

Obtains system memory information. This API is implemented by reading data from the **\/proc/meminfo** node.

**Since:** 12

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SystemMemInfo](arkts-performanceanalysis-hidebug-systemmeminfo-i.md) |
