# uptime

## Modules to Import

```TypeScript
import { process } from '@kit.ArkTS';
```

## uptime

```TypeScript
function uptime(): number
```

Obtains the running time of the current system, in seconds.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
let time = process.uptime();
```
