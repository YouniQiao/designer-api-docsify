# isFlagEnabled

## Modules to Import

```TypeScript
import { hiTraceChain } from 'kits/@kit.PerformanceAnalysisKit';
```

## isFlagEnabled

```TypeScript
function isFlagEnabled(id: HiTraceId, flag: HiTraceFlag): boolean
```

Checks whether the trace flag is enabled for **HiTraceId**. This API returns the result synchronously.

**Since:** 8

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | [HiTraceId](arkts-performanceanalysis-hitracechain-hitraceid-i.md) | Yes |
| flag | [HiTraceFlag](arkts-performanceanalysis-hitracechain-hitraceflag-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
