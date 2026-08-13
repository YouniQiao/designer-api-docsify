# getCardTypeSync

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getCardTypeSync

```TypeScript
function getCardTypeSync(slotId: number): CardType
```

Obtains the type of the SIM card inserted in a specified slot.

**Since:** 23

**Deprecated since:** -1

<!--Device-sim-function getCardTypeSync(slotId: int): CardType--><!--Device-sim-function getCardTypeSync(slotId: int): CardType-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CardType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-cardemulation-cardtype-e.md) |

## Examples

```TypeScript
import { sim } from '@kit.TelephonyKit';

let cardType: sim.CardType = sim.getCardTypeSync(0);
console.info(`the card type is:` + cardType);
```
