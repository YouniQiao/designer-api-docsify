# getLastParticipationTimestamp

## Modules to Import

```TypeScript
import { hiRetrieval } from 'hiRetrieval';
```

## getLastParticipationTimestamp

```TypeScript
function getLastParticipationTimestamp(): long
```

Query the UNIX timestamp of the last participating time.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hiRetrieval-function getLastParticipationTimestamp(): long--><!--Device-hiRetrieval-function getLastParticipationTimestamp(): long-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

**Return value:**

| Type | Description |
| --- | --- |
| long | Returns the timestamp of the last participating time in milliseconds, if never participated return 0. |

