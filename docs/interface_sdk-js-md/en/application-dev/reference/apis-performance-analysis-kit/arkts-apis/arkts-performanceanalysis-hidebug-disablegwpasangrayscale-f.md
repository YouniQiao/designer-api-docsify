# disableGwpAsanGrayscale

## Modules to Import

```TypeScript
import { hidebug } from 'hidebug';
```

## disableGwpAsanGrayscale

```TypeScript
function disableGwpAsanGrayscale(): void
```

Disables GWP-ASan. This API is used to cancel the custom configuration and restore the default parameter [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md#gwpasanoptions).

**Since:** 23

<!--Device-hidebug-function disableGwpAsanGrayscale(): void--><!--Device-hidebug-function disableGwpAsanGrayscale(): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Examples**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.disableGwpAsanGrayscale();
```

