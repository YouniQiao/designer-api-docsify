# PhotoPickerComponent

Declare struct PhotoPickerComponent

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct PhotoPickerComponent--><!--Device-unnamed-export declare struct PhotoPickerComponent-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## build

```TypeScript
@Builder
  build(): void
```

Build function of PhotoPickerComponent

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-@Builder  build(): void--><!--Device-PhotoPickerComponent-@Builder  build(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onCurrentAlbumDeleted

```TypeScript
onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback
```

Callback when the current album is deleted

**Type:** [CurrentAlbumDeletedCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-currentalbumdeletedcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback--><!--Device-PhotoPickerComponent-onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onDeselect

```TypeScript
onDeselect?: DeSelectCallback
```

Callback when Deselect photos or videos

**Type:** [DeSelectCallback](arkts-na-deselectcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onDeselect?: DeSelectCallback--><!--Device-PhotoPickerComponent-onDeselect?: DeSelectCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onEnterPhotoBrowser

```TypeScript
onEnterPhotoBrowser?: EnterPhotoBrowserCallback
```

Callback when enter photo browser, will return photoBrowserInfo

**Type:** [EnterPhotoBrowserCallback](arkts-na-enterphotobrowsercallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onEnterPhotoBrowser?: EnterPhotoBrowserCallback--><!--Device-PhotoPickerComponent-onEnterPhotoBrowser?: EnterPhotoBrowserCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onError

```TypeScript
onError?: ErrorCallback
```

Callback when an error occurs in the PhotoPickerComponent.

**Type:** [ErrorCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-errorcallback-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onError?: ErrorCallback--><!--Device-PhotoPickerComponent-onError?: ErrorCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onExceedMaxSelected

```TypeScript
onExceedMaxSelected?: ExceedMaxSelectedCallback
```

Callback when exceed max selected

**Type:** [ExceedMaxSelectedCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-exceedmaxselectedcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onExceedMaxSelected?: ExceedMaxSelectedCallback--><!--Device-PhotoPickerComponent-onExceedMaxSelected?: ExceedMaxSelectedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onExitPhotoBrowser

```TypeScript
onExitPhotoBrowser?: ExitPhotoBrowserCallback
```

Callback when exit photo browser, will return photoBrowserInfo

**Type:** [ExitPhotoBrowserCallback](arkts-na-exitphotobrowsercallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onExitPhotoBrowser?: ExitPhotoBrowserCallback--><!--Device-PhotoPickerComponent-onExitPhotoBrowser?: ExitPhotoBrowserCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onItemClicked

```TypeScript
onItemClicked?: ItemClickedCallback
```

Callback when click item. include click camera item and thumbnail item, will return itemInfo

**Type:** [ItemClickedCallback](arkts-na-itemclickedcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onItemClicked?: ItemClickedCallback--><!--Device-PhotoPickerComponent-onItemClicked?: ItemClickedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onItemClickedNotify

```TypeScript
onItemClickedNotify?: ItemClickedNotifyCallback
```

Callback when click item. Includes camera items and thumbnail items. Returns itemInfo in the callback. Must be used in conjunction with the addData method.

**Type:** [ItemClickedNotifyCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-itemclickednotifycallback-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onItemClickedNotify?: ItemClickedNotifyCallback--><!--Device-PhotoPickerComponent-onItemClickedNotify?: ItemClickedNotifyCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onMovingPhotoBadgeStateChanged

```TypeScript
onMovingPhotoBadgeStateChanged?: MovingPhotoBadgeStateChangedCallback
```

Callback when moving photo badge state changed

**Type:** [MovingPhotoBadgeStateChangedCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-movingphotobadgestatechangedcallback-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onMovingPhotoBadgeStateChanged?: MovingPhotoBadgeStateChangedCallback--><!--Device-PhotoPickerComponent-onMovingPhotoBadgeStateChanged?: MovingPhotoBadgeStateChangedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPhotoBrowserChangeStart

```TypeScript
onPhotoBrowserChangeStart?: PhotoBrowserChangeStartCallback
```

Callback when photo browser change start (upon user swipe release), will return targetPhotoInfo

**Type:** [PhotoBrowserChangeStartCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photobrowserchangestartcallback-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onPhotoBrowserChangeStart?: PhotoBrowserChangeStartCallback--><!--Device-PhotoPickerComponent-onPhotoBrowserChangeStart?: PhotoBrowserChangeStartCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPhotoBrowserChanged

```TypeScript
onPhotoBrowserChanged?: PhotoBrowserChangedCallback
```

Callback when photo browser change, will return browserItemInfo

**Type:** [PhotoBrowserChangedCallback](arkts-na-photobrowserchangedcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onPhotoBrowserChanged?: PhotoBrowserChangedCallback--><!--Device-PhotoPickerComponent-onPhotoBrowserChanged?: PhotoBrowserChangedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPhotoBrowserZoom

```TypeScript
onPhotoBrowserZoom?: PhotoBrowserZoomCallback
```

Callback when the zoom scale changes during large image browsing.

**Type:** [PhotoBrowserZoomCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photobrowserzoomcallback-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onPhotoBrowserZoom?: PhotoBrowserZoomCallback--><!--Device-PhotoPickerComponent-onPhotoBrowserZoom?: PhotoBrowserZoomCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPickerControllerReady

```TypeScript
onPickerControllerReady?: PickerControllerReadyCallback
```

Callback when pickerController is ready. Set data to picker component by pickerController is supported after pickerController is ready

**Type:** [PickerControllerReadyCallback](arkts-na-pickercontrollerreadycallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onPickerControllerReady?: PickerControllerReadyCallback--><!--Device-PhotoPickerComponent-onPickerControllerReady?: PickerControllerReadyCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPinchGridSwitched

```TypeScript
onPinchGridSwitched?: PinchGridSwitchedCallback
```

Callback when the grid's level is switched via pinch gesture.

**Type:** [PinchGridSwitchedCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-pinchgridswitchedcallback-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onPinchGridSwitched?: PinchGridSwitchedCallback--><!--Device-PhotoPickerComponent-onPinchGridSwitched?: PinchGridSwitchedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onScrollStopAtEnd

```TypeScript
onScrollStopAtEnd?: ScrollStopAtEndCallback
```

Callback when the grid stops scrolling at the ending position.

**Type:** [ScrollStopAtEndCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-scrollstopatendcallback-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onScrollStopAtEnd?: ScrollStopAtEndCallback--><!--Device-PhotoPickerComponent-onScrollStopAtEnd?: ScrollStopAtEndCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onScrollStopAtStart

```TypeScript
onScrollStopAtStart?: ScrollStopAtStartCallback
```

Callback when the grid stops scrolling at the starting position.

**Type:** [ScrollStopAtStartCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-scrollstopatstartcallback-t.md)

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onScrollStopAtStart?: ScrollStopAtStartCallback--><!--Device-PhotoPickerComponent-onScrollStopAtStart?: ScrollStopAtStartCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onSelect

```TypeScript
onSelect?: SelectCallback
```

Callback when select photos or videos

**Type:** [SelectCallback](arkts-na-selectcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onSelect?: SelectCallback--><!--Device-PhotoPickerComponent-onSelect?: SelectCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onSelectedItemsDeleted

```TypeScript
onSelectedItemsDeleted?: ItemsDeletedCallback
```

Callback when selected items are deleted

**Type:** [ItemsDeletedCallback](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-itemsdeletedcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onSelectedItemsDeleted?: ItemsDeletedCallback--><!--Device-PhotoPickerComponent-onSelectedItemsDeleted?: ItemsDeletedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onVideoPlayStateChanged

```TypeScript
onVideoPlayStateChanged?: VideoPlayStateChangedCallback
```

Callback when the video play state changed

**Type:** [VideoPlayStateChangedCallback](arkts-na-videoplaystatechangedcallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-onVideoPlayStateChanged?: VideoPlayStateChangedCallback--><!--Device-PhotoPickerComponent-onVideoPlayStateChanged?: VideoPlayStateChangedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## pickerController

```TypeScript
@ObjectLink
  pickerController: PickerController
```

PickerController

**Type:** [PickerController](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-pickercontroller-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-@ObjectLink  pickerController: PickerController--><!--Device-PhotoPickerComponent-@ObjectLink  pickerController: PickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## pickerOptions

```TypeScript
pickerOptions?: PickerOptions
```

PickerOptions

**Type:** [PickerOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-file-photopickercomponent-pickeroptions-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-PhotoPickerComponent-pickerOptions?: PickerOptions--><!--Device-PhotoPickerComponent-pickerOptions?: PickerOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

