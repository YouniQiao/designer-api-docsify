# setProcDumpInSharedOOM

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## setProcDumpInSharedOOM

```TypeScript
function setProcDumpInSharedOOM(enable: boolean): void
```

Changes the dump heap snapshot from the thread-level to the process-level.

> **NOTE：**&gt;
> To dump a process-level heap snapshot, you must call this API and pass **true**. In addition, SharedHeap OOM must
> occur.&gt;
> This API does not affect the heap snapshot dumped in other scenarios. For example, it does not affect the result
> of [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md).&gt;
> This API can be called multiple times in the application lifecycle, but only the last call takes effect.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
