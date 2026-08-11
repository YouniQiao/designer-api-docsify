# getAppMemoryLimit

## getAppMemoryLimit

```TypeScript
function getAppMemoryLimit(): MemoryLimit
```

��ȡӦ�ó�����̵��ڴ����ơ�

**起始版本：** 12

<!--Device-hidebug-function getAppMemoryLimit(): MemoryLimit--><!--Device-hidebug-function getAppMemoryLimit(): MemoryLimit-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 |
| --- |
| [MemoryLimit](arkts-performanceanalysis-hidebug-memorylimit-i.md) |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let appMemoryLimit:hidebug.MemoryLimit = hidebug.getAppMemoryLimit();
console.info(`rssLimit: ${appMemoryLimit.rssLimit}, vssLimit: ${appMemoryLimit.vssLimit},` +
  `vmHeapLimit: ${appMemoryLimit.vmHeapLimit}, vmTotalHeapSize: ${appMemoryLimit.vmTotalHeapSize}`);
```
