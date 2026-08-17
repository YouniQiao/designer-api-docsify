# messageToBytes

## Modules to Import

```TypeScript
import { tag } from 'tag';
```

## messageToBytes

```TypeScript
function messageToBytes(ndefMessage: NdefMessage): int[]
```

Parses an NDEF message into raw bytes.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ndef-function messageToBytes(ndefMessage: NdefMessage): int[]--><!--Device-ndef-function messageToBytes(ndefMessage: NdefMessage): int[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ndefMessage | NdefMessage | Yes | An NDEF message to parse. |

**Return value:**

| Type | Description |
| --- | --- |
| int[] | Returns the raw bytes of an NDEF message. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

