# getNativeHeapFreeSize

## 导入模块

```TypeScript
```

## getNativeHeapFreeSize

```TypeScript
function getNativeHeapFreeSize() : bigint
```

获取内存分配器统计的进程持有的空闲的普通块所占用的总字节数。

**起始版本：** 23

<!--Device-hidebug-function getNativeHeapFreeSize() : bigint--><!--Device-hidebug-function getNativeHeapFreeSize() : bigint-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 |
| --- |
| bigint |

**示例**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeHeapFreeSize: bigint = hidebug.getNativeHeapFreeSize();
console.info(`nativeHeapFreeSize = ${nativeHeapFreeSize}`);
```
