# disableGwpAsanGrayscale

## disableGwpAsanGrayscale

```TypeScript
function disableGwpAsanGrayscale(): void
```

Disables GWP-ASan. This API is used to cancel the custom configuration and restore the default parameter  
[GwpAsanOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-hidebug-function disableGwpAsanGrayscale(): void--><!--Device-hidebug-function disableGwpAsanGrayscale(): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Example**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.disableGwpAsanGrayscale();
```

