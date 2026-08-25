# startTrace

## Modules to Import

```TypeScript
```

## startTrace

```TypeScript
function startTrace(name: string, taskId: number, expectedTime?: number): void
```

Marks the start of a timeslice trace task.

> **NOTE：**&gt;
> If multiple trace tasks with the same name need to be performed at the same time or a trace task needs to be
> performed multiple times concurrently, different task IDs must be specified in **startTrace**. If the trace tasks
> with the same name are not performed at the same time, the same task ID can be used. For details, see the
> bytrace.finishTrace example.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 8

**Substitutes:** startTrace

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| taskId | number | Yes |
| expectedTime | number | No |

**Examples**

```TypeScript
bytrace.startTrace("myTestFunc", 1);
bytrace.startTrace("myTestFunc", 1, 5); // The expected duration of the trace is 5 ms.
```
