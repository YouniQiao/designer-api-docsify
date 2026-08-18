# getSimSpnSync

## Modules to Import

```TypeScript
```

## getSimSpnSync

```TypeScript
function getSimSpnSync(slotId: number): string
```

Obtains the service provider name (SPN) of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the EFSPN file of the SIM card and is irrelevant to the network with which the SIM card is currently registered.

**Since:** 23

<!--Device-sim-function getSimSpnSync(slotId: int): string--><!--Device-sim-function getSimSpnSync(slotId: int): string-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { sim } from '@kit.TelephonyKit';

let spn: string = sim.getSimSpnSync(0);
console.info(`the sim card spn is:` + spn);
```
