# getSignalInformationSync

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getSignalInformationSync

```TypeScript
function getSignalInformationSync(slotId: number): Array<SignalInformation>
```

Obtains a list of signal strengths of the network with which the SIM card in the specified slot is registered.

**Since:** 10

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;SignalInformation & gt; |
