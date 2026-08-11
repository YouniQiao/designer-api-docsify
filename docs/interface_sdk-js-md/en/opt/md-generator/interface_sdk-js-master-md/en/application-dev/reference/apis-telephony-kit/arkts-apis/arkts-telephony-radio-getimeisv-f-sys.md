# getIMEISV (System API)

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getIMEISV

```TypeScript
function getIMEISV(slotId: number): string
```

Obtains the software version number of a specified card slot of the device.

**Since:** 12

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function getIMEISV(slotId: int): string--><!--Device-radio-function getIMEISV(slotId: int): string-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
let slotId: number = 0;
let data: string = radio.getIMEISV(slotId);
console.info(`IMEISV is:` + data);
```
