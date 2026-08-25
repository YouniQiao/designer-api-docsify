# getNfcATag

## Modules to Import

```TypeScript
import { tag } from 'kits/@kit.ConnectivityKit';
```

## getNfcATag

```TypeScript
function getNfcATag(tagInfo: TagInfo): NfcATag
```

Obtains an **NfcATag** object, which allows access to the tags that use the NFC-A technology.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. Use
> [tag.getNfcA](arkts-connectivity-tag-getnfca-f.md) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getNfcA](arkts-connectivity-tag-getnfca-f.md)

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tagInfo | [TagInfo](arkts-connectivity-tag-taginfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NfcATag](arkts-connectivity-tag-nfcatag-t.md) |
