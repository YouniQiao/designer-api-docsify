# GcStats

```TypeScript
type GcStats = Record<string, long>
```

Describes the key-value pair used to store GC statistics. This type does not support multi-thread operations. If this type is operated by multiple threads at the same time in an application, use a lock for it.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Property type:** ArkTS-Dyn: Record&lt;string, number&gt;  <br>ArkTS-Sta：Record&lt;string, long&gt;
