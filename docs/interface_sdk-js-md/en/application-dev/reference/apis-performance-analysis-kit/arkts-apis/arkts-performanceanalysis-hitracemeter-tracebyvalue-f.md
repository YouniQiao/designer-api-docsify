# traceByValue

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## traceByValue

```TypeScript
function traceByValue(name: string, count: long): void
```

用来标记一个跟踪的整数变量，该变量的数值会不断变化。适用于需要实时监控数值变化（如网络请求次数、缓存命中率、内存占用等）的场景，能够帮助开发者快速发现异常波动，分析数据趋势。

从API version 19开始，建议使用[traceByValue&lt;sup&gt;19+&lt;/sup&gt;()](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#tracebyvalue)接口，以便分级控制跟踪输出。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function traceByValue(name: string, count: long): void--><!--Device-hiTraceMeter-function traceByValue(name: string, count: long): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 要跟踪的整数变量名称。 由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议该参数的长度不要超过420Byte。 |
| count | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 整数变量的值。 |

## Examples

```TypeScript
let traceCount = 3;
hiTraceMeter.traceByValue("myTestCount", traceCount);  // Use trace to record the value of myTestCount.
traceCount = 4;
hiTraceMeter.traceByValue("myTestCount", traceCount);  // When myTestCount changes, the new value is recorded.
// Service flow...
```


## traceByValue

```TypeScript
function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void
```

整数跟踪事件，分级控制跟踪输出。用来标记一个预先定义需要跟踪的整数变量名及整数值。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void--><!--Device-hiTraceMeter-function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | Yes | 跟踪输出级别。 |
| name | string | Yes | 要跟踪的整数变量名称。 由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议该参数的长度不要超过420Byte。 |
| count | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 整数变量的值。 |

## Examples

```TypeScript
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
let traceCount = 3;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
traceCount = 4;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
// Service flow...
```

