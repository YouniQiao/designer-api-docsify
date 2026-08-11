# messageToBytes

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## messageToBytes

```TypeScript
function messageToBytes(ndefMessage: NdefMessage): number[]
```

Parses an NDEF message into raw bytes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ndef-function messageToBytes(ndefMessage: NdefMessage): int[]--><!--Device-ndef-function messageToBytes(ndefMessage: NdefMessage): int[]-End-->

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
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
