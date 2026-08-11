# isOperatorSimCard (System API)

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## isOperatorSimCard

```TypeScript
function isOperatorSimCard(slotId: number, operator: OperatorSimCard): boolean
```

Indicates whether the SIM card in a specified slot is a specified operator.

**Since:** 11

<!--Device-sim-function isOperatorSimCard(slotId: int, operator: OperatorSimCard): boolean--><!--Device-sim-function isOperatorSimCard(slotId: int, operator: OperatorSimCard): boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| operator | [OperatorSimCard](arkts-telephony-sim-operatorsimcard-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { sim } from '@kit.TelephonyKit';

let slotId : number = 0;
let operator : sim.OperatorSimCard = sim.OperatorSimCard.CHINA_TELECOM_CARD;
try {
    let isOperatorSimCard: boolean = sim.isOperatorSimCard(slotId, operator);
    console.info(`is operator sim card: ` + isOperatorSimCard);
} catch (err) {
    console.error("isOperatorSimCard err: " + JSON.stringify(err));
}
```
