# getSignalInformationSync

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## getSignalInformationSync

```TypeScript
function getSignalInformationSync(slotId: number): Array<SignalInformation>
```

Obtains the list of signal strength information of the registered network corresponding to a specified SIM card.

**Since:** 10

<!--Device-radio-function getSignalInformationSync(slotId: int): Array<SignalInformation>--><!--Device-radio-function getSignalInformationSync(slotId: int): Array<SignalInformation>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;SignalInformation & gt; |

## Examples

```TypeScript
let slotId: number = 0;
let signalInfo: Array<radio.SignalInformation> = radio.getSignalInformationSync(slotId);
console.info(`signal information size is:` + signalInfo.length);
```
