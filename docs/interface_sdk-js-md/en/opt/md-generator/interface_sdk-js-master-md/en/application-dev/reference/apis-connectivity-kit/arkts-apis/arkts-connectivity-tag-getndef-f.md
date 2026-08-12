# getNdef

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNdef

```TypeScript
function getNdef(tagInfo: TagInfo): NdefTag
```

Obtains an [NdefTag](arkts-connectivity-tag-ndeftag-t.md#NdefTag) object based on the tag information.During tag reading, if the tag supports the NDEF technology, an [NdefTag](arkts-connectivity-tag-ndeftag-t.md#NdefTag) object will be created based on the tag information.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-tag-function getNdef(tagInfo: TagInfo): NdefTag--><!--Device-tag-function getNdef(tagInfo: TagInfo): NdefTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NdefTag](arkts-connectivity-nfctech-ndeftag-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3100201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3100201-tag-readwrite-error) |
