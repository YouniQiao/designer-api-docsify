# AlbumPickerComponent

AlbumPickerComponent( {albumPickerOptions?: AlbumPickerOptions, onAlbumClick?: (albumInfo: AlbumInfo) => boolean, onEmptyAreaClick?: EmptyAreaClickCallback, albumPickerController?: AlbumPickerController }) The **AlbumPickerComponent** embedded in the UI of an application allows the application to access the albums in the user directory without any permission.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct AlbumPickerComponent--><!--Device-unnamed-export declare struct AlbumPickerComponent-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { EmptyAreaClickCallback, AlbumPickerComponent, AlbumInfo, AlbumPickerOptions, AlbumPickerController } from '@kit.MediaLibraryKit';
```

## albumPickerController

```TypeScript
albumPickerController?: AlbumPickerController
```

AlbumPickerController

**Type:** [AlbumPickerController](../../apis-na/arkts-apis/arkts-na-file-albumpickercomponent-albumpickercontroller-c.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AlbumPickerComponent-albumPickerController?: AlbumPickerController--><!--Device-AlbumPickerComponent-albumPickerController?: AlbumPickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## albumPickerOptions

```TypeScript
albumPickerOptions?: AlbumPickerOptions
```

AlbumPickerOptions

**Type:** [AlbumPickerOptions](../../apis-na/arkts-apis/arkts-na-file-albumpickercomponent-albumpickeroptions-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlbumPickerComponent-albumPickerOptions?: AlbumPickerOptions--><!--Device-AlbumPickerComponent-albumPickerOptions?: AlbumPickerOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onAlbumClick

```TypeScript
onAlbumClick?: (albumInfo: AlbumInfo) => boolean
```

Callback when select an album, will return album uri

**Type:** (albumInfo: AlbumInfo) =&gt; boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AlbumPickerComponent-onAlbumClick?: (albumInfo: AlbumInfo) => boolean--><!--Device-AlbumPickerComponent-onAlbumClick?: (albumInfo: AlbumInfo) => boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onEmptyAreaClick

```TypeScript
onEmptyAreaClick?: EmptyAreaClickCallback
```

Callback when click the empty area of the album component

**Type:** [EmptyAreaClickCallback](../../apis-na/arkts-apis/arkts-na-emptyareaclickcallback-t.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-AlbumPickerComponent-onEmptyAreaClick?: EmptyAreaClickCallback--><!--Device-AlbumPickerComponent-onEmptyAreaClick?: EmptyAreaClickCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

