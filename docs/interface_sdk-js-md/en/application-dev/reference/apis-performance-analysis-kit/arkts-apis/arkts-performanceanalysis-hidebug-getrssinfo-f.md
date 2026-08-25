# getRssInfo

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getRssInfo

```TypeScript
function getRssInfo(): RssInfo
```

Obtains the physical memory usage of the application process. Reads data from the **\/proc/{pid}/status** node.

> **NOTE：**&gt;
> Reading the /proc/{pid}/status node takes a short time. The value obtained by this API is slightly different from
> the **rss** value obtained by the [hidebug.getAppNativeMemInfo](arkts-performanceanalysis-hidebug-getappnativememinfo-f.md) API. However,
> this API is more lightweight. To avoid frame loss or frame freezing, you are advised to use this API.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RssInfo](arkts-performanceanalysis-hidebug-rssinfo-i.md) |
