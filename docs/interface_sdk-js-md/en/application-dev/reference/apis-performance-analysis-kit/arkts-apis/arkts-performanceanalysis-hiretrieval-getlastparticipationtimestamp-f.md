# getLastParticipationTimestamp

## Modules to Import

```TypeScript
import { hiRetrieval } from 'kits/@kit.PerformanceAnalysisKit';
```

## getLastParticipationTimestamp

```TypeScript
function getLastParticipationTimestamp(): long
```

查询此设备上次参与应用灰度活动的UNIX时间戳，如果此设备从未参与则返回0。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hiRetrieval-function getLastParticipationTimestamp(): long--><!--Device-hiRetrieval-function getLastParticipationTimestamp(): long-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 上一次参与应用灰度活动的UNIX时间戳，单位为毫秒。如果此设备从未参与则返回0。 |

