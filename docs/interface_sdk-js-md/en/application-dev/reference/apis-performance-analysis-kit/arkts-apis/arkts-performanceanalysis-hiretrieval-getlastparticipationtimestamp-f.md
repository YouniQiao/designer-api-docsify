# getLastParticipationTimestamp

## Modules to Import

```TypeScript
import { hiRetrieval } from '@kit.PerformanceAnalysisKit';
```

## getLastParticipationTimestamp

```TypeScript
function getLastParticipationTimestamp(): long
```

Query the UNIX timestamp of the last participating time.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hiRetrieval-function getLastParticipationTimestamp(): long--><!--Device-hiRetrieval-function getLastParticipationTimestamp(): long-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | Returns the timestamp of the last participating time in milliseconds, if never participated return 0. |

