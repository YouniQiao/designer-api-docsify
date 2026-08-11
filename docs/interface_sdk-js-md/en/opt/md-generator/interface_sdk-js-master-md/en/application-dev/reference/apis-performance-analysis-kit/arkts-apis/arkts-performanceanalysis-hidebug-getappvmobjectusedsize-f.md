# getAppVMObjectUsedSize

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getAppVMObjectUsedSize

```TypeScript
function getAppVMObjectUsedSize(): bigint
```

Obtains the VM memory size occupied by ArkTS objects.

**Since:** 21

<!--Device-hidebug-function getAppVMObjectUsedSize(): bigint--><!--Device-hidebug-function getAppVMObjectUsedSize(): bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

console.info(`getAppVMObjectUsedSize = ${hidebug.getAppVMObjectUsedSize()}`);
```
