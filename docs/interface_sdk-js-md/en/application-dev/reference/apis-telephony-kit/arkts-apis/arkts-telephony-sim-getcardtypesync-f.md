# getCardTypeSync

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getCardTypeSync

```TypeScript
function getCardTypeSync(slotId: int): CardType
```

Obtains the type of the SIM card in the specified slot.

**Since:** 23

<!--Device-sim-function getCardTypeSync(slotId: int): CardType--><!--Device-sim-function getCardTypeSync(slotId: int): CardType-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Card slot ID. <br>- **0**: card slot 1. <br>- **1**: card slot 2 |

**Return value:**

| Type | Description |
| --- | --- |
| CardType | Type of the SIM card in the specified slot. |

**Examples**

```TypeScript
import { sim } from '@kit.TelephonyKit';

let cardType: sim.CardType = sim.getCardTypeSync(0);
console.info(`the card type is:` + cardType);
```

