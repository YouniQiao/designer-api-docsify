# @ohos.file.PhotoPickerComponent

## Modules to Import

```TypeScript
import { PhotoPickerComponent, PickerController, PickerOptions, DataType, BaseItemInfo, ItemInfo, PhotoBrowserInfo, AnimatorParams, MaxSelected, ItemType, ClickType, PickerOrientation, SelectMode, PickerColorMode, ReminderMode, MaxCountType, PhotoBrowserRange, PhotoBrowserUIElement, ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback, videoPlayStateChangedCallback, MovingPhotoBadgeStateChangedCallback, UpdatablePickerConfigs, SingleLineConfig, BadgeConfig, PreselectedInfo, SaveMode, BadgeType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ItemClickedNotifyCallback, ScrollStopAtEndCallback, PhotoBrowserChangeStartCallback, PinchGridSwitchedCallback, ErrorCallback, ClickResult, PickerError } from '@kit.MediaLibraryKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AnimatorParams](arkts-medialibrary-filephotopickercomponent-animatorparams-c.md) | Defines animation parameters for entering or exiting the photo browser page. |
| [BadgeConfig](arkts-medialibrary-filephotopickercomponent-badgeconfig-c.md) | Describes the badge configuration. |
| [BaseItemInfo](arkts-medialibrary-filephotopickercomponent-baseiteminfo-c.md) | Represents basic image and video information. |
| [ClickResult](arkts-medialibrary-filephotopickercomponent-clickresult-c.md) | Sets whether the asset with the specified URI is selected. |
| [CompletedResult](arkts-medialibrary-filephotopickercomponent-completedresult-c.md) | Defines the information about the Picker's state from the last exit. |
| [ItemInfo](arkts-medialibrary-filephotopickercomponent-iteminfo-c.md) | It inherits from [BaseItemInfo](arkts-medialibrary-filephotopickercomponent-baseiteminfo-c.md), adding the parameter **itemType**. |
| [MaxSelected](arkts-medialibrary-filephotopickercomponent-maxselected-c.md) | Represents the maximum number of media assets that can be selected at a time. |
| [PhotoBrowserInfo](arkts-medialibrary-filephotopickercomponent-photobrowserinfo-c.md) | Represents information about the photo browser page. |
| [PickerController](arkts-medialibrary-filephotopickercomponent-pickercontroller-c.md) | Defines an instance used to send data to the **PhotoPickerComponent**. |
| [PickerError](arkts-medialibrary-filephotopickercomponent-pickererror-c.md) | Describes the function name, error code, and message of the error returned when an error occurs during the use of the **PhotoPickerComponent** component. |
| [PickerOptions](arkts-medialibrary-filephotopickercomponent-pickeroptions-c.md) | Describes the configuration of a Picker. It inherits from [photoAccessHelper.BaseSelectOptions](arkts-medialibrary-photoaccesshelper-baseselectoptions-c.md). |
| [PreselectedInfo](arkts-medialibrary-filephotopickercomponent-preselectedinfo-c.md) | Describes the information about the preselected files and their corresponding **PhotoPickerComponent** index. |
| [RecoveryResult](arkts-medialibrary-filephotopickercomponent-recoveryresult-c.md) | RecoveryResult |
| [SingleLineConfig](arkts-medialibrary-filephotopickercomponent-singlelineconfig-c.md) | Represents the single-line display mode. In single-line mode, the component does not provide functions for viewing a larger image. The component does not support callbacks related to large images, and the PickerController does not support APIs related to large images, making API calls ineffective. |
| [UnselectableItemInfo](arkts-medialibrary-filephotopickercomponent-unselectableiteminfo-c.md) | UnselectableItemInfo |
| [UpdatablePickerConfigs](arkts-medialibrary-filephotopickercomponent-updatablepickerconfigs-c.md) | Describes the updatable attributes of the **PhotoPickerComponent**. These attributes are a subset of [PickerOptions](arkts-medialibrary-filephotopickercomponent-pickeroptions-c.md). |

### Structs

| Name | Description |
| --- | --- |
| [PhotoPickerComponent](arkts-medialibrary-filephotopickercomponent-photopickercomponent-s.md) | PhotoPickerComponent({ pickerOptions?: PickerOptions, onSelect?: (uri: string) =&gt; void, onDeselect?: (uri: string) =&gt; void, onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) =&gt; boolean, onItemClickedNotify?: ItemClickedNotifyCallback, onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) =&gt; boolean, onExitPhotoBrowser? : (photoBrowserInfo: PhotoBrowserInfo) =&gt; boolean, onPickerControllerReady?: () =&gt; void, onPhotoBrowserChanged?: ( browserItemInfo: BaseItemInfo) =&gt; boolean, onSelectedItemsDeleted?: ItemsDeletedCallback, onExceedMaxSelected?: ExceedMaxSelectedCallback, onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback, onVideoPlayStateChanged?: videoPlayStateChangedCallback, pickerController: PickerController }) |

### Enums

| Name | Description |
| --- | --- |
| [BadgeType](arkts-medialibrary-filephotopickercomponent-badgetype-e.md) | Enumerates the badge types. |
| [ClickType](arkts-medialibrary-filephotopickercomponent-clicktype-e.md) | Enumerates the click operation types. |
| [DataType](arkts-medialibrary-filephotopickercomponent-datatype-e.md) | Enumerates the types of data sent from **PickerController** to the **PhotoPickerComponent**. |
| [ItemDisplayRatio](arkts-medialibrary-filephotopickercomponent-itemdisplayratio-e.md) | Enumerates the aspect ratios for grid display in single-line display mode. |
| [ItemType](arkts-medialibrary-filephotopickercomponent-itemtype-e.md) | Enumerates the types of the item clicked. |
| [MaxCountType](arkts-medialibrary-filephotopickercomponent-maxcounttype-e.md) | Enumerates the types of the maximum count. |
| [PhotoBrowserRange](arkts-medialibrary-filephotopickercomponent-photobrowserrange-e.md) | Enumerates the view range on the photo browser page. |
| [PhotoBrowserUIElement](arkts-medialibrary-filephotopickercomponent-photobrowseruielement-e.md) | Represents other UI elements except the image preview component on the photo browser page. |
| [PickerColorMode](arkts-medialibrary-filephotopickercomponent-pickercolormode-e.md) | Enumerates the Picker color modes. |
| [PickerOrientation](arkts-medialibrary-filephotopickercomponent-pickerorientation-e.md) | Enumerates the sliding preview directions of the Picker grid page. |
| [ReminderMode](arkts-medialibrary-filephotopickercomponent-remindermode-e.md) | Enumerates the types of the reminder when the number of selected items reaches the maximum. |
| [SaveMode](arkts-medialibrary-filephotopickercomponent-savemode-e.md) | Enumerates the modes for saving images or videos. |
| [SelectMode](arkts-medialibrary-filephotopickercomponent-selectmode-e.md) | Enumerates the selection modes. |
| [VideoPlayerState](arkts-medialibrary-filephotopickercomponent-videoplayerstate-e.md) | Enumerates the video playback states. |

### Types

| Name | Description |
| --- | --- |
| [CurrentAlbumDeletedCallback](arkts-medialibrary-currentalbumdeletedcallback-t.md) | Called when the current album is deleted. |
| [ErrorCallback](arkts-medialibrary-errorcallback-t.md) | Callback to be invoked when an error occurs in the **PhotoPickerComponent**. |
| [ExceedMaxSelectedCallback](arkts-medialibrary-exceedmaxselectedcallback-t.md) | Called when items are selected after the maximum count has been reached. |
| [ItemClickedNotifyCallback](arkts-medialibrary-itemclickednotifycallback-t.md) | Callback to be invoked when an item in a **PhotoPickerComponent** is clicked. |
| [ItemsDeletedCallback](arkts-medialibrary-itemsdeletedcallback-t.md) | Called when the selected items are deleted. |
| [MovingPhotoBadgeStateChangedCallback](arkts-medialibrary-movingphotobadgestatechangedcallback-t.md) | Callback to be invoked when the moving photo effect of the **PhotoPickerComponent** is enabled or disabled. |
| [PhotoBrowserChangeStartCallback](arkts-medialibrary-photobrowserchangestartcallback-t.md) | Callback to be invoked when a grid view switches to the photo browser page or the photo browser page is switched. |
| [PhotoBrowserZoomCallback](arkts-medialibrary-photobrowserzoomcallback-t.md) | Callback to be invoked when the large image is zoomed in or out after the large image is entered through the **PhotoPickerComponent**. |
| [PickerRecoveryCallback](arkts-medialibrary-pickerrecoverycallback-t.md) | The callback of onPickerRecovery event |
| [PinchGridSwitchedCallback](arkts-medialibrary-pinchgridswitchedcallback-t.md) | Callback to be invoked when a user pinches a grid component. |
| [ScrollStopAtEndCallback](arkts-medialibrary-scrollstopatendcallback-t.md) | Callback to be invoked when the user stops scrolling and is positioned at the end of the grid content in the **PhotoPickerComponent**. |
| [ScrollStopAtStartCallback](arkts-medialibrary-scrollstopatstartcallback-t.md) | Callback to be invoked when the user stops scrolling and is positioned at the beginning of the grid content in the **PhotoPickerComponent**. |
| [UnselectableItemClickedCallback](arkts-medialibrary-unselectableitemclickedcallback-t.md) | The callback of onUnselectableItemInfo event |
| [videoPlayStateChangedCallback](arkts-medialibrary-videoplaystatechangedcallback-t.md) | Callback to be invoked when the video playback state on a photo browser page changes. |

