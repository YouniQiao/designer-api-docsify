# quit

## Modules to Import

```TypeScript
import { hiRetrieval } from 'kits/@kit.PerformanceAnalysisKit';
```

## quit

```TypeScript
function quit(): void
```

设置此设备退出应用灰度活动，退出后此设备将无法在云端被圈选。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hiRetrieval-function quit(): void--><!--Device-hiRetrieval-function quit(): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36000001 | Initialization error. Possibly caused by invoking this function before invoking init function. |

