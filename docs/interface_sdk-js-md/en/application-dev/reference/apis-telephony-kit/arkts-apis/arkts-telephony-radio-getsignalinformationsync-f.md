# getSignalInformationSync

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## getSignalInformationSync

```TypeScript
function getSignalInformationSync(slotId: int): Array<SignalInformation>
```

Obtains a list of signal strengths of the network with which the SIM card in the specified slot is registered.

**Since:** 23

<!--Device-radio-function getSignalInformationSync(slotId: int): Array<SignalInformation>--><!--Device-radio-function getSignalInformationSync(slotId: int): Array<SignalInformation>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Card slot ID. <br>- **0**: card slot 1. <br>- **1**: card slot 2 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;SignalInformation&gt; | Array of child class objects derived from [SignalInformation]{ |

**Examples**

```TypeScript
let slotId: number = 0;
let signalInfo: Array<radio.SignalInformation> = radio.getSignalInformationSync(slotId);
console.info(`signal information size is:` + signalInfo.length);
```

