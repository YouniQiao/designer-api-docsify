# isSimActiveSync

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## isSimActiveSync

```TypeScript
function isSimActiveSync(slotId: int): boolean
```

Checks whether the SIM card in a specified slot is activated.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sim-function isSimActiveSync(slotId: int): boolean--><!--Device-sim-function isSimActiveSync(slotId: int): boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slots supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
import { sim } from '@kit.TelephonyKit';

let isSimActive: boolean = sim.isSimActiveSync(0);
console.info(`the sim is active:` + isSimActive);
```

