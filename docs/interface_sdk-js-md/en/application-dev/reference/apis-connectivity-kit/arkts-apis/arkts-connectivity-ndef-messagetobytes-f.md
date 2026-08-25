# messageToBytes

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## messageToBytes

```TypeScript
function messageToBytes(ndefMessage: NdefMessage): number[]
```

Converts an NDEF message to bytes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ndefMessage | [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
