# check

## Modules to Import

```TypeScript
import { jsLeakWatcher } from 'jsLeakWatcher';
```

## check

```TypeScript
function check(): string
```

Obtains the list of objects that are leaked and registered using **jsLeakWatcher.watch()**. Objects that are not reclaimed after GC is triggered are marked as leaked.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

<!--Device-jsLeakWatcher-function check(): string--><!--Device-jsLeakWatcher-function check(): string-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Return value:**

| Type | Description |
| --- | --- |
| string | List of leaked objects that are not reclaimed after GC is triggered. <br>Note: If this API is successful, a list of leaked objects in JSON format is returned. Otherwise, an empty string is returned. |

## Examples

```TypeScript
let leakObjlist:string = jsLeakWatcher.check();
```

