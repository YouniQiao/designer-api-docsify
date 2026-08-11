# getAppVMMemoryInfo

## getAppVMMemoryInfo

```TypeScript
function getAppVMMemoryInfo(): VMMemoryInfo
```

��ȡVM�ڴ������Ϣ��

**起始版本：** 12

<!--Device-hidebug-function getAppVMMemoryInfo(): VMMemoryInfo--><!--Device-hidebug-function getAppVMMemoryInfo(): VMMemoryInfo-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 |
| --- |
| [VMMemoryInfo](arkts-performanceanalysis-hidebug-vmmemoryinfo-i.md) |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let vmMemory: hidebug.VMMemoryInfo = hidebug.getAppVMMemoryInfo();
console.info(`totalHeap = ${vmMemory.totalHeap}, heapUsed = ${vmMemory.heapUsed},` +
  `allArraySize = ${vmMemory.allArraySize}` );
```
