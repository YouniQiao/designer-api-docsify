# getSimLabelSync

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getSimLabelSync

```TypeScript
function getSimLabelSync(slotId: number): SimLabel
```

Obtains the SIM card label synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-sim-function getSimLabelSync(slotId: int): SimLabel--><!--Device-sim-function getSimLabelSync(slotId: int): SimLabel-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SimLabel](arkts-telephony-sim-simlabel-i.md) |

## Examples

```TypeScript
import { sim } from '@kit.TelephonyKit';


let simLabel: sim.SimLabel = sim.getSimLabelSync(0);
console.info(`The sim state is:` + simLabel);
```
