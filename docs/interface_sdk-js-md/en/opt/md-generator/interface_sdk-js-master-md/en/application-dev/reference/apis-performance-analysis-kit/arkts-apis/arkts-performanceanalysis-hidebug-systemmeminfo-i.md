# SystemMemInfo

Describes the system memory information, including the total memory, free memory, and available memory.

**Since:** 23

<!--Device-hidebug-interface SystemMemInfo--><!--Device-hidebug-interface SystemMemInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
```

## availableMem

```TypeScript
availableMem: bigint
```

Available memory of the system, in KB. The value of this parameter is obtained by reading the value of **MemAvailable** in the **\/proc/meminfo** node.

**Type:** bigint

**Since:** 23

<!--Device-SystemMemInfo-availableMem: bigint--><!--Device-SystemMemInfo-availableMem: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## freeMem

```TypeScript
freeMem: bigint
```

Free memory of the system, in KB. The value of this parameter is obtained by reading the value of **MemFree** in the **\/proc/meminfo** node.

**Type:** bigint

**Since:** 23

<!--Device-SystemMemInfo-freeMem: bigint--><!--Device-SystemMemInfo-freeMem: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## totalMem

```TypeScript
totalMem: bigint
```

Total memory of the system, in KB. The value of this parameter is obtained by reading the value of **MemTotal** in the **\/proc/meminfo** node.

**Type:** bigint

**Since:** 23

<!--Device-SystemMemInfo-totalMem: bigint--><!--Device-SystemMemInfo-totalMem: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug
