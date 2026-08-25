# isSupported

## Modules to Import

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## isSupported

```TypeScript
function isSupported(slotId: number): boolean
```

Checks whether the specified card slot supports the eSIM function.

**Since:** 18

**System capability:** SystemCapability.Telephony.CoreService.Esim

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) |
