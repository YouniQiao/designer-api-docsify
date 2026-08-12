# getBarcodeTag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getBarcodeTag

```TypeScript
function getBarcodeTag(tagInfo: TagInfo): BarcodeTag
```

Obtains an [BarcodeTag](arkts-connectivity-tag-barcodetag-t.md#BarcodeTag) object based on the tag information.During tag reading, if the tag supports the NfcBarcode technology,an [BarcodeTag](arkts-connectivity-tag-barcodetag-t.md#BarcodeTag) object will be created.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-tag-function getBarcodeTag(tagInfo: TagInfo): BarcodeTag--><!--Device-tag-function getBarcodeTag(tagInfo: TagInfo): BarcodeTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BarcodeTag](arkts-connectivity-nfctech-barcodetag-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3100201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3100201-tag-readwrite-error) |
