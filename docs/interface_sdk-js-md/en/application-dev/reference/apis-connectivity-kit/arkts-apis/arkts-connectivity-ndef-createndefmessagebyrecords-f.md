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

<!--Device-ndef-function createNdefMessageByRecords(ndefRecords: NdefRecord[]): NdefMessage--><!--Device-ndef-function createNdefMessageByRecords(ndefRecords: NdefRecord[]): NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ndefRecords | [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md)[] | Yes | The NDEF records to parse NDEF message. |

**Return value:**

| Type | Description |
| --- | --- |
| NdefMessage | The instance of NdefMessage. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

