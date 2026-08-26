# @ohos.file.PhotoPickerComponent(PhotoPickerComponent)

You can embed the **PhotoPickerComponent** in your application's layout to let users pick images or videos without
 requiring extra permissions. Once the users have made their selection, your application gets read-only access to the
 chosen images or videos.
 Note that **PhotoPickerComponent** does not support nesting. Additionally, prevent overlaying components with the
 **overlay** attribute or of higher levels on top it, as this will prevent it from receiving gesture events.
 Once embedded, users can directly select images or videos within the **PhotoPickerComponent**.
 > **NOTE**
 >
 > - This component does not support [same-layer rendering](../../../web/web-same-layer.md).
 ###### Attributes
 The universal attributes are supported.


## Modules to Import

```TypeScript
import { PhotoPickerComponent, PickerController, PickerOptions, DataType, BaseItemInfo, ItemInfo, PhotoBrowserInfo, AnimatorParams, MaxSelected, ItemType, ClickType, PickerOrientation, SelectMode, PickerColorMode, ReminderMode, MaxCountType, PhotoBrowserRange, PhotoBrowserUIElement, ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback, videoPlayStateChangedCallback, MovingPhotoBadgeStateChangedCallback, UpdatablePickerConfigs, SingleLineConfig, BadgeConfig, PreselectedInfo, SaveMode, BadgeType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ItemClickedNotifyCallback, ScrollStopAtEndCallback, PhotoBrowserChangeStartCallback, PinchGridSwitchedCallback, ErrorCallback, ClickResult, PickerError } from '@kit.MediaLibraryKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AnimatorParams(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-animatorparams-c.md) | Defines animation parameters for entering or exiting the photo browser page. |
| [BadgeConfig(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-badgeconfig-c.md) | Describes the badge configuration. |
| [BaseItemInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-baseiteminfo-c.md) | Represents basic image and video information. |
| [ClickResult(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-clickresult-c.md) | Sets whether the asset with the specified URI is selected. |
| [CompletedResult(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-completedresult-c.md) | Defines the information about the Picker's state from the last exit. |
| [ItemInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | It inherits from [BaseItemInfo](arkts-medialibrary-file-photopickercomponent-baseiteminfo-c.md), adding the parameter **itemType**.Represents basic image and video information. |
| [MaxSelected(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-maxselected-c.md) | Represents the maximum number of media assets that can be selected at a time. |
| [PhotoBrowserInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-photobrowserinfo-c.md) | Represents information about the photo browser page. |
| [PickerController(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickercontroller-c.md) | Defines an instance used to send data to the **PhotoPickerComponent**. |
| [PickerError(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickererror-c.md) | Describes the function name, error code, and message of the error returned when an error occurs during the use of the **PhotoPickerComponent** component. |
| [PickerOptions(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickeroptions-c.md) | Describes the configuration of a Picker. It inherits from [photoAccessHelper.BaseSelectOptions](arkts-medialibrary-photoaccesshelper-baseselectoptions-c.md). |
| [PreselectedInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-preselectedinfo-c.md) | Describes the information about the preselected files and their corresponding **PhotoPickerComponent** index. |
| [RecoveryResult(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-recoveryresult-c.md) | [RecoveryResult](arkts-medialibrary-file-photopickercomponent-recoveryresult-c.md) |
| [SingleLineConfig(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-singlelineconfig-c.md) | Represents the single-line display mode. In single-line mode, the component does not provide functions for viewing a larger image. The component does not support callbacks related to large images, and the PickerController does not support APIs related to large images, making API calls ineffective. |
| [UnselectableItemInfo(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-unselectableiteminfo-c.md) | [UnselectableItemInfo](arkts-medialibrary-file-photopickercomponent-unselectableiteminfo-c.md) |
| [UpdatablePickerConfigs(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-updatablepickerconfigs-c.md) | Describes the updatable attributes of the **PhotoPickerComponent**. These attributes are a subset of [PickerOptions](arkts-medialibrary-file-photopickercomponent-pickeroptions-c.md). |

### Structs

| Name | Description |
| --- | --- |
| [PhotoPickerComponent(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-photopickercomponent-s.md) | PhotoPickerComponent({ pickerOptions?: PickerOptions, onSelect?: (uri: string) = & gt; void, onDeselect?: (uri: string) = & gt; void, onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) = & gt; boolean, onItemClickedNotify?: ItemClickedNotifyCallback, onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) = & gt; boolean, onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) = & gt; boolean, onPickerControllerReady?: () = & gt; void, onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) = & gt; boolean, onSelectedItemsDeleted?: ItemsDeletedCallback, onExceedMaxSelected?: ExceedMaxSelectedCallback, onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback, onVideoPlayStateChanged?: videoPlayStateChangedCallback, pickerController: PickerController })Allows the application to access images or videos in the user directory without any permission. |

### Enums

| Name | Description |
| --- | --- |
| [BadgeType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-badgetype-e.md) | Enumerates the badge types. |
| [ClickType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-clicktype-e.md) | Enumerates the click operation types. |
| [DataType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | Enumerates the types of data sent from **PickerController** to the **PhotoPickerComponent**. |
| [ItemDisplayRatio(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-itemdisplayratio-e.md) | Enumerates the aspect ratios for grid display in single-line display mode. |
| [ItemType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-itemtype-e.md) | Enumerates the types of the item clicked. |
| [MaxCountType(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-maxcounttype-e.md) | Enumerates the types of the maximum count. |
| [PhotoBrowserRange(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-photobrowserrange-e.md) | Enumerates the view range on the photo browser page. |
| [PhotoBrowserUIElement(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-photobrowseruielement-e.md) | Represents other UI elements except the image preview component on the photo browser page. |
| [PickerColorMode(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickercolormode-e.md) | Enumerates the Picker color modes. |
| [PickerOrientation(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-pickerorientation-e.md) | Enumerates the sliding preview directions of the Picker grid page.This capability can be configured since API version 20. If this capability is set since API version 12 to 19, the setting does not take effect and the default direction (vertical) is used. |
| [ReminderMode(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-remindermode-e.md) | Enumerates the types of the reminder when the number of selected items reaches the maximum. |
| [SaveMode(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-savemode-e.md) | Enumerates the modes for saving images or videos. |
| [SelectMode(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-selectmode-e.md) | Enumerates the selection modes. |
| [VideoPlayerState(PhotoPickerComponent)](arkts-medialibrary-file-photopickercomponent-videoplayerstate-e.md) | Enumerates the video playback states. |

### Types

| Name | Description |
| --- | --- |
| [CurrentAlbumDeletedCallback(PhotoPickerComponent)](arkts-medialibrary-currentalbumdeletedcallback-t.md) | Called when the current album is deleted. |
| [ErrorCallback(PhotoPickerComponent)](arkts-medialibrary-errorcallback-t.md) | Callback to be invoked when an error occurs in the **PhotoPickerComponent**. |
| [ExceedMaxSelectedCallback(PhotoPickerComponent)](arkts-medialibrary-exceedmaxselectedcallback-t.md) | Called when items are selected after the maximum count has been reached. |
| [ItemClickedNotifyCallback(PhotoPickerComponent)](arkts-medialibrary-itemclickednotifycallback-t.md) | Callback to be invoked when an item in a **PhotoPickerComponent** is clicked. |
| [ItemsDeletedCallback(PhotoPickerComponent)](arkts-medialibrary-itemsdeletedcallback-t.md) | Called when the selected items are deleted. |
| [MovingPhotoBadgeStateChangedCallback(PhotoPickerComponent)](arkts-medialibrary-movingphotobadgestatechangedcallback-t.md) | Callback to be invoked when the moving photo effect of the **PhotoPickerComponent** is enabled or disabled. |
| [PhotoBrowserChangeStartCallback(PhotoPickerComponent)](arkts-medialibrary-photobrowserchangestartcallback-t.md) | Callback to be invoked when a grid view switches to the photo browser page or the photo browser page is switched. |
| [PhotoBrowserZoomCallback(PhotoPickerComponent)](arkts-medialibrary-photobrowserzoomcallback-t.md) | Callback to be invoked when the large image is zoomed in or out after the large image is entered through the **PhotoPickerComponent**. |
| [PickerRecoveryCallback(PhotoPickerComponent)](arkts-medialibrary-pickerrecoverycallback-t.md) | The callback of onPickerRecovery event |
| [PinchGridSwitchedCallback(PhotoPickerComponent)](arkts-medialibrary-pinchgridswitchedcallback-t.md) | Callback to be invoked when a user pinches a grid component. |
| [ScrollStopAtEndCallback(PhotoPickerComponent)](arkts-medialibrary-scrollstopatendcallback-t.md) | Callback to be invoked when the user stops scrolling and is positioned at the end of the grid content in the **PhotoPickerComponent**. |
| [ScrollStopAtStartCallback(PhotoPickerComponent)](arkts-medialibrary-scrollstopatstartcallback-t.md) | Callback to be invoked when the user stops scrolling and is positioned at the beginning of the grid content in the **PhotoPickerComponent**. |
| [UnselectableItemClickedCallback(PhotoPickerComponent)](arkts-medialibrary-unselectableitemclickedcallback-t.md) | The callback of onUnselectableItemInfo event |
| [videoPlayStateChangedCallback(PhotoPickerComponent)](arkts-medialibrary-videoplaystatechangedcallback-t.md) | Callback to be invoked when the video playback state on a photo browser page changes. |
