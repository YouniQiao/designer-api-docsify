# stopProfiling

## stopProfiling

```TypeScript
function stopProfiling(): void
```

ֹͣ�����Profiling�������٣�`stopProfiling()`�����ĵ�����Ҫ��`startProfiling(filename: string)`�����ĵ���һһ��Ӧ���ȿ�����رգ�������ظ��������ظ��رյĵ��÷�ʽ�������ӿڵ����쳣��

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [hidebug.stopJsCpuProfiling](arkts-performanceanalysis-hidebug-stopjscpuprofiling-f.md#stopjscpuprofiling)

<!--Device-hidebug-function stopProfiling(): void--><!--Device-hidebug-function stopProfiling(): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.startProfiling("cpuprofiler-20220216");
// code block
// ...
// code block
hidebug.stopProfiling();
```

