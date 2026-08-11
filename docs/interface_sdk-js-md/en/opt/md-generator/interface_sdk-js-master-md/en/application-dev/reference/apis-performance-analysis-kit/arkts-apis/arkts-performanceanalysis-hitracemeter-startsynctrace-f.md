# startSyncTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## startSyncTrace

```TypeScript
function startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void
```

Starts a synchronous trace with the trace output level specified. For details, see  
[finishSyncTrace()](arkts-performanceanalysis-hitracemeter-finishsynctrace-f.md#finishsynctrace).

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void--><!--Device-hiTraceMeter-function startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | Yes |
| name | string | Yes |
| customArgs | string | No |

## Examples

```TypeScript
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
// If the customArgs parameter is not required, do not pass in this parameter or pass in an empty string.
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc");
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc", "");
// Use commas (,) to separate multiple key-value pairs.
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc", "key=value");
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc", "key1=value1,key2=value2");
```
