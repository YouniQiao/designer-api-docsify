# init

## Modules to Import

```TypeScript
import { hiRetrieval } from 'kits/@kit.PerformanceAnalysisKit';
```

## init

```TypeScript
function init(): void
```

初始化应用灰度模块。多实例应用不支持调用此接口。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hiRetrieval-function init(): void--><!--Device-hiRetrieval-function init(): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiRetrieval

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 36000002 | Multi-instance applications not supported error. Possibly caused by invoking this function in a multi-instance application. |

