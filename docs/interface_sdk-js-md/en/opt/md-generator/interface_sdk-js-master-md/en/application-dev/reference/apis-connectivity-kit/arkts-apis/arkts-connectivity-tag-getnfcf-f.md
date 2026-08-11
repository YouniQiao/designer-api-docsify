# getNfcF

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## getNfcF

```TypeScript
function getNfcF(tagInfo: TagInfo): NfcFTag
```

Obtains an {@link NfcFTag} object based on the tag information.During tag reading, if the tag supports the NFC-F technology, an {@link NfcFTag} object will be created based on the tag information.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-tag-function getNfcF(tagInfo: TagInfo): NfcFTag--><!--Device-tag-function getNfcF(tagInfo: TagInfo): NfcFTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NfcFTag](arkts-connectivity-tag-nfcftag-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
