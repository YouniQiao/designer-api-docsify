# startProfiling

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## startProfiling

```TypeScript
function startProfiling(filename: string): void
```

���������Profiling�������٣�`startProfiling(filename: string)`�����ĵ�����Ҫ��`stopProfiling()`�����ĵ���һһ��Ӧ���ȿ�����رգ�������ظ��������ظ��رյĵ��÷�ʽ�������ӿڵ����쳣��

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [hidebug.startJsCpuProfiling](arkts-performanceanalysis-hidebug-startjscpuprofiling-f.md#startjscpuprofiling)

<!--Device-hidebug-function startProfiling(filename: string): void--><!--Device-hidebug-function startProfiling(filename: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filename | string | Yes | �û��Զ���Ĳ������������ļ���������Ӧ�õ�`files`Ŀ¼�������Ըò���������json�ļ���string���ȵ����ֵΪ128�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.startProfiling("cpuprofiler-20220216");
// code block
// ...
// code block
hidebug.stopProfiling();
```

