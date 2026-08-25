# getRadioTechSync

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getRadioTechSync

```TypeScript
function getRadioTechSync(slotId: number): NetworkRadioTech
```

Obtains the RAT used in the CS and PS domains for the SIM card in the specified slot. The CS domain refers to the Circuit Switched domain, and the PS domain refers to the Packet Switched domain.  
**Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 18

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NetworkRadioTech](arkts-telephony-radio-networkradiotech-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
