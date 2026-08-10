# startSyncTrace

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## startSyncTrace

```TypeScript
function startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void
```

标记一个同步跟踪耗时任务的开始，分级控制跟踪输出。适用于需要跟踪同步代码块执行耗时的场景，能够帮助开发者定位同步操作的耗时问题，优化应用响应速度。具体示例可参考[finishSyncTrace()](arkts-performanceanalysis-hitracemeter-finishsynctrace-f.md#finishsynctrace)中的示例。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void--><!--Device-hiTraceMeter-function startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | Yes | 跟踪输出级别。 |
| name | string | Yes | 要跟踪的任务名称。由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议name和customArgs的总 长度不要超过420Byte。 |
| customArgs | string | No | 键值对，格式key=value，多个键值对用逗号分隔，用于记录额外的业务信息或调试信息（如记录函数参数、 返回值等）。当需要附加自定义数据用于同步跟踪的trace分析时传入此参数，不需要附加数据时不传入即可。默认值为空字符串。由于单条trace记录的 总长度限制为512Byte，超过的部分将会被截断，建议name和customArgs的总长度不要超过420Byte。 |

## Examples

```TypeScript
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
// If the customArgs parameter is not required, do not pass in this parameter or pass in an empty string.
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc");
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc", "");
// Use commas (,) to separate multiple key-value pairs.
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc", "key=value");
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc", "key1=value1,key2=value2");
```

