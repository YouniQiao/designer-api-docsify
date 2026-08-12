# getSimOperatorNumericSync

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getSimOperatorNumericSync

```TypeScript
function getSimOperatorNumericSync(slotId: number): string
```

Obtains the home PLMN number of the SIM card in a specified slot.

&lt;p&gt;The value is recorded in the SIM card and is irrelevant to the network with which the SIM card is currently registered.

**Since:** 10

<!--Device-sim-function getSimOperatorNumericSync(slotId: int): string--><!--Device-sim-function getSimOperatorNumericSync(slotId: int): string-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { sim } from '@kit.TelephonyKit';

let numeric: string = sim.getSimOperatorNumericSync(0);
console.info(`the sim operator numeric is:` + numeric);
```
