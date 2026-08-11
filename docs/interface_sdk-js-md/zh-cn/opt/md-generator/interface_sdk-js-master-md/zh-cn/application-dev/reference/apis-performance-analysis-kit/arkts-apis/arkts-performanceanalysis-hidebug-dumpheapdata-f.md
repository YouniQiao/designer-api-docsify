# dumpHeapData

## dumpHeapData

```TypeScript
function dumpHeapData(filename: string): void
```

�����������ת��������`filename.heapsnapshot`�ļ���

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [hidebug.dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md#dumpjsheapdata)(filename

<!--Device-hidebug-function dumpHeapData(filename: string): void--><!--Device-hidebug-function dumpHeapData(filename: string): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filename | string | 是 |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.dumpHeapData("heap-20220216");
```
