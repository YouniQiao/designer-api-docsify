# getNfcFTag

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getNfcFTag

```TypeScript
function getNfcFTag(tagInfo: TagInfo): NfcFTag
```

Obtains an [NfcFTag](arkts-connectivity-tag-nfcftag-t.md#NfcFTag) object based on the tag information.&lt;p&gt;During tag reading, if the tag supports the NFC-F technology, an [NfcFTag](arkts-connectivity-tag-nfcftag-t.md#NfcFTag) object will be created based on the tag information.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [getNfcF](arkts-connectivity-tag-getnfcf-f.md#getNfcF)

<!--Device-tag-function getNfcFTag(tagInfo: TagInfo): NfcFTag--><!--Device-tag-function getNfcFTag(tagInfo: TagInfo): NfcFTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes | Indicates the tag information. |

**Return value:**

| Type | Description |
| --- | --- |
| NfcFTag | The { |

