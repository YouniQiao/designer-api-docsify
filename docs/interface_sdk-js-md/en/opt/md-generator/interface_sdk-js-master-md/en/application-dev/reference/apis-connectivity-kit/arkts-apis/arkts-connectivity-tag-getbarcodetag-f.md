# getBarcodeTag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getBarcodeTag

```TypeScript
function getBarcodeTag(tagInfo: TagInfo): BarcodeTag
```

Obtains an [BarcodeTag](arkts-connectivity-tag-barcodetag-t.md#BarcodeTag) object based on the tag information. During tag reading, if the tag supports the NfcBarcode technology, an [BarcodeTag](arkts-connectivity-tag-barcodetag-t.md#BarcodeTag) object will be created.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
