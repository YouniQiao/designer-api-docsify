# getOperatorNameSync

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## getOperatorNameSync

```TypeScript
function getOperatorNameSync(slotId: number): string
```

Get the operator name of the specified SIM card slot.

**Since:** 10

<!--Device-radio-function getOperatorNameSync(slotId: int): string--><!--Device-radio-function getOperatorNameSync(slotId: int): string-End-->

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
let slotId: number = 0;
let operatorName: string = radio.getOperatorNameSync(slotId);
console.info(`operator name is:` + operatorName);
```
