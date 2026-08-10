# participate

## Modules to Import

```TypeScript
import { hiRetrieval } from 'kits/@kit.PerformanceAnalysisKit';
```

## participate

```TypeScript
function participate(config: HiRetrievalConfig): void
```

设置此设备参与应用灰度活动。调用后向服务器发送参与灰度消息和应用灰度活动配置，服务器标记此设备为可圈选并记录该应用灰度活动配置作为算法参数。多次调用将更新为最新的应用灰度活动配置。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hiRetrieval-function participate(config: HiRetrievalConfig): void--><!--Device-hiRetrieval-function participate(config: HiRetrievalConfig): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [HiRetrievalConfig](arkts-performanceanalysis-hiretrieval-hiretrievalconfig-i.md) | Yes | 开发者指定的应用灰度活动配置。用于设置此设备参与应用灰度活动时的用户类型、设备类型和设备型号信息，服务器将记录这些配置作为算法参数，用于圈选设备。 不同参数值会影响设备参与应用灰度活动的概率和采集的日志类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36000001 | Initialization error. Possibly caused by invoking this function before invoking init function. |

