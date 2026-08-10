# startAsyncTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## startAsyncTrace

```TypeScript
function startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: int, customCategory: string,
      customArgs?: string): void
```

标记一个异步跟踪耗时任务的开始，分级控制跟踪输出。

如果有多个相同name的任务需要跟踪或者对同一个任务要跟踪多次，并且任务同时被执行，则开发者每次调用startAsyncTrace传入的taskId需不同。

如果具有相同name的任务是串行执行的，则taskId可以相同。具体示例可参考[finishAsyncTrace()](arkts-performanceanalysis-hitracemeter-finishasynctrace-f.md#finishasynctrace)中的示例。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: int, customCategory: string,      customArgs?: string): void--><!--Device-hiTraceMeter-function startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: int, customCategory: string,      customArgs?: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | Yes | 跟踪输出级别，必须与流程开始的 [startAsyncTrace()](arkts-performanceanalysis-hitracemeter-startasynctrace-f.md#startasynctrace)的level参数值一致。 |
| name | string | Yes | 要跟踪的任务名称。由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议name、 customCategory、customArgs的长度之和不要超过420Byte。 |
| taskId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 任务id。用来区分具有相同名称的多个不同的任务，需确保并发执行的同名任务之间的任务id具有唯一性。 |
| customCategory | string | Yes | 自定义聚类名称，用于聚合同一类异步跟踪打点。由于单条trace记录的总长度限制为512Byte，超过的部分 将会被截断，建议name、customCategory、customArgs的长度之和不要超过420Byte。 |
| customArgs | string | No | 自定义键值对，格式key=value，多个键值对用逗号分隔，用于记录额外的业务信息或调试信息 （如记录用户ID、操作类型等）。当需要附加自定义数据用于trace分析时传入此参数，不需要附加数据时不传入即可。默认值为空字符串。 由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议name、customCategory、customArgs的长度之和不要超过420Byte。 |

## Examples

```TypeScript
// If the customCategory parameter is not required, pass in an empty string.
// If the customArgs parameter is not required, do not pass in this parameter or pass in an empty string.
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 1, "", "");
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 2, "");
// Use commas (,) to separate multiple key-value pairs.
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 3, "categoryTest", "key1=value");
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 4, "categoryTest", "key1=value1,key2=value2");
```

