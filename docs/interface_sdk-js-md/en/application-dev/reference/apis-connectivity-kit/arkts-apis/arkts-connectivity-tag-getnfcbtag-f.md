# getNfcBTag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNfcBTag

```TypeScript
function getNfcBTag(tagInfo: TagInfo): NfcBTag
```

Obtains an [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) object based on the tag information. &lt;p&gt;During tag reading, if the tag supports the NFC-B technology, an [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) object will be created based on the tag information.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getNfcB](arkts-connectivity-tag-getnfcb-f.md)

<!--Device-tag-function getNfcBTag(tagInfo: TagInfo): NfcBTag--><!--Device-tag-function getNfcBTag(tagInfo: TagInfo): NfcBTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes | Indicates the tag information. |

**Return value:**

| Type | Description |
| --- | --- |
| NfcBTag | The { |

