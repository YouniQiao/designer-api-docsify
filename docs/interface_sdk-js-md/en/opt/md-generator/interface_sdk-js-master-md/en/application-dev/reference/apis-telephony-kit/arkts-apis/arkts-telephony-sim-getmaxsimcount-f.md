# getMaxSimCount

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getMaxSimCount

```TypeScript
function getMaxSimCount(): number
```

Obtains the maximum number of SIM cards that can be used simultaneously on the device,that is, the maximum number of SIM card slots.

**Since:** 7

<!--Device-sim-function getMaxSimCount(): int--><!--Device-sim-function getMaxSimCount(): int-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { sim } from '@kit.TelephonyKit';

console.info("Result: "+ sim.getMaxSimCount());
```
