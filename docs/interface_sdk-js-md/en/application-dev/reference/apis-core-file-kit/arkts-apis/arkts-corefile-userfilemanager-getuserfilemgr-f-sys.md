# getUserFileMgr (System API)

## Modules to Import

```TypeScript
import { userFileManager } from 'kits/@kit.CoreFileKit';
```

## getUserFileMgr

```TypeScript
function getUserFileMgr(context: Context): UserFileManager
```

Obtains a **UserFileManager** instance. This instance can be used to access and modify user media data (such as audio and video assets, images, and documents).

**Since:** 9

**Deprecated since:** 26.0.0

**Substitutes:** [getPhotoAccessHelper](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-getphotoaccesshelper-f.md)

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UserFileManager](arkts-corefile-userfilemanager-userfilemanager-i-sys.md) |
