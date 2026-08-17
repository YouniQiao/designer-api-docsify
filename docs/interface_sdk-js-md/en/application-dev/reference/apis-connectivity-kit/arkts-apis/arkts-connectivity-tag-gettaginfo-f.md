# getTagInfo

## Modules to Import

```TypeScript
import { tag } from 'tag';
```

## getTagInfo

```TypeScript
function getTagInfo(want: Want): TagInfo
```

Parse a [TagInfo](arkts-connectivity-tag-taginfo-i.md#taginfo) object from Want.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-tag-function getTagInfo(want: Want): TagInfo--><!--Device-tag-function getTagInfo(want: Want): TagInfo-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | The want object that contains the values of TagInfo. |

**Return value:**

| Type | Description |
| --- | --- |
| [TagInfo](arkts-connectivity-tag-taginfo-i.md) | The { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | The parameter check failed. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

