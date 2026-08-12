# getNativeHeapSize

## getNativeHeapSize

```TypeScript
function getNativeHeapSize() : bigint
```

获取内存分配器统计的进程持有的普通块所占用的总字节数。

**起始版本：** 8

<!--Device-hidebug-function getNativeHeapSize() : bigint--><!--Device-hidebug-function getNativeHeapSize() : bigint-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 |
| --- |
| bigint |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapSize: bigint = hidebug.getNativeHeapSize();
console.info(`nativeHeapSize = ${nativeHeapSize}`);
```
