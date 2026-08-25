# setJsRawHeapTrimLevel

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## setJsRawHeapTrimLevel

```TypeScript
function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void
```

Sets the trimming level of the original heap snapshot stored by the current process. Using **TRIM_LEVEL_2** for this API can effectively reduce the size of the heap snapshot file.

> **NOTE：**&gt;
> The default trimming level is **TRIM_LEVEL_1**. If **TRIM_LEVEL_2** is set, you need to use
> rawheap-translator since API version 20 to convert the .rawheap file to
> the .heapsnapshot file. Otherwise, the conversion may fail.&gt;
> This API affects the result of [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md).

**Since:** 20

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | [JsRawHeapTrimLevel](arkts-performanceanalysis-hidebug-jsrawheaptrimlevel-e.md) | Yes |
