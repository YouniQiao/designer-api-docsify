# getCurrentConfig

## Modules to Import

```TypeScript
import { hiRetrieval } from 'kits/@kit.PerformanceAnalysisKit';
```

## getCurrentConfig

```TypeScript
function getCurrentConfig(): HiRetrievalConfig
```

获取当前应用灰度活动配置。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hiRetrieval-function getCurrentConfig(): HiRetrievalConfig--><!--Device-hiRetrieval-function getCurrentConfig(): HiRetrievalConfig-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

**Return value:**

| Type | Description |
| --- | --- |
| [HiRetrievalConfig](arkts-performanceanalysis-hiretrieval-hiretrievalconfig-i.md) | 当前应用灰度活动配置，包含用户类型、设备类型、设备型号等参数，用于标识和圈选设备参与应用灰度活动。 |

