# startTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## startTrace

```TypeScript
function startTrace(name: string, taskId: int): void
```

标记一个异步跟踪耗时任务的开始。调用成功后，创建一条异步跟踪记录。

如果有多个相同name的任务需要跟踪或者对同一个任务要跟踪多次，并且任务同时被执行，则开发者每次调用startTrace传入的taskId需不同。

如果具有相同name的任务是串行执行的，则taskId可以相同。具体示例可参考[finishTrace()](arkts-performanceanalysis-hitracemeter-finishtrace-f.md#finishtrace)中的示例。

从API version 19开始，建议使用[startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace)接口（需与  
[finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace)接口配套使用），以便分级控制跟踪输出与跟踪聚类。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function startTrace(name: string, taskId: int): void--><!--Device-hiTraceMeter-function startTrace(name: string, taskId: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 要跟踪的任务名称。 由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议该参数的长度不要超过420Byte。 |
| taskId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 任务id。 用来区分具有相同名称的多个不同的任务，需确保并发执行的同名任务之间的任务id具有唯一性。 |

## Examples

```TypeScript
hiTraceMeter.startTrace("myTestFunc", 1);
```

