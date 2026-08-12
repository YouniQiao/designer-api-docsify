# getNativeHeapAllocatedSize

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getNativeHeapAllocatedSize

```TypeScript
function getNativeHeapAllocatedSize() : bigint
```

Obtains the total number of bytes occupied by the total allocated space (**uordblks**, which is obtained from  
**mallinfo**) held by a process, which is measured by the memory allocator.

**Since:** 8

<!--Device-hidebug-function getNativeHeapAllocatedSize() : bigint--><!--Device-hidebug-function getNativeHeapAllocatedSize() : bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapAllocatedSize: bigint = hidebug.getNativeHeapAllocatedSize();
console.info(`nativeHeapAllocatedSize = ${nativeHeapAllocatedSize}`);
```
