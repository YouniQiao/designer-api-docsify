# isTraceEnabled

## Modules to Import

```TypeScript
import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
```

## isTraceEnabled

```TypeScript
function isTraceEnabled(): boolean
```

Checks whether application trace capture is enabled.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hiTraceMeter-function isTraceEnabled(): boolean--><!--Device-hiTraceMeter-function isTraceEnabled(): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
if (hiTraceMeter.isTraceEnabled()) {
  // Service flow...
} else {
  // Service flow...
}
```
