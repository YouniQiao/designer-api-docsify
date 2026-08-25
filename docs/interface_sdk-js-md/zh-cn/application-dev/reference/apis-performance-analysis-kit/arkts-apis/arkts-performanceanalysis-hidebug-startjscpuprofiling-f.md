# startJsCpuProfiling

## 导入模块

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## startJsCpuProfiling

```TypeScript
function startJsCpuProfiling(filename : string) : void
```

启动虚拟机Profiling方法跟踪，`startJsCpuProfiling(filename: string)`方法的调用需要与`stopJsCpuProfiling()`方法的调用一一对应，先开启后关闭，请避免重复开启或重复 关闭的调用方式，否则会接口调用异常。

**起始版本：** 9

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filename | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
