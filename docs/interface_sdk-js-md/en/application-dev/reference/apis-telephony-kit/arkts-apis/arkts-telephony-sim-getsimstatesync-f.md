# getSimStateSync

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getSimStateSync

```TypeScript
function getSimStateSync(slotId: int): SimState
```

Obtains the state of the SIM card in the specified slot.

**Since:** 23

<!--Device-sim-function getSimStateSync(slotId: int): SimState--><!--Device-sim-function getSimStateSync(slotId: int): SimState-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Card slot ID. <br>- **0**: card slot 1. <br>- **1**: card slot 2 |

**Return value:**

| Type | Description |
| --- | --- |
| SimState | State of the SIM card in the specified slot. |

**Examples**

```TypeScript
import { sim } from '@kit.TelephonyKit';

let simState: sim.SimState = sim.getSimStateSync(0);
console.info(`The sim state is:` + simState);
```

