# getRadioTech

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getRadioTech

```TypeScript
function getRadioTech(slotId: number, callback: AsyncCallback<NetworkRadioTech>): void
```

Obtains the RAT used in the CS and PS domains for the SIM card in the specified slot. This API uses an asynchronous callback to return the result. The CS domain refers to the Circuit Switched domain, and the PS domain refers to the Packet Switched domain.  
**Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 6

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[NetworkRadioTech](arkts-telephony-radio-networkradiotech-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |


## getRadioTech

```TypeScript
function getRadioTech(slotId: number): Promise<NetworkRadioTech>
```

Obtains the RAT used in the CS and PS domains for the SIM card in the specified slot. This API uses a promise to return the result. The CS domain refers to the Circuit Switched domain, and the PS domain refers to the Packet Switched domain.  
**Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 6

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;{psRadioTech: RadioTechnology, csRadioTech: RadioTechnology |
| Promise&lt;[NetworkRadioTech](arkts-telephony-radio-networkradiotech-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
