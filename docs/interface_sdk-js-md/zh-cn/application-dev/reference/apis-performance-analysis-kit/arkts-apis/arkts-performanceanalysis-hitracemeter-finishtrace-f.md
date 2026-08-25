# finishTrace

## 导入模块

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## finishTrace

```TypeScript
function finishTrace(name: string, taskId: number): void
```

标记一个异步跟踪耗时任务的结束。调用成功后，完成该任务的跟踪。finishTrace的name和taskId必须与流程开始的[startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md)对应参数值一致。从API version 19开始，建议使用[finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md)接口（需与 [startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md)接口配套使用）。

**起始版本：** 8

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| taskId | number | 是 |
