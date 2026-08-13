# createNdefMessageByRecords

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## createNdefMessageByRecords

```TypeScript
function createNdefMessageByRecords(ndefRecords: NdefRecord[]): NdefMessage
```

Creates an NDEF message with record list.

**Since:** 23

**Deprecated since:** -1

<!--Device-ndef-function createNdefMessageByRecords(ndefRecords: NdefRecord[]): NdefMessage--><!--Device-ndef-function createNdefMessageByRecords(ndefRecords: NdefRecord[]): NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ndefRecords | [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
