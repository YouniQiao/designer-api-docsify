# getAppNativeMemInfoWithCache

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getAppNativeMemInfoWithCache

```TypeScript
function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo
```

Obtains the memory information of the application process. This API uses the cache mechanism and has higher performance than the **getAppNativeMemInfo** API. The cache is valid for 5 minutes.

> **NOTE：**&gt;
> Reading **\/proc/{pid}/smaps_rollup** is time-consuming. Therefore, you are advised not to use this API in the
> main thread. You can use [@ohos.taskpool](../../apis-arkts/arkts-apis/arkts-taskpool.md) or [@ohos.worker](../../apis-arkts/arkts-apis/arkts-arkts-worker-n.md) to
> enable asynchronous threads to avoid application frame freezing.

**Since:** 20

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| forceRefresh | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NativeMemInfo](arkts-performanceanalysis-hidebug-nativememinfo-i.md) |
