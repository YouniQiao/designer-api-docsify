# isSupported

## Modules to Import

```TypeScript
import { eSIM } from 'eSIM';
```

## isSupported

```TypeScript
function isSupported(slotId: int): boolean
```

Whether embedded subscriptions are currently supported.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-eSIM-function isSupported(slotId: int): boolean--><!--Device-eSIM-function isSupported(slotId: int): boolean-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) | System internal error. |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) | Service connection failed. |

## Examples

```TypeScript
import { eSIM } from '@kit.TelephonyKit';

let isSupported: boolean = eSIM.isSupported(1);
console.info(`the esim is Supported:` + isSupported);
```

