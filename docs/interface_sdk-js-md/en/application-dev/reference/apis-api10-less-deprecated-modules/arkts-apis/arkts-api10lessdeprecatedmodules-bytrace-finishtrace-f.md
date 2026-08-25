# finishTrace

## Modules to Import

```TypeScript
```

## finishTrace

```TypeScript
function finishTrace(name: string, taskId: number): void
```

Marks the end of a timeslice trace task.

> **NOTE：**&gt;
> To stop a trace task, the values of name and task ID in **finishTrace** must be the same as those in
> **startTrace**.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** finishTrace

**System capability:** SystemCapability.HiviewDFX.HiTrace

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| taskId | number | Yes |
