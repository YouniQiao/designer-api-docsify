# getMaxSimCount

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getMaxSimCount

```TypeScript
function getMaxSimCount(): int
```

Obtains the maximum number of SIM cards that can be used simultaneously on the device, that is, the maximum number of SIM card slots.

**Since:** 23

<!--Device-sim-function getMaxSimCount(): int--><!--Device-sim-function getMaxSimCount(): int-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the maximum number of SIM card slots. |

**Examples**

```TypeScript
import { sim } from '@kit.TelephonyKit';

console.info("Result: "+ sim.getMaxSimCount());
```

