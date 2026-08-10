# traceByValue

## traceByValue

```TypeScript
function traceByValue(name: string, count: number): void
```

标记预追踪耗时任务的数值变量，该变量的数值会不断变化。traceByValue可独立使用，用于记录某个数值变量的变化轨迹。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** ohos.hiTraceMeter.traceByValue

<!--Device-bytrace-function traceByValue(name: string, count: number): void--><!--Device-bytrace-function traceByValue(name: string, count: number): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 数值变量的名称。 |
| count | number | Yes | 数值变量的值。 |

## Examples

```TypeScript
let traceCount = 3;
bytrace.traceByValue("myTestCount", traceCount);
traceCount = 4;
bytrace.traceByValue("myTestCount", traceCount);
// Service flow...
```

