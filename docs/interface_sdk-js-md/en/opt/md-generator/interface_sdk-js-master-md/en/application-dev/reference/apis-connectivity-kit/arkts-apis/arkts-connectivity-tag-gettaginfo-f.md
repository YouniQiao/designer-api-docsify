# getTagInfo

## Modules to Import

```TypeScript
import { tag } from '@kit.ConnectivityKit';
```

## getTagInfo

```TypeScript
function getTagInfo(want: Want): TagInfo
```

Parse a [TagInfo](arkts-connectivity-tag-taginfo-i.md#TagInfo) object from Want.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-tag-function getTagInfo(want: Want): TagInfo--><!--Device-tag-function getTagInfo(want: Want): TagInfo-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TagInfo](arkts-connectivity-tag-taginfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
