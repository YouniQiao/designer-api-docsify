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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-tag-function getBarcodeTag(tagInfo: TagInfo): BarcodeTag--><!--Device-tag-function getBarcodeTag(tagInfo: TagInfo): BarcodeTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes | Indicates the dispatched tag information. |

**Return value:**

| Type | Description |
| --- | --- |
| BarcodeTag | The { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |

