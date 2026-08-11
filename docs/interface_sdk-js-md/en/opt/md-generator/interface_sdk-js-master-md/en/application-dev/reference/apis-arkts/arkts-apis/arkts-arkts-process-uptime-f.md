# uptime

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## uptime

```TypeScript
function uptime(): number
```

Obtains the running time of the current system, in seconds.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function uptime(): number--><!--Device-process-function uptime(): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let time = process.uptime();
```
