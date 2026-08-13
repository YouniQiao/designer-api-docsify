# getSimStateSync

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getSimStateSync

```TypeScript
function getSimStateSync(slotId: number): SimState
```

Obtains the state of the SIM card in a specified slot.

**Since:** 23

**Deprecated since:** -1

<!--Device-sim-function getSimStateSync(slotId: int): SimState--><!--Device-sim-function getSimStateSync(slotId: int): SimState-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SimState](arkts-telephony-sim-simstate-e.md) |

## Examples

```TypeScript
import { sim } from '@kit.TelephonyKit';

let simState: sim.SimState = sim.getSimStateSync(0);
console.info(`The sim state is:` + simState);
```
