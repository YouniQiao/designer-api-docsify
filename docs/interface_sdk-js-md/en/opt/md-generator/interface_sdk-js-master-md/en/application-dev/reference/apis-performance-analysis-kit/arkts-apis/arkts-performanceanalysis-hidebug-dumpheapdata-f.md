# dumpHeapData

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## dumpHeapData

```TypeScript
function dumpHeapData(filename: string): void
```

Exports the VM heap data and generates a filename.heapsnapshot file.The input parameter is a user-defined file name, excluding the file suffix.The generated file is in the files folder under the application directory.Such as "/data/accounts/account_0/appdata/[package name]/files/xxx.heapsnapshot".

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [hidebug.dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md#dumpjsheapdata)

<!--Device-hidebug-function dumpHeapData(filename: string): void--><!--Device-hidebug-function dumpHeapData(filename: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filename | string | Yes |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.dumpHeapData("heap-20220216");
```
