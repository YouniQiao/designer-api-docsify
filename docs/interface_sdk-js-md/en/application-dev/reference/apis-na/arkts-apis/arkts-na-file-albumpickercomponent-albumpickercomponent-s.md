# AlbumPickerComponent

AlbumPickerComponent: can select a certain album and display the images in that album through PhotoPickerComponent

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare struct AlbumPickerComponent--><!--Device-unnamed-export declare struct AlbumPickerComponent-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

Build function of AlbumPickerComponent

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlbumPickerComponent-@Builder  build(): void--><!--Device-AlbumPickerComponent-@Builder  build(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumPickerController

```TypeScript
albumPickerController?: AlbumPickerController
```

AlbumPickerController

**Type:** [AlbumPickerController](arkts-na-file-albumpickercomponent-albumpickercontroller-c.md)

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlbumPickerComponent-albumPickerController?: AlbumPickerController--><!--Device-AlbumPickerComponent-albumPickerController?: AlbumPickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumPickerOptions

```TypeScript
albumPickerOptions?: AlbumPickerOptions
```

AlbumPickerOptions

**Type:** [AlbumPickerOptions](arkts-na-file-albumpickercomponent-albumpickeroptions-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlbumPickerComponent-albumPickerOptions?: AlbumPickerOptions--><!--Device-AlbumPickerComponent-albumPickerOptions?: AlbumPickerOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onAlbumClick

```TypeScript
onAlbumClick?: AlbumClickCallback
```

Callback when select an album, will return album uri

**Type:** [AlbumClickCallback](arkts-na-albumclickcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlbumPickerComponent-onAlbumClick?: AlbumClickCallback--><!--Device-AlbumPickerComponent-onAlbumClick?: AlbumClickCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onEmptyAreaClick

```TypeScript
onEmptyAreaClick?: EmptyAreaClickCallback
```

Callback when click the empty area of the album component

**Type:** [EmptyAreaClickCallback](arkts-na-emptyareaclickcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AlbumPickerComponent-onEmptyAreaClick?: EmptyAreaClickCallback--><!--Device-AlbumPickerComponent-onEmptyAreaClick?: EmptyAreaClickCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

