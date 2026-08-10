# clearData

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## clearData

```TypeScript
function clearData(): void
```

应用事件打点数据清理方法，将当前应用存储在本地的打点数据进行清除。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function clearData(): void--><!--Device-hiAppEvent-function clearData(): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Examples

```TypeScript
hiAppEvent.clearData();
```

