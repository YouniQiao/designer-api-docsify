# createNdefMessageByData

## Modules to Import

```TypeScript
```

## createNdefMessageByData

```TypeScript
function createNdefMessageByData(data: number[]): NdefMessage
```

Creates an NDEF message with raw bytes.

**Since:** 23

<!--Device-ndef-function createNdefMessageByData(data: int[]): NdefMessage--><!--Device-ndef-function createNdefMessageByData(data: int[]): NdefMessage-End-->

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
