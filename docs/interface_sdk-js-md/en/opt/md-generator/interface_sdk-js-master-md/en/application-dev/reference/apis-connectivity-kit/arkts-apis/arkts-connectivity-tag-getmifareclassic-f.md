# getMifareClassic

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getMifareClassic

```TypeScript
function getMifareClassic(tagInfo: TagInfo): MifareClassicTag
```

Obtains an [MifareClassicTag](arkts-connectivity-tag-mifareclassictag-t.md#MifareClassicTag) object based on the tag information.During tag reading, if the tag supports the MIFARE Classic technology,an [MifareClassicTag](arkts-connectivity-tag-mifareclassictag-t.md#MifareClassicTag) object will be created based on the tag information.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-tag-function getMifareClassic(tagInfo: TagInfo): MifareClassicTag--><!--Device-tag-function getMifareClassic(tagInfo: TagInfo): MifareClassicTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MifareClassicTag](arkts-connectivity-tag-mifareclassictag-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3100201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3100201-tag-readwrite-error) |
