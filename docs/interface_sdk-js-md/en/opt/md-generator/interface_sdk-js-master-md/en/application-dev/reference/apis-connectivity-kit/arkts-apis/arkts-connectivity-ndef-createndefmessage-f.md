# createNdefMessage

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## createNdefMessage

```TypeScript
function createNdefMessage(data: number[]): NdefMessage
```

Creates an NDEF message with raw bytes.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ndef-function createNdefMessage(data: int[]): NdefMessage--><!--Device-ndef-function createNdefMessage(data: int[]): NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NdefMessage](arkts-connectivity-nfctech-ndefmessage-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## createNdefMessage

```TypeScript
function createNdefMessage(ndefRecords: NdefRecord[]): NdefMessage
```

Creates an NDEF message with record list.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ndef-function createNdefMessage(ndefRecords: NdefRecord[]): NdefMessage--><!--Device-ndef-function createNdefMessage(ndefRecords: NdefRecord[]): NdefMessage-End-->

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
