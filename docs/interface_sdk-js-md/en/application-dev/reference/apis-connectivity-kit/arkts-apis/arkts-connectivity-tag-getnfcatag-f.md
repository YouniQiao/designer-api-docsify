# getNfcATag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNfcATag

```TypeScript
function getNfcATag(tagInfo: TagInfo): NfcATag
```

Obtains an [NfcATag](arkts-connectivity-tag-nfcatag-t.md) object based on the tag information. &lt;p&gt;During tag reading, if the tag supports the NFC-A technology, an [NfcATag](arkts-connectivity-tag-nfcatag-t.md) object will be created based on the tag information.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getNfcA](arkts-connectivity-tag-getnfca-f.md)

<!--Device-tag-function getNfcATag(tagInfo: TagInfo): NfcATag--><!--Device-tag-function getNfcATag(tagInfo: TagInfo): NfcATag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes | Indicates the tag information. |

**Return value:**

| Type | Description |
| --- | --- |
| NfcATag | The { |

