# @ohos.file.PhotoPickerComponent(A component which support other applications to select photos or videos)

## 导入模块

```TypeScript
import { MaxCountType, PreselectedInfo, BaseItemInfo, ItemInfo, AnimatorParams, SelectMode, PhotoBrowserUIElement, ItemType, PinchGridSwitchedCallback, SingleLineConfig, ClickResult, ClickType, UpdatablePickerConfigs, DataType, VideoPlayerState, ItemDisplayRatio, ScrollStopAtStartCallback, ScrollStopAtEndCallback, PickerOrientation, videoPlayStateChangedCallback, PhotoBrowserChangeStartCallback, MovingPhotoBadgeStateChangedCallback, ErrorCallback, PickerOptions, ItemsDeletedCallback, PhotoBrowserRange, SaveMode, MaxSelected, PickerController, PickerError, PhotoPickerComponent, ExceedMaxSelectedCallback, ReminderMode, ItemClickedNotifyCallback, PickerColorMode, BadgeConfig, BadgeType, PhotoBrowserInfo, CurrentAlbumDeletedCallback } from 'kits/@kit.MediaLibraryKit';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [AnimatorParams](arkts-medialibrary-file-photopickercomponent-animatorparams-c.md) | AnimatorParams |
| [BadgeConfig](arkts-medialibrary-file-photopickercomponent-badgeconfig-c.md) | BadgeConfig |
| [BaseItemInfo](arkts-medialibrary-file-photopickercomponent-baseiteminfo-c.md) | BaseItemInfo |
| [CompletedResult](arkts-medialibrary-file-photopickercomponent-completedresult-c.md) | CompletedResult |
| [ItemInfo](arkts-medialibrary-file-photopickercomponent-iteminfo-c.md) | ItemInfo |
| [MaxSelected](arkts-medialibrary-file-photopickercomponent-maxselected-c.md) | MaxSelected |
| [PhotoBrowserInfo](arkts-medialibrary-file-photopickercomponent-photobrowserinfo-c.md) | PhotoBrowserInfo |
| [PickerController](arkts-medialibrary-file-photopickercomponent-pickercontroller-c.md) | The class for PickerController |
| [PickerOptions](arkts-medialibrary-file-photopickercomponent-pickeroptions-c.md) | PickerOptions Object |
| [PreselectedInfo](arkts-medialibrary-file-photopickercomponent-preselectedinfo-c.md) | PreselectedInfo |
| [SingleLineConfig](arkts-medialibrary-file-photopickercomponent-singlelineconfig-c.md) | Single-Line display mode. |

### 结构体

| 名称 | 说明 |
| --- | --- |
| [PhotoPickerComponent](arkts-medialibrary-file-photopickercomponent-photopickercomponent-s.md) | Declare struct PhotoPickerComponent |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [BadgeType](arkts-medialibrary-file-photopickercomponent-badgetype-e.md) | BadgeType. |
| [ClickType](arkts-medialibrary-file-photopickercomponent-clicktype-e.md) | ClickType. include SELECTED and DESELECTED |
| [DataType](arkts-medialibrary-file-photopickercomponent-datatype-e.md) | DataType represents the type of the data set to picker component |
| [ItemDisplayRatio](arkts-medialibrary-file-photopickercomponent-itemdisplayratio-e.md) | Enumerates the aspect ratios of the grid item display, including 1:1 and the original image's aspect ratio. |
| [ItemType](arkts-medialibrary-file-photopickercomponent-itemtype-e.md) | ItemType. include CAMERA and THUMBNAIL |
| [MaxCountType](arkts-medialibrary-file-photopickercomponent-maxcounttype-e.md) | MaxCountType. include TOTAL_MAX_COUNT, PHOTO_MAX_COUNT and VIDEO_MAX_COUNT |
| [PhotoBrowserRange](arkts-medialibrary-file-photopickercomponent-photobrowserrange-e.md) | PhotoBrowserRange. include ALL and SELECTED_ONLY |
| [PhotoBrowserUIElement](arkts-medialibrary-file-photopickercomponent-photobrowseruielement-e.md) | PhotoBrowserUIElement. include CHECKBOX and BACK_BUTTON |
| [PickerColorMode](arkts-medialibrary-file-photopickercomponent-pickercolormode-e.md) | PickerColorMode. include AUTO, LIGHT and DARK |
| [PickerOrientation](arkts-medialibrary-file-photopickercomponent-pickerorientation-e.md) | PickerOrientation. include VERTICAL and HORIZONTAL |
| [ReminderMode](arkts-medialibrary-file-photopickercomponent-remindermode-e.md) | ReminderMode, include NONE, TOAST and MASK |
| [SaveMode](arkts-medialibrary-file-photopickercomponent-savemode-e.md) | Enumeration type of save mode. |
| [SelectMode](arkts-medialibrary-file-photopickercomponent-selectmode-e.md) | SelectMode. include SINGLE_SELECT and MULTI_SELECT |
| [VideoPlayerState](arkts-medialibrary-file-photopickercomponent-videoplayerstate-e.md) | VideoPlayerState. include PLAYING, PAUSED, STOPPED, SEEK_START and SEEK_FINISH |

### 类型

| 名称 | 说明 |
| --- | --- |
| [CurrentAlbumDeletedCallback](arkts-medialibrary-currentalbumdeletedcallback-t.md) | The callback of onCurrentAlbumDeleted event |
| [DeSelectCallback](arkts-medialibrary-deselectcallback-t.md) | The callback of onDeSelected event |
| [EnterPhotoBrowserCallback](arkts-medialibrary-enterphotobrowsercallback-t.md) | The callback of enterPhotoBrowser event |
| [ExceedMaxSelectedCallback](arkts-medialibrary-exceedmaxselectedcallback-t.md) | The callback of onExceedMaxSelected event |
| [ExitPhotoBrowserCallback](arkts-medialibrary-exitphotobrowsercallback-t.md) | The callback of exitPhotoBrowser event |
| [ItemClickedCallback](arkts-medialibrary-itemclickedcallback-t.md) | The callback of itemClicked event |
| [ItemsDeletedCallback](arkts-medialibrary-itemsdeletedcallback-t.md) | The callback of onSelectedItemsDeleted event |
| [PhotoBrowserChangedCallback](arkts-medialibrary-photobrowserchangedcallback-t.md) | The callback of onPhotoBrowserChanged event |
| [PhotoBrowserZoomCallback](arkts-medialibrary-photobrowserzoomcallback-t.md) | The callback of onPhotoBrowserZoom event |
| [PickerControllerReadyCallback](arkts-medialibrary-pickercontrollerreadycallback-t.md) | The callback of pickerControllerReady event |
| [SelectCallback](arkts-medialibrary-selectcallback-t.md) | The callback of onSelected event |
| [VideoPlayStateChangedCallback](arkts-medialibrary-videoplaystatechangedcallback-t.md) | The callback of onVideoPlayStateChanged event |

