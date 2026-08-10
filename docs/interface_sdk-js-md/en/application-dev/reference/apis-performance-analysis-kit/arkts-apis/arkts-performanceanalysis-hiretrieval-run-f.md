# run

## Modules to Import

```TypeScript
import { hiRetrieval } from 'kits/@kit.PerformanceAnalysisKit';
```

## run

```TypeScript
function run(): void
```

若此设备正在参与应用灰度活动（即已调用participate接口且未调用quit接口），则应用灰度模块开始工作，否则调用该接口不会产生任何效果。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hiRetrieval-function run(): void--><!--Device-hiRetrieval-function run(): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36000001 | Initialization error. Possibly caused by invoking this function before invoking init function. |

