# getGwpAsanGrayscaleState

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getGwpAsanGrayscaleState

```TypeScript
function getGwpAsanGrayscaleState(): int
```

Obtain the remaining days of GWP-ASan grayscale for your application.

**Since:** 23

<!--Device-hidebug-function getGwpAsanGrayscaleState(): int--><!--Device-hidebug-function getGwpAsanGrayscaleState(): int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| int | The remaining days of GWP-ASan grayscale. |

**Examples**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let remainDays: number = hidebug.getGwpAsanGrayscaleState();
console.info(`remainDays: ${remainDays}`);
```

