# NdefMessage

Provides methods for Message of NDEF.

**Since:** 23

<!--Device-unnamed-export interface NdefMessage--><!--Device-unnamed-export interface NdefMessage-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

## getNdefRecords

```TypeScript
getNdefRecords(): tag.NdefRecord[]
```

Obtains all NDEF records.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NdefMessage-getNdefRecords(): tag.NdefRecord[]--><!--Device-NdefMessage-getNdefRecords(): tag.NdefRecord[]-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Return value:**

| Type | Description |
| --- | --- |
| tag.NdefRecord[] | List of NDEF records obtained. For details, see *NFCForum-TS-NDEF_1.0*. |

