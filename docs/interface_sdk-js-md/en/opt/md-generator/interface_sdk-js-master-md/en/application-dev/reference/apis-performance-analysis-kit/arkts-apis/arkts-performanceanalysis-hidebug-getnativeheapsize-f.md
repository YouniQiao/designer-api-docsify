# getNativeHeapSize

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getNativeHeapSize

```TypeScript
function getNativeHeapSize() : bigint
```

Obtains the total number of bytes occupied by the total space (**uordblks** + **fordblks**, which are obtained from  
**mallinfo**) held by a process, which is measured by the memory allocator.

**Since:** 8

<!--Device-hidebug-function getNativeHeapSize() : bigint--><!--Device-hidebug-function getNativeHeapSize() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapSize: bigint = hidebug.getNativeHeapSize();
console.info(`nativeHeapSize = ${nativeHeapSize}`);
```
