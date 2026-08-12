# getNativeHeapFreeSize

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getNativeHeapFreeSize

```TypeScript
function getNativeHeapFreeSize() : bigint
```

Obtains the total number of bytes occupied by the total free space (**fordblks**, which is obtained from  
**mallinfo**) held by a process, which is measured by the memory allocator.

**Since:** 8

<!--Device-hidebug-function getNativeHeapFreeSize() : bigint--><!--Device-hidebug-function getNativeHeapFreeSize() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapFreeSize: bigint = hidebug.getNativeHeapFreeSize();
console.info(`nativeHeapFreeSize = ${nativeHeapFreeSize}`);
```
