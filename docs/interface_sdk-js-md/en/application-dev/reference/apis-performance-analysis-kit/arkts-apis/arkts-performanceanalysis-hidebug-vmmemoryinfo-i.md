# VMMemoryInfo

Describes the VM memory information.

@interface VMMemoryInfo

**Since:** 23

<!--Device-hidebug-interface VMMemoryInfo--><!--Device-hidebug-interface VMMemoryInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## allArraySize

```TypeScript
allArraySize: bigint
```

Size of all array objects of the current VM, in KB.

**Type:** bigint

**Since:** 23

<!--Device-VMMemoryInfo-allArraySize: bigint--><!--Device-VMMemoryInfo-allArraySize: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## heapUsed

```TypeScript
heapUsed: bigint
```

Heap size used by the current VM, in KB.

**Type:** bigint

**Since:** 23

<!--Device-VMMemoryInfo-heapUsed: bigint--><!--Device-VMMemoryInfo-heapUsed: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## totalHeap

```TypeScript
totalHeap: bigint
```

Total heap size of the current VM, in KB.

**Type:** bigint

**Since:** 23

<!--Device-VMMemoryInfo-totalHeap: bigint--><!--Device-VMMemoryInfo-totalHeap: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

