# traceByValue

## traceByValue

```TypeScript
function traceByValue(name: string, count: number): void
```

用来标记一个跟踪的整数变量，该变量的数值会不断变化。适用于需要实时监控数值变化（如网络请求次数、缓存命中率、内存占用等）的场景，能够帮助开发者快速发现异常波动，分析数据趋势。

从API version 19开始，建议使用  
[traceByValue](arkts-performanceanalysis-hitracemeter-tracebyvalue-f.md#tracebyvalue)接口，以便分级控制跟踪输出。

**起始版本：** 8

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-hiTraceMeter-function traceByValue(name: string, count: long): void--><!--Device-hiTraceMeter-function traceByValue(name: string, count: long): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| count | number | 是 |

## 示例

```TypeScript
let traceCount = 3;  // 定义要跟踪的整数变量初始值
hiTraceMeter.traceByValue("myTestCount", traceCount);
traceCount = 4;
hiTraceMeter.traceByValue("myTestCount", traceCount);  // 当myTestCount发生变化时，记录新值。
// 业务流程......
```


## traceByValue

```TypeScript
function traceByValue(level: HiTraceOutputLevel, name: string, count: number): void
```

整数跟踪事件，分级控制跟踪输出。用来标记一个预先定义需要跟踪的整数变量名及整数值。

**起始版本：** 19

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-hiTraceMeter-function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void--><!--Device-hiTraceMeter-function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | 是 |
| name | string | 是 |
| count | number | 是 |

## 示例

```TypeScript
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
let traceCount = 3;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
traceCount = 4;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
// 业务流程......
```
