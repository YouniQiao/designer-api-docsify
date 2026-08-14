# makeMimeRecord

## Modules to Import

```TypeScript
import { tag } from 'tag';
```

## makeMimeRecord

```TypeScript
function makeMimeRecord(mimeType: string, mimeData: int[]): NdefRecord
```

Creates an NDEF record with mime data.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ndef-function makeMimeRecord(mimeType: string, mimeData: int[]): NdefRecord--><!--Device-ndef-function makeMimeRecord(mimeType: string, mimeData: int[]): NdefRecord-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mimeType | string | Yes | type of mime data for new an NDEF record. |
| mimeData | int[] | Yes | mime data for new an NDEF record. |

**Return value:**

| Type | Description |
| --- | --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) | The instance of NdefRecord. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

