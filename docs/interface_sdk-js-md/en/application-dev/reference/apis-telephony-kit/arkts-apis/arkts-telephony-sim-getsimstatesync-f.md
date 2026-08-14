# getSimStateSync

## Modules to Import

```TypeScript
import { sim } from 'sim';
```

## getSimStateSync

```TypeScript
function getSimStateSync(slotId: int): SimState
```

Obtains the state of the SIM card in a specified slot.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sim-function getSimStateSync(slotId: int): SimState--><!--Device-sim-function getSimStateSync(slotId: int): SimState-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slots supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| SimState | Returns one of the following SIM card states: &lt;ul&gt; &lt;li&gt;{ |

## Examples

```TypeScript
import { sim } from '@kit.TelephonyKit';

let simState: sim.SimState = sim.getSimStateSync(0);
console.info(`The sim state is:` + simState);
```

