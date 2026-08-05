# PhotoAssetChangeData

Describes the change data of a media asset.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-interface PhotoAssetChangeData--><!--Device-photoAccessHelper-interface PhotoAssetChangeData-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## assetAfterChange

```TypeScript
assetAfterChange: PhotoAssetChangeInfo | null
```

Data of the media asset after change. In the case of asset deletion, **assetAfterChange** is null.

**Type:** PhotoAssetChangeInfo \| null

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetChangeData-assetAfterChange: PhotoAssetChangeInfo | null--><!--Device-PhotoAssetChangeData-assetAfterChange: PhotoAssetChangeInfo | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## assetBeforeChange

```TypeScript
assetBeforeChange: PhotoAssetChangeInfo | null
```

Data of the media asset before change. In the case of asset addition, **assetBeforeChange** is null.

**Type:** PhotoAssetChangeInfo \| null

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetChangeData-assetBeforeChange: PhotoAssetChangeInfo | null--><!--Device-PhotoAssetChangeData-assetBeforeChange: PhotoAssetChangeInfo | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isContentChanged

```TypeScript
isContentChanged: boolean
```

Whether the content of the media asset is changed. **true** if changed, **false** otherwise.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetChangeData-isContentChanged: boolean--><!--Device-PhotoAssetChangeData-isContentChanged: boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## isDeleted

```TypeScript
isDeleted: boolean
```

Whether the media asset is deleted. **true** if deleted, **false** otherwise.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PhotoAssetChangeData-isDeleted: boolean--><!--Device-PhotoAssetChangeData-isDeleted: boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

