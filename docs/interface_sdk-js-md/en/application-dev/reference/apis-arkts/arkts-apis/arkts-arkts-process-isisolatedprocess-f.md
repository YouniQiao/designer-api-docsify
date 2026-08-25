# isIsolatedProcess

## Modules to Import

```TypeScript
import { process } from '@kit.ArkTS';
```

## isIsolatedProcess

```TypeScript
function isIsolatedProcess(): boolean
```

Checks whether this process is isolated.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
let result = process.isIsolatedProcess();
```
