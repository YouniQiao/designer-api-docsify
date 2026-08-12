# MediaAssetEditData (System API)

Represents the edited media asset data.

**Since:** 11

<!--Device-photoAccessHelper-class MediaAssetEditData--><!--Device-photoAccessHelper-class MediaAssetEditData-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## constructor

```TypeScript
constructor(compatibleFormat: string, formatVersion: string)
```

Constructor.

**Since:** 11

<!--Device-MediaAssetEditData-constructor(compatibleFormat: string, formatVersion: string)--><!--Device-MediaAssetEditData-constructor(compatibleFormat: string, formatVersion: string)-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [compatibleFormat](arkts-medialibrary-photoaccesshelper-mediaasseteditdata-c-sys.md) | string | Yes |
| [formatVersion](arkts-medialibrary-photoaccesshelper-mediaasseteditdata-c-sys.md) | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14000011 |

## Examples

```TypeScript
let assetEditData: photoAccessHelper.MediaAssetEditData = new photoAccessHelper.MediaAssetEditData('system', '1.0');
```

## compatibleFormat

```TypeScript
compatibleFormat: string
```

Format of the edited data.

**Type:** string

**Since:** 11

<!--Device-MediaAssetEditData-compatibleFormat: string--><!--Device-MediaAssetEditData-compatibleFormat: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## data

```TypeScript
data: string
```

Content edited.

**Type:** string

**Since:** 11

<!--Device-MediaAssetEditData-data: string--><!--Device-MediaAssetEditData-data: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## formatVersion

```TypeScript
formatVersion: string
```

Version of the data format.

**Type:** string

**Since:** 11

<!--Device-MediaAssetEditData-formatVersion: string--><!--Device-MediaAssetEditData-formatVersion: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.
