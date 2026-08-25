# getSimLabel

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getSimLabel

```TypeScript
function getSimLabel(slotId: number, callback: AsyncCallback<SimLabel>): void
```

Checks the mapping between card slot IDs and SIM cards.  
- Slot 1 corresponds to SIM card 1 or SIM card 2.  
- Slot 2 corresponds to SIM card 2 or eSIMX.

**Since:** 20

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SimLabel](arkts-telephony-sim-simlabel-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |


## getSimLabel

```TypeScript
function getSimLabel(slotId: number): Promise<SimLabel>
```

Obtains the SIM card label. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SimLabel](arkts-telephony-sim-simlabel-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
