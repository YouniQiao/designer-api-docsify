# getNfcB

## Modules to Import

```TypeScript
import { tag } from 'tag';
```

## getNfcB

```TypeScript
function getNfcB(tagInfo: TagInfo): NfcBTag
```

Obtains an [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md#NfcBTag) object based on the tag information. During tag reading, if the tag supports the NFC-B technology, an [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md#NfcBTag) object will be created based on the tag information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-tag-function getNfcB(tagInfo: TagInfo): NfcBTag--><!--Device-tag-function getNfcB(tagInfo: TagInfo): NfcBTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes | Indicates the dispatched tag information. |

**Return value:**

| Type | Description |
| --- | --- |
| NfcBTag | The { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |

