# isDebugState

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## isDebugState

```TypeScript
function isDebugState(): boolean
```

Obtains the debugging state of an application process.

**Since:** 12

<!--Device-hidebug-function isDebugState(): boolean--><!--Device-hidebug-function isDebugState(): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

console.info(`isDebugState = ${hidebug.isDebugState()}`)
```
