# dumpHeapData

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## dumpHeapData

```TypeScript
function dumpHeapData(filename: string): void
```

Dumps the VM heap data and generates the **filename.heapsnapshot** file.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md)

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filename | string | Yes |
