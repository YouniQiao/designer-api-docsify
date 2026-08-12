# PhotoAssetChangeInfo

Describes the information about a media asset.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-interface PhotoAssetChangeInfo--><!--Device-photoAccessHelper-interface PhotoAssetChangeInfo-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## albumUri

```TypeScript
albumUri: string
```

URI of the album that the media asset belongs to.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetChangeInfo-albumUri: string--><!--Device-PhotoAssetChangeInfo-albumUri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isFavorite

```TypeScript
isFavorite: boolean
```

Whether the media asset is marked as a favorite. **true** if marked, **false** otherwise.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetChangeInfo-isFavorite: boolean--><!--Device-PhotoAssetChangeInfo-isFavorite: boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## mediaType

```TypeScript
mediaType: PhotoType
```

Type of the media asset (image or video).

**Type:** PhotoType

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetChangeInfo-mediaType: PhotoType--><!--Device-PhotoAssetChangeInfo-mediaType: PhotoType-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## uri

```TypeScript
uri: string
```

URI of the media asset.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetChangeInfo-uri: string--><!--Device-PhotoAssetChangeInfo-uri: string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

