# isSupported

## Modules to Import

```TypeScript
```

## isSupported

```TypeScript
function isSupported(slotId: number): boolean
```

Whether embedded subscriptions are currently supported.

**Since:** 23

<!--Device-eSIM-function isSupported(slotId: int): boolean--><!--Device-eSIM-function isSupported(slotId: int): boolean-End-->

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
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) |

**Examples**

```TypeScript
import { eSIM } from '@kit.TelephonyKit';

let isSupported: boolean = eSIM.isSupported(1);
console.info(`the esim is Supported:` + isSupported);
```
