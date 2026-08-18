# getOutputDir

## Modules to Import

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
```

## getOutputDir

```TypeScript
function getOutputDir(): string
```

Returns the directory path of hilog logs in the sandbox. If the output type of hilog is DEFAULT, an empty string is returned.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hilog-function getOutputDir(): string--><!--Device-hilog-function getOutputDir(): string-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Return value:**

| Type | Description |
| --- | --- |
| string | the directory path of hilog logs in the sandbox. |

