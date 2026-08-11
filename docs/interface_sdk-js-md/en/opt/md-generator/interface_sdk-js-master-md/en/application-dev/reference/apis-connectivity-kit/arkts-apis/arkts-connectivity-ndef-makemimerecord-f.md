# makeMimeRecord

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## makeMimeRecord

```TypeScript
function makeMimeRecord(mimeType: string, mimeData: number[]): NdefRecord
```

Creates an NDEF record with mime data.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ndef-function makeMimeRecord(mimeType: string, mimeData: int[]): NdefRecord--><!--Device-ndef-function makeMimeRecord(mimeType: string, mimeData: int[]): NdefRecord-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |
| mimeData | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
