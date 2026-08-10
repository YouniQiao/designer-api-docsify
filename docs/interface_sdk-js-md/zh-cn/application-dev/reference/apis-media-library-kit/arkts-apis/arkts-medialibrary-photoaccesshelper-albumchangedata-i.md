# AlbumChangeData

Describes the change data of an album.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface AlbumChangeData--><!--Device-photoAccessHelper-interface AlbumChangeData-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## albumAfterChange

```TypeScript
albumAfterChange: AlbumChangeInfo | null
```

Data of the album after change. In the case of album deletion, **albumAfterChange** is null.

**类型：** [AlbumChangeInfo](arkts-medialibrary-photoaccesshelper-albumchangeinfo-i.md) \| null

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeData-albumAfterChange: AlbumChangeInfo | null--><!--Device-AlbumChangeData-albumAfterChange: AlbumChangeInfo | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumBeforeChange

```TypeScript
albumBeforeChange: AlbumChangeInfo | null
```

Data of the album before change. If an album is added, **albumBeforeChange** is null.

**类型：** [AlbumChangeInfo](arkts-medialibrary-photoaccesshelper-albumchangeinfo-i.md) \| null

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AlbumChangeData-albumBeforeChange: AlbumChangeInfo | null--><!--Device-AlbumChangeData-albumBeforeChange: AlbumChangeInfo | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

