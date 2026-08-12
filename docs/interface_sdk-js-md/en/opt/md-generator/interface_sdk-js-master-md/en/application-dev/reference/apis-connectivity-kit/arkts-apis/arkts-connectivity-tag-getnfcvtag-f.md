# getNfcVTag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNfcVTag

```TypeScript
function getNfcVTag(tagInfo: TagInfo): NfcVTag
```

Obtains an [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md#NfcVTag) object based on the tag information.&lt;p&gt;During tag reading, if the tag supports the NFC-V technology, an [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md#NfcVTag) object will be created based on the tag information.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getNfcV](arkts-connectivity-tag-getnfcv-f.md#getNfcV)

<!--Device-tag-function getNfcVTag(tagInfo: TagInfo): NfcVTag--><!--Device-tag-function getNfcVTag(tagInfo: TagInfo): NfcVTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NfcVTag](arkts-connectivity-tag-nfcvtag-t.md) |
