# finishAsyncTrace

## 导入模块

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## finishAsyncTrace

```TypeScript
function finishAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number): void
```

标记一个异步跟踪耗时任务的结束，分级控制跟踪输出。finishAsyncTrace的level、name和taskId必须与流程开始的[startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md)对应参数值一致。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | 是 |
| name | string | 是 |
| taskId | number | 是 |
