# PhotoPickerComponent

Declare struct PhotoPickerComponent

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Component

<!--Device-unnamed-export declare struct PhotoPickerComponent--><!--Device-unnamed-export declare struct PhotoPickerComponent-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## build

```TypeScript
build(): void
```

Build function of PhotoPickerComponent

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-build(): void--><!--Device-PhotoPickerComponent-build(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onCurrentAlbumDeleted

```TypeScript
onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback
```

Callback when the current album is deleted

**Type:** CurrentAlbumDeletedCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback--><!--Device-PhotoPickerComponent-onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onDeselect

```TypeScript
onDeselect?: DeSelectCallback
```

Callback when Deselect photos or videos

**Type:** DeSelectCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onDeselect?: DeSelectCallback--><!--Device-PhotoPickerComponent-onDeselect?: DeSelectCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onEnterPhotoBrowser

```TypeScript
onEnterPhotoBrowser?: EnterPhotoBrowserCallback
```

Callback when enter photo browser, will return photoBrowserInfo

**Type:** EnterPhotoBrowserCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onEnterPhotoBrowser?: EnterPhotoBrowserCallback--><!--Device-PhotoPickerComponent-onEnterPhotoBrowser?: EnterPhotoBrowserCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onExceedMaxSelected

```TypeScript
onExceedMaxSelected?: ExceedMaxSelectedCallback
```

Callback when exceed max selected

**Type:** ExceedMaxSelectedCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onExceedMaxSelected?: ExceedMaxSelectedCallback--><!--Device-PhotoPickerComponent-onExceedMaxSelected?: ExceedMaxSelectedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onExitPhotoBrowser

```TypeScript
onExitPhotoBrowser?: ExitPhotoBrowserCallback
```

Callback when exit photo browser, will return photoBrowserInfo

**Type:** ExitPhotoBrowserCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onExitPhotoBrowser?: ExitPhotoBrowserCallback--><!--Device-PhotoPickerComponent-onExitPhotoBrowser?: ExitPhotoBrowserCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onItemClicked

```TypeScript
onItemClicked?: ItemClickedCallback
```

Callback when click item. include click camera item and thumbnail item, will return itemInfo

**Type:** ItemClickedCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onItemClicked?: ItemClickedCallback--><!--Device-PhotoPickerComponent-onItemClicked?: ItemClickedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPhotoBrowserChanged

```TypeScript
onPhotoBrowserChanged?: PhotoBrowserChangedCallback
```

Callback when photo browser change, will return browserItemInfo

**Type:** PhotoBrowserChangedCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onPhotoBrowserChanged?: PhotoBrowserChangedCallback--><!--Device-PhotoPickerComponent-onPhotoBrowserChanged?: PhotoBrowserChangedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPhotoBrowserZoom

```TypeScript
onPhotoBrowserZoom?: PhotoBrowserZoomCallback
```

Callback when the zoom scale changes during large image browsing.

**Type:** PhotoBrowserZoomCallback

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onPhotoBrowserZoom?: PhotoBrowserZoomCallback--><!--Device-PhotoPickerComponent-onPhotoBrowserZoom?: PhotoBrowserZoomCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPickerControllerReady

```TypeScript
onPickerControllerReady?: PickerControllerReadyCallback
```

Callback when pickerController is ready. Set data to picker component by pickerController is supported after pickerController is ready

**Type:** PickerControllerReadyCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onPickerControllerReady?: PickerControllerReadyCallback--><!--Device-PhotoPickerComponent-onPickerControllerReady?: PickerControllerReadyCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onSelect

```TypeScript
onSelect?: SelectCallback
```

Callback when select photos or videos

**Type:** SelectCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onSelect?: SelectCallback--><!--Device-PhotoPickerComponent-onSelect?: SelectCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onSelectedItemsDeleted

```TypeScript
onSelectedItemsDeleted?: ItemsDeletedCallback
```

Callback when selected items are deleted

**Type:** ItemsDeletedCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onSelectedItemsDeleted?: ItemsDeletedCallback--><!--Device-PhotoPickerComponent-onSelectedItemsDeleted?: ItemsDeletedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onVideoPlayStateChanged

```TypeScript
onVideoPlayStateChanged?: VideoPlayStateChangedCallback
```

Callback when the video play state changed

**Type:** VideoPlayStateChangedCallback

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onVideoPlayStateChanged?: VideoPlayStateChangedCallback--><!--Device-PhotoPickerComponent-onVideoPlayStateChanged?: VideoPlayStateChangedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## pickerController

```TypeScript
pickerController: PickerController
```

PickerController

**Type:** PickerController

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @ObjectLink

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-pickerController: PickerController--><!--Device-PhotoPickerComponent-pickerController: PickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## pickerOptions

```TypeScript
pickerOptions?: PickerOptions
```

PickerOptions

**Type:** PickerOptions

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-pickerOptions?: PickerOptions--><!--Device-PhotoPickerComponent-pickerOptions?: PickerOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

