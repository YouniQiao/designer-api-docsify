# getNfcBTag

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## getNfcBTag

```TypeScript
function getNfcBTag(tagInfo: TagInfo): NfcBTag
```

Obtains an {@link NfcBTag} object based on the tag information.&lt;p&gt;During tag reading, if the tag supports the NFC-B technology, an {@link NfcBTag} object will be created based on the tag information.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.nfc.tag/tag#getNfcB

<!--Device-tag-function getNfcBTag(tagInfo: TagInfo): NfcBTag--><!--Device-tag-function getNfcBTag(tagInfo: TagInfo): NfcBTag-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NfcBTag](arkts-connectivity-tag-nfcbtag-t.md) |
