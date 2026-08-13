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

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-tag-function getNfcV(tagInfo: TagInfo): NfcVTag--><!--Device-tag-function getNfcV(tagInfo: TagInfo): NfcVTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) |
