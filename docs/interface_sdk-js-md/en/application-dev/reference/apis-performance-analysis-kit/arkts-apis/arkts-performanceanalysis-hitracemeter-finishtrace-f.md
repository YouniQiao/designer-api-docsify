# finishTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## finishTrace

```TypeScript
function finishTrace(name: string, taskId: int): void
```

标记一个异步跟踪耗时任务的结束。调用成功后，完成该任务的跟踪。

finishTrace的name和taskId必须与流程开始的[startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md#starttrace)对应参数值一致。

从API version 19开始，建议使用[finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace)接口（需与  
[startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace)接口配套使用）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function finishTrace(name: string, taskId: int): void--><!--Device-hiTraceMeter-function finishTrace(name: string, taskId: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 要跟踪的任务名称，必须与流程开始的[startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md#starttrace)对应参数值一致。 |
| taskId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 任务id，必须与流程开始的[startTrace()](arkts-performanceanalysis-hitracemeter-starttrace-f.md#starttrace)对应参数值一致。 |

## Examples

```TypeScript
// Start trace tasks with the same name concurrently.
hiTraceMeter.startTrace("myTestFunc", 1);
// Service flow...
hiTraceMeter.startTrace("myTestFunc", 2);  // Start the second trace with the same name while the first task is still running. The tasks are running concurrently and therefore their taskId must be different.
// Service flow...
hiTraceMeter.finishTrace("myTestFunc", 1);
// Service flow...
hiTraceMeter.finishTrace("myTestFunc", 2);
```

```TypeScript
// Start trace tasks with the same name in serial mode.
hiTraceMeter.startTrace("myTestFunc", 1);
// Service flow...
hiTraceMeter.finishTrace("myTestFunc", 1);  // End the first trace task.
// Service flow...
hiTraceMeter.startTrace("myTestFunc", 1);   // Start the second trace task with the same name in serial mode.
// Service flow...
hiTraceMeter.finishTrace("myTestFunc", 1);
```

