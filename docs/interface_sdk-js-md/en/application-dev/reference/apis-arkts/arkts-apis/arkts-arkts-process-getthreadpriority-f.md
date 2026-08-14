# getThreadPriority

## Modules to Import

```TypeScript
import { process } from 'process';
```

## getThreadPriority

```TypeScript
function getThreadPriority(v: number): number
```

Obtains the thread priority based on the specified TID.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [getThreadPriority](arkts-arkts-process-processmanager-c.md#getThreadPriority)

<!--Device-process-function getThreadPriority(v: number): number--><!--Device-process-function getThreadPriority(v: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | number | Yes | TID. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Priority of the thread. The priority depends on the operating system. |

## Examples

```TypeScript
let tid = process.tid;
let pres = process.getThreadPriority(tid);
```

