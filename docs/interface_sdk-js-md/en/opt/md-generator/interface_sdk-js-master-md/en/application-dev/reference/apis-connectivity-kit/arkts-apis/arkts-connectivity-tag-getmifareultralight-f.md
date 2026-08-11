# getMifareUltralight

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## getMifareUltralight

```TypeScript
function getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag
```

Obtains an {@link MifareUltralightTag} object based on the tag information.During tag reading, if the tag supports the MIFARE Ultralight technology,an {@link MifareUltralightTag} object will be created based on the tag information.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-tag-function getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag--><!--Device-tag-function getMifareUltralight(tagInfo: TagInfo): MifareUltralightTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MifareUltralightTag](arkts-connectivity-nfctech-mifareultralighttag-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
