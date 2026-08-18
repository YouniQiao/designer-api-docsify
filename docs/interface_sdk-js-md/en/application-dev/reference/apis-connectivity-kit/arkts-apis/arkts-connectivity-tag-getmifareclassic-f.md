# getMifareClassic

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getMifareClassic

```TypeScript
function getMifareClassic(tagInfo: TagInfo): MifareClassicTag
```

Obtains an [MifareClassicTag](arkts-connectivity-tag-mifareclassictag-t.md) object based on the tag information. During tag reading, if the tag supports the MIFARE Classic technology, an [MifareClassicTag](arkts-connectivity-tag-mifareclassictag-t.md) object will be created based on the tag information.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-tag-function getMifareClassic(tagInfo: TagInfo): MifareClassicTag--><!--Device-tag-function getMifareClassic(tagInfo: TagInfo): MifareClassicTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes | Indicates the dispatched tag information. |

**Return value:**

| Type | Description |
| --- | --- |
| MifareClassicTag | The { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |

