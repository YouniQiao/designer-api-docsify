# RssInfo

Describes the physical memory information of the application process.

**Since:** 24

<!--Device-hidebug-interface RssInfo--><!--Device-hidebug-interface RssInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## rss

```TypeScript
rss: bigint
```

Size of the occupied physical memory (including the memory occupied by the shared library), in KB.The value of this parameter is obtained by reading the value of VmRSS in the /proc/{pid}/status node.

**Type:** bigint

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RssInfo-rss: bigint--><!--Device-RssInfo-rss: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## swapRss

```TypeScript
swapRss: bigint
```

Size of the memory occupied by the process in swap space, in KB.The value of this parameter is obtained by reading the value of VmSwap in the /proc/{pid}/status node.

**Type:** bigint

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RssInfo-swapRss: bigint--><!--Device-RssInfo-swapRss: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

