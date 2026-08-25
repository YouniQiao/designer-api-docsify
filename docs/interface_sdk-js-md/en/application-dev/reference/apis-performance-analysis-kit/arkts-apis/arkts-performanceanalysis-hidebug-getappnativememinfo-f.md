# getAppNativeMemInfo

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getAppNativeMemInfo

```TypeScript
function getAppNativeMemInfo(): NativeMemInfo
```

Obtains the memory information of the application process. This API is implemented by reading data from the **\/proc/{pid}/smaps_rollup and /proc/{pid}/statm** node.

> **NOTE：**&gt;
> Reading the **\/proc/{pid}/smaps_rollup** node takes a number time. You are advised to use the asynchronous API
> [hidebug.getAppNativeMemInfoAsync](arkts-performanceanalysis-hidebug-getappnativememinfoasync-f.md) to avoid frame loss or frame freezing.&gt;
> You are advised to use the [hidebug.getRssInfo](arkts-performanceanalysis-hidebug-getrssinfo-f.md) API to obtain the RSS information of an
> application.

**Since:** 12

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NativeMemInfo](arkts-performanceanalysis-hidebug-nativememinfo-i.md) |
