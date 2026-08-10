# MediaAssetEditData (System API)

Represents the edited media asset data.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-class MediaAssetEditData--><!--Device-photoAccessHelper-class MediaAssetEditData-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## constructor

```TypeScript
constructor(compatibleFormat: string, formatVersion: string)
```

Constructor.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-MediaAssetEditData-constructor(compatibleFormat: string, formatVersion: string)--><!--Device-MediaAssetEditData-constructor(compatibleFormat: string, formatVersion: string)-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| compatibleFormat | string | Yes | Format of the edited data. |
| formatVersion | string | Yes | Version of the data format. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 202 | Called by non-system application |
| 14000011 | System inner fail |

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

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

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

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-MediaAssetEditData-formatVersion: string--><!--Device-MediaAssetEditData-formatVersion: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

