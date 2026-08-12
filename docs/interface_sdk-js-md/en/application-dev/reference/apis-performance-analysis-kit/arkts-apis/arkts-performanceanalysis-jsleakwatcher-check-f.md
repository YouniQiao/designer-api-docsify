# check

## Modules to Import

```TypeScript
import { jsLeakWatcher } from '@kit.PerformanceAnalysisKit';
```

## check

```TypeScript
function check(): string
```

Obtains the list of objects that are leaked and registered using **jsLeakWatcher.watch()**. Objects that are not reclaimed after GC is triggered are marked as leaked.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.1.0.

<!--Device-jsLeakWatcher-function check(): string--><!--Device-jsLeakWatcher-function check(): string-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Return value:**

| Type | Description |
| --- | --- |
| string | List of leaked objects that are not reclaimed after GC is triggered. &lt;br&gt;Note: If this API is successful, a list of leaked objects in JSON format is returned. Otherwise, an empty string is returned. |

## Examples

```TypeScript
let leakObjlist:string = jsLeakWatcher.check();
```

