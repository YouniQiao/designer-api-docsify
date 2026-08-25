# MediaAssetEditData (System API)

Represents the edited media asset data.

**Since:** 11

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 14000011 |

## compatibleFormat

```TypeScript
compatibleFormat: string
```

Format of the edited data.

**Type:** string

**Since:** 11

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## data

```TypeScript
data: string
```

Content edited.

**Type:** string

**Since:** 11

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.

## formatVersion

```TypeScript
formatVersion: string
```

Version of the data format.

**Type:** string

**Since:** 11

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**System API:** This is a system API.
