# SystemMemInfo

Describes the system memory information, including the total memory, free memory, and available memory.@interface SystemMemInfo

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## availableMem

```TypeScript
availableMem: bigint
```

Available memory of the system, in KB. The value of this parameter is obtained by reading the value of **MemAvailable** in the **\/proc/meminfo** node.

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## freeMem

```TypeScript
freeMem: bigint
```

Free memory of the system, in KB. The value of this parameter is obtained by reading the value of **MemFree** in the **\/proc/meminfo** node.

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## totalMem

```TypeScript
totalMem: bigint
```

Total memory of the system, in KB. The value of this parameter is obtained by reading the value of **MemTotal** in the **\/proc/meminfo** node.

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug
