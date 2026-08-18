# traceByValue

## Modules to Import

```TypeScript
```

## traceByValue

```TypeScript
function traceByValue(name: string, count: number): void
```

Defines a numeric variable that indicates the number of timeslice trace tasks.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** traceByValue

<!--Device-bytrace-function traceByValue(name: string, count: number): void--><!--Device-bytrace-function traceByValue(name: string, count: number): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| count | number | Yes |

**Examples**

```TypeScript
let traceCount = 3;
bytrace.traceByValue("myTestCount", traceCount);
traceCount = 4;
bytrace.traceByValue("myTestCount", traceCount);
// Service flow...
```
