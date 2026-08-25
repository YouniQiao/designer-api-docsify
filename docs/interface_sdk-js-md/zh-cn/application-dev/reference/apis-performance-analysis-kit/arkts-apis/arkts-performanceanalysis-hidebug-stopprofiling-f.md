# stopProfiling

## 导入模块

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## stopProfiling

```TypeScript
function stopProfiling(): void
```


> **说明：**&gt;
> 从API version 8支持，从API version 9开始废弃，
> 停止虚拟机Profiling方法跟踪，`stopProfiling()`方法的调用需要与`startProfiling(filename: string)`方法的调用一一对应，先开启后关闭，请避免重复开启或重复关闭的调用方式，
> 否则会接口调用异常。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stopJsCpuProfiling](arkts-performanceanalysis-hidebug-stopjscpuprofiling-f.md)

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug
