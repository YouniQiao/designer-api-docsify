# traceByValue

## Modules to Import

```TypeScript
import { hiTraceMeter } from 'kits/@kit.PerformanceAnalysisKit';
```

## traceByValue

```TypeScript
function traceByValue(name: string, count: number): void
```

Traces the value changes of an integer variable.Since API version 19, you are advised to use the [traceByValue](#tracebyvalue) API to specify the trace output level.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| count | number | Yes |


## traceByValue

```TypeScript
function traceByValue(level: HiTraceOutputLevel, name: string, count: number): void
```

Traces an integer with the trace output level specified. It is used to mark the name and value of a predefined integer variable to be traced.

**Since:** 19

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | [HiTraceOutputLevel](arkts-performanceanalysis-hitracemeter-hitraceoutputlevel-e.md) | Yes |
| name | string | Yes |
| count | number | Yes |
