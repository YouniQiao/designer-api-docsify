# getSimOperatorNumericSync

## getSimOperatorNumericSync

```TypeScript
function getSimOperatorNumericSync(slotId: int): string
```

Obtains the home PLMN number of the SIM card in a specified slot. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_The value is recorded in the SIM card and is irrelevant to the network with which the SIM card is currently registered.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-sim-function getSimOperatorNumericSync(slotId: int): string--><!--Device-sim-function getSimOperatorNumericSync(slotId: int): string-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Indicates the card slot index number,ranging from 0 to the maximum card slots supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the PLMN number; returns an empty string if no SIM card is inserted. |

**Example**

```TypeScript
import { sim } from '@kit.TelephonyKit';

let numeric: string = sim.getSimOperatorNumericSync(0);
console.info(`the sim operator numeric is:` + numeric);
```

