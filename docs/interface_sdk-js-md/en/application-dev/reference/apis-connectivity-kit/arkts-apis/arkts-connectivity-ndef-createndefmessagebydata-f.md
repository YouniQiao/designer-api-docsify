# createNdefMessageByData

## Modules to Import

```TypeScript
import { tag } from 'tag';
```

## createNdefMessageByData

```TypeScript
function createNdefMessageByData(data: int[]): NdefMessage
```

Creates an NDEF message with raw bytes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ndef-function createNdefMessageByData(data: int[]): NdefMessage--><!--Device-ndef-function createNdefMessageByData(data: int[]): NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | int[] | Yes | The raw bytes to parse NDEF message. |

**Return value:**

| Type | Description |
| --- | --- |
| NdefMessage | The instance of NdefMessage. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

