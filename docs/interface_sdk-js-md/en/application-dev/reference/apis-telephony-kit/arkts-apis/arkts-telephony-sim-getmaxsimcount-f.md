# getMaxSimCount

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getMaxSimCount

```TypeScript
function getMaxSimCount(): int
```

Obtains the number of card slots.

**Since:** 23

<!--Device-sim-function getMaxSimCount(): int--><!--Device-sim-function getMaxSimCount(): int-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| Type | Description |
| --- | --- |
| int | Number of card slots. |

**Examples**

```TypeScript
import { sim } from '@kit.TelephonyKit';

console.info("Result: "+ sim.getMaxSimCount());
```

