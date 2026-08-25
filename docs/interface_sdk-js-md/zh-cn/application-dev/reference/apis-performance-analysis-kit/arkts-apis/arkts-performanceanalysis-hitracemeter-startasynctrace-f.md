# startAsyncTrace

## 导入模块

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## startAsyncTrace

```TypeScript
function startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number, customCategory: string,
      customArgs?: string): void
```

标记一个异步跟踪耗时任务的开始，分级控制跟踪输出。如果有多个相同name的任务需要跟踪或者对同一个任务要跟踪多次，并且任务同时被执行，则开发者每次调用startAsyncTrace传入的taskId需不同。如果具有相同name的任务是串行执行的，则taskId可以相同。具体示例可参考[finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md) 中的示例。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | 是 |
| name | string | 是 |
| taskId | number | 是 |
| customCategory | string | 是 |
| customArgs | string | 否 |
