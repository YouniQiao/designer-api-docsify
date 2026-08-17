# AlbumChangeData

Describes the change data of an album.

**Since:** 23

<!--Device-photoAccessHelper-interface AlbumChangeData--><!--Device-photoAccessHelper-interface AlbumChangeData-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from 'photoAccessHelper';
```

## albumAfterChange

```TypeScript
albumAfterChange: AlbumChangeInfo | null
```

Data of the album after change. In the case of album deletion, **albumAfterChange** is null.

**Type:** [AlbumChangeInfo](arkts-medialibrary-photoaccesshelper-albumchangeinfo-i.md) \| null

**Since:** 23

<!--Device-AlbumChangeData-albumAfterChange: AlbumChangeInfo | null--><!--Device-AlbumChangeData-albumAfterChange: AlbumChangeInfo | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumBeforeChange

```TypeScript
albumBeforeChange: AlbumChangeInfo | null
```

Data of the album before change. If an album is added, **albumBeforeChange** is null.

**Type:** [AlbumChangeInfo](arkts-medialibrary-photoaccesshelper-albumchangeinfo-i.md) \| null

**Since:** 23

<!--Device-AlbumChangeData-albumBeforeChange: AlbumChangeInfo | null--><!--Device-AlbumChangeData-albumBeforeChange: AlbumChangeInfo | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

