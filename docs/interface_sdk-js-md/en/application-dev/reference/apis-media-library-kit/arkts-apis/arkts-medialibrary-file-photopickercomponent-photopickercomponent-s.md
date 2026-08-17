# PhotoPickerComponent

PhotoPickerComponent({ pickerOptions?: PickerOptions, onSelect?: (uri: string) => void, onDeselect?: (uri: string) => void, onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean, onItemClickedNotify?: ItemClickedNotifyCallback, onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean, onExitPhotoBrowser? : (photoBrowserInfo: PhotoBrowserInfo) => boolean, onPickerControllerReady?: () => void, onPhotoBrowserChanged?: ( browserItemInfo: BaseItemInfo) => boolean, onSelectedItemsDeleted?: ItemsDeletedCallback, onExceedMaxSelected?: ExceedMaxSelectedCallback, onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback, onVideoPlayStateChanged?: videoPlayStateChangedCallback, pickerController: PickerController }) Allows the application to access images or videos in the user directory without any permission. > **NOTE：**> > If the **PhotoPickerComponent** is used with the **Tabs** component, the swipe gestures of the **Tabs** component > conflict with those of the photo browser page. > > To prevent this problem, you can disable the swipe operation for the **Tabs** component in > **onEnterPhotoBrowser()** and enable it in **onExitPhotoBrowser()**. This conflict will be resolved in later > versions.

**Since:** 12

<!--Device-unnamed-export declare struct PhotoPickerComponent--><!--Device-unnamed-export declare struct PhotoPickerComponent-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { PhotoPickerComponent } from 'PhotoPickerComponent';
import { PickerController } from 'PickerController';
import { PickerOptions } from 'PickerOptions';
import { DataType } from 'DataType';
import { BaseItemInfo } from 'BaseItemInfo';
import { ItemInfo } from 'ItemInfo';
import { PhotoBrowserInfo } from 'PhotoBrowserInfo';
import { AnimatorParams } from 'AnimatorParams';
import { MaxSelected } from 'MaxSelected';
import { ItemType } from 'ItemType';
import { ClickType } from 'ClickType';
import { PickerOrientation } from 'PickerOrientation';
import { SelectMode } from 'SelectMode';
import { PickerColorMode } from 'PickerColorMode';
import { ReminderMode } from 'ReminderMode';
import { MaxCountType } from 'MaxCountType';
import { PhotoBrowserRange } from 'PhotoBrowserRange';
import { PhotoBrowserUIElement } from 'PhotoBrowserUIElement';
import { ItemsDeletedCallback } from 'ItemsDeletedCallback';
import { ExceedMaxSelectedCallback } from 'ExceedMaxSelectedCallback';
import { CurrentAlbumDeletedCallback } from 'CurrentAlbumDeletedCallback';
import { videoPlayStateChangedCallback } from 'videoPlayStateChangedCallback';
import { MovingPhotoBadgeStateChangedCallback } from 'MovingPhotoBadgeStateChangedCallback';
import { UpdatablePickerConfigs } from 'UpdatablePickerConfigs';
import { SingleLineConfig } from 'SingleLineConfig';
import { BadgeConfig } from 'BadgeConfig';
import { PreselectedInfo } from 'PreselectedInfo';
import { SaveMode } from 'SaveMode';
import { BadgeType } from 'BadgeType';
import { VideoPlayerState } from 'VideoPlayerState';
import { ItemDisplayRatio } from 'ItemDisplayRatio';
import { ScrollStopAtStartCallback } from 'ScrollStopAtStartCallback';
import { ItemClickedNotifyCallback } from 'ItemClickedNotifyCallback';
import { ScrollStopAtEndCallback } from 'ScrollStopAtEndCallback';
import { PhotoBrowserChangeStartCallback } from 'PhotoBrowserChangeStartCallback';
import { PinchGridSwitchedCallback } from 'PinchGridSwitchedCallback';
import { ErrorCallback } from 'ErrorCallback';
import { ClickResult } from 'ClickResult';
import { PickerError } from 'PickerError';
```

## build

```TypeScript
@Builder
  build(): void
```

Build function of PhotoPickerComponent

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-@Builder  build(): void--><!--Device-PhotoPickerComponent-@Builder  build(): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onCurrentAlbumDeleted

```TypeScript
onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback
```

Callback when the current album is deleted

**Type:** [CurrentAlbumDeletedCallback](arkts-medialibrary-currentalbumdeletedcallback-t.md)

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-PhotoPickerComponent-onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback--><!--Device-PhotoPickerComponent-onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onDeselect

```TypeScript
onDeselect?: (uri: string) => void
```

Callback when Deselect photos or videos

**Type:** (uri: string) =&gt; void

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-onDeselect?: (uri: string) => void--><!--Device-PhotoPickerComponent-onDeselect?: (uri: string) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onEnterPhotoBrowser

```TypeScript
onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean
```

Callback when enter photo browser, will return photoBrowserInfo

**Type:** (photoBrowserInfo: PhotoBrowserInfo) =&gt; boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean--><!--Device-PhotoPickerComponent-onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onError

```TypeScript
onError?: ErrorCallback
```

Callback when an error occurs in the PhotoPickerComponent.

**Type:** [ErrorCallback](arkts-medialibrary-errorcallback-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoPickerComponent-onError?: ErrorCallback--><!--Device-PhotoPickerComponent-onError?: ErrorCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onExceedMaxSelected

```TypeScript
onExceedMaxSelected?: ExceedMaxSelectedCallback
```

Callback when exceed max selected

**Type:** [ExceedMaxSelectedCallback](arkts-medialibrary-exceedmaxselectedcallback-t.md)

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-PhotoPickerComponent-onExceedMaxSelected?: ExceedMaxSelectedCallback--><!--Device-PhotoPickerComponent-onExceedMaxSelected?: ExceedMaxSelectedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onExitPhotoBrowser

```TypeScript
onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean
```

Callback when exit photo browser, will return photoBrowserInfo

**Type:** (photoBrowserInfo: PhotoBrowserInfo) =&gt; boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean--><!--Device-PhotoPickerComponent-onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onItemClicked

```TypeScript
onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean
```

Callback when click item. include click camera item and thumbnail item, will return itemInfo

**Type:** (itemInfo: ItemInfo, clickType: ClickType) =&gt; boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean--><!--Device-PhotoPickerComponent-onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onItemClickedNotify

```TypeScript
onItemClickedNotify?: ItemClickedNotifyCallback
```

Callback when click item. Includes camera items and thumbnail items. Returns itemInfo in the callback. Must be used in conjunction with the addData method.

**Type:** [ItemClickedNotifyCallback](arkts-medialibrary-itemclickednotifycallback-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoPickerComponent-onItemClickedNotify?: ItemClickedNotifyCallback--><!--Device-PhotoPickerComponent-onItemClickedNotify?: ItemClickedNotifyCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onMovingPhotoBadgeStateChanged

```TypeScript
onMovingPhotoBadgeStateChanged?: MovingPhotoBadgeStateChangedCallback
```

Callback when moving photo badge state changed

**Type:** [MovingPhotoBadgeStateChangedCallback](arkts-medialibrary-movingphotobadgestatechangedcallback-t.md)

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-PhotoPickerComponent-onMovingPhotoBadgeStateChanged?: MovingPhotoBadgeStateChangedCallback--><!--Device-PhotoPickerComponent-onMovingPhotoBadgeStateChanged?: MovingPhotoBadgeStateChangedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPhotoBrowserChangeStart

```TypeScript
onPhotoBrowserChangeStart?: PhotoBrowserChangeStartCallback
```

Callback when photo browser change start (upon user swipe release), will return targetPhotoInfo

**Type:** [PhotoBrowserChangeStartCallback](arkts-medialibrary-photobrowserchangestartcallback-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoPickerComponent-onPhotoBrowserChangeStart?: PhotoBrowserChangeStartCallback--><!--Device-PhotoPickerComponent-onPhotoBrowserChangeStart?: PhotoBrowserChangeStartCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPhotoBrowserChanged

```TypeScript
onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) => boolean
```

Callback when photo browser change, will return browserItemInfo

**Type:** (browserItemInfo: BaseItemInfo) =&gt; boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) => boolean--><!--Device-PhotoPickerComponent-onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) => boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPhotoBrowserZoom

```TypeScript
onPhotoBrowserZoom?: PhotoBrowserZoomCallback
```

Callback when the zoom scale changes during large image browsing.

**Type:** [PhotoBrowserZoomCallback](arkts-medialibrary-photobrowserzoomcallback-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PhotoPickerComponent-onPhotoBrowserZoom?: PhotoBrowserZoomCallback--><!--Device-PhotoPickerComponent-onPhotoBrowserZoom?: PhotoBrowserZoomCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPickerControllerReady

```TypeScript
onPickerControllerReady?: () => void
```

Callback when pickerController is ready. Set data to picker component by pickerController is supported after pickerController is ready

**Type:** () =&gt; void

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-onPickerControllerReady?: () => void--><!--Device-PhotoPickerComponent-onPickerControllerReady?: () => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPickerRecovery

```TypeScript
onPickerRecovery?: PickerRecoveryCallback
```

Callback when the photo picker restores the previously grid state.

**Type:** [PickerRecoveryCallback](arkts-medialibrary-pickerrecoverycallback-t.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PhotoPickerComponent-onPickerRecovery?: PickerRecoveryCallback--><!--Device-PhotoPickerComponent-onPickerRecovery?: PickerRecoveryCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onPinchGridSwitched

```TypeScript
onPinchGridSwitched?: PinchGridSwitchedCallback
```

Callback when the grid's level is switched via pinch gesture.

**Type:** [PinchGridSwitchedCallback](arkts-medialibrary-pinchgridswitchedcallback-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoPickerComponent-onPinchGridSwitched?: PinchGridSwitchedCallback--><!--Device-PhotoPickerComponent-onPinchGridSwitched?: PinchGridSwitchedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onScrollStopAtEnd

```TypeScript
onScrollStopAtEnd?: ScrollStopAtEndCallback
```

Callback when the grid stops scrolling at the ending position.

**Type:** [ScrollStopAtEndCallback](arkts-medialibrary-scrollstopatendcallback-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoPickerComponent-onScrollStopAtEnd?: ScrollStopAtEndCallback--><!--Device-PhotoPickerComponent-onScrollStopAtEnd?: ScrollStopAtEndCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onScrollStopAtStart

```TypeScript
onScrollStopAtStart?: ScrollStopAtStartCallback
```

Callback when the grid stops scrolling at the starting position.

**Type:** [ScrollStopAtStartCallback](arkts-medialibrary-scrollstopatstartcallback-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-PhotoPickerComponent-onScrollStopAtStart?: ScrollStopAtStartCallback--><!--Device-PhotoPickerComponent-onScrollStopAtStart?: ScrollStopAtStartCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onSelect

```TypeScript
onSelect?: (uri: string) => void
```

Callback when select photos or videos

**Type:** (uri: string) =&gt; void

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-onSelect?: (uri: string) => void--><!--Device-PhotoPickerComponent-onSelect?: (uri: string) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onSelectedItemsDeleted

```TypeScript
onSelectedItemsDeleted?: ItemsDeletedCallback
```

Callback when selected items are deleted

**Type:** [ItemsDeletedCallback](arkts-medialibrary-itemsdeletedcallback-t.md)

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-PhotoPickerComponent-onSelectedItemsDeleted?: ItemsDeletedCallback--><!--Device-PhotoPickerComponent-onSelectedItemsDeleted?: ItemsDeletedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onUnselectableItemClicked

```TypeScript
onUnselectableItemClicked?: UnselectableItemClickedCallback
```

Callback when an unselectable item is clicked.

**Type:** [UnselectableItemClickedCallback](arkts-medialibrary-unselectableitemclickedcallback-t.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-PhotoPickerComponent-onUnselectableItemClicked?: UnselectableItemClickedCallback--><!--Device-PhotoPickerComponent-onUnselectableItemClicked?: UnselectableItemClickedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onVideoPlayStateChanged

```TypeScript
onVideoPlayStateChanged?: videoPlayStateChangedCallback
```

Callback when the video play state changed

**Type:** [videoPlayStateChangedCallback](arkts-medialibrary-videoplaystatechangedcallback-t.md)

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PhotoPickerComponent-onVideoPlayStateChanged?: videoPlayStateChangedCallback--><!--Device-PhotoPickerComponent-onVideoPlayStateChanged?: videoPlayStateChangedCallback-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## pickerController

```TypeScript
@ObjectLink
  pickerController: PickerController
```

PickerController

**Type:** [PickerController](arkts-medialibrary-file-photopickercomponent-pickercontroller-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-@ObjectLink  pickerController: PickerController--><!--Device-PhotoPickerComponent-@ObjectLink  pickerController: PickerController-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## pickerOptions

```TypeScript
pickerOptions?: PickerOptions
```

PickerOptions

**Type:** [PickerOptions](arkts-medialibrary-file-photopickercomponent-pickeroptions-c.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PhotoPickerComponent-pickerOptions?: PickerOptions--><!--Device-PhotoPickerComponent-pickerOptions?: PickerOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

