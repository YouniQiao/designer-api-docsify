# getNfcV

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNfcV

```TypeScript
function getNfcV(tagInfo: TagInfo): NfcVTag
```

Obtains an [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md#NfcVTag) object based on the tag information. During tag reading, if the tag supports the NFC-V technology, an [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md#NfcVTag) object will be created based on the tag information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-tag-function getNfcV(tagInfo: TagInfo): NfcVTag--><!--Device-tag-function getNfcV(tagInfo: TagInfo): NfcVTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes | Indicates the dispatched tag information. |

**Return value:**

| Type | Description |
| --- | --- |
| NfcVTag | The { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |

