# getCardTypeSync

## getCardTypeSync

```TypeScript
function getCardTypeSync(slotId: number): CardType
```

Obtains the type of the SIM card inserted in a specified slot.

**起始版本：** 10

<!--Device-sim-function getCardTypeSync(slotId: int): CardType--><!--Device-sim-function getCardTypeSync(slotId: int): CardType-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [CardType](arkts-telephony-sim-cardtype-e.md) |

## 示例

```TypeScript
import { sim } from '@kit.TelephonyKit';

let cardType: sim.CardType = sim.getCardTypeSync(0);
console.info(`the card type is:` + cardType);
```
