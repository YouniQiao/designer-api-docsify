# traceByValue

## traceByValue

```TypeScript
function traceByValue(name: string, count: long): void
```

Traces the value changes of an integer variable. Since API version 19, you are advised to use the [traceByValue\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_19+\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_()]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API to specify the trace output level

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function traceByValue(name: string, count: long): void--><!--Device-hiTraceMeter-function traceByValue(name: string, count: long): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the integer variable to trace.The maximum length of a trace record is 512 bytes. The excess part will be truncated. It is recommended that the length of this parameter be less than or equal to 420 bytes. |
| count | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | Value of an integer variable. |

**Example**

```TypeScript
let traceCount = 3;
hiTraceMeter.traceByValue("myTestCount", traceCount);
traceCount = 4;
hiTraceMeter.traceByValue("myTestCount", traceCount);
// Service flow...
```


## traceByValue

```TypeScript
function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void
```

Traces an integer with the trace output level specified. It is used to mark the name and value of a predefined integer variable to be traced.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-hiTraceMeter-function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void--><!--Device-hiTraceMeter-function traceByValue(level: HiTraceOutputLevel, name: string, count: long): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Trace output level. |
| name | string | Yes | Name of the integer variable to trace.The maximum length of a trace record is 512 bytes. The excess part will be truncated. It is recommended that the length of this parameter be less than or equal to 420 bytes. |
| count | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | Value of an integer variable. |

**Example**

```TypeScript
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
let traceCount = 3;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
traceCount = 4;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
// Service flow...
```

