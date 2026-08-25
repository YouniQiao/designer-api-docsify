# makeApplicationRecord

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## makeApplicationRecord

```TypeScript
function makeApplicationRecord(bundleName: string): NdefRecord
```

Creates an NDEF record based on the specified application bundle name.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NdefRecord](arkts-connectivity-tag-ndefrecord-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
