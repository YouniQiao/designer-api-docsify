# traceByValue

## Modules to Import

```TypeScript
```

## traceByValue

```TypeScript
function traceByValue(name: string, count: number): void
```

Traces the value changes of an integer variable. Since API version 19, you are advised to use the [traceByValue](#tracebyvalue) API to specify the trace output level.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function traceByValue(name: string, count: long): void--><!--Device-hiTraceMeter-function traceByValue(name: string, count: long): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| count | number | Yes |

**Examples**

```TypeScript
let traceCount = 3;
hiTraceMeter.traceByValue("myTestCount", traceCount);  // Use trace to record the value of myTestCount.
traceCount = 4;
hiTraceMeter.traceByValue("myTestCount", traceCount);  // When myTestCount changes, the new value is recorded.
// Service flow...
```


## traceByValue

```TypeScript
function traceByValue(level: HiTraceOutputLevel, name: string, count: number): void
```

Traces an integer with the trace output level specified. It is used to mark the name and value of a predefined integer variable to be traced.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hiTraceMeter-function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void--><!--Device-hiTraceMeter-function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | Yes |
| name | string | Yes |
| count | number | Yes |

**Examples**

```TypeScript
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
let traceCount = 3;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
traceCount = 4;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
// Service flow...
```
