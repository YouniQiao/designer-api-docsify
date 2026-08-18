# getOpNameSync

## Modules to Import

```TypeScript
```

## getOpNameSync

```TypeScript
function getOpNameSync(slotId: number): string
```

Obtains the operator name of the SIM card in a specified slot.

**Since:** 23

<!--Device-sim-function getOpNameSync(slotId: int): string--><!--Device-sim-function getOpNameSync(slotId: int): string-End-->

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

let data: string = sim.getOpNameSync(0);
console.info(`getOpName success, promise: data->${JSON.stringify(data)}`);
```
